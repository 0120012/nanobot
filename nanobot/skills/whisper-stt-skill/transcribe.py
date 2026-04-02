#!/usr/bin/env python3
"""
Whisper.cpp 语音转文字工具（固定 base 模型）
依赖: whisper-cli, ffmpeg, ggml-base.bin
"""

import argparse
import hashlib
import json
import os
import select
import subprocess
import sys
import tempfile
import time
from pathlib import Path

DEFAULT_IDLE_TTL = 90
DEFAULT_LANG = "zh"
DEFAULT_MODEL_FILE = "ggml-base.bin"
DEFAULT_TRANSCRIBE_TIMEOUT_SEC = 180
WHISPER_CLI_PATH = Path.home() / ".local" / "bin" / "whisper-cli"
MODEL_PATH = Path("/www") / ".cache" / "whisper.cpp" / DEFAULT_MODEL_FILE
CACHE_FILE = Path(
    os.environ.get(
        "OPENCLAW_WHISPER_CACHE_FILE",
        str(Path.home() / ".cache" / "openclaw-whisper-stt" / "transcribe_cache.json"),
    )
)


def resolve_whisper_cli() -> str:
    """定位 whisper.cpp 可执行文件路径"""
    # Why: 与安装脚本保持单一路径约定，避免 PATH 命中错误二进制。
    if WHISPER_CLI_PATH.is_file():
        return str(WHISPER_CLI_PATH)
    raise RuntimeError(f"未找到 whisper-cli: {WHISPER_CLI_PATH}")


def resolve_model_path() -> Path:
    """定位 base 模型文件路径"""
    # Why: 与下载脚本默认目录对齐，减少多路径分支造成的部署歧义。
    if MODEL_PATH.is_file():
        return MODEL_PATH
    raise FileNotFoundError(f"未找到模型文件: {MODEL_PATH}")



def load_transcribe_cache(cache_file: Path) -> dict[str, str]:
    """读取磁盘缓存"""
    # Why: 缓存必须跨进程生效，才能在宿主重启技能进程时仍复用结果。
    if not cache_file.is_file():
        return {}
    try:
        raw = json.loads(cache_file.read_text(encoding="utf-8"))
    except Exception:
        return {}
    if not isinstance(raw, dict):
        return {}
    return {
        str(k): str(v)
        for k, v in raw.items()
        if isinstance(k, str) and isinstance(v, str)
    }


def save_transcribe_cache(cache_file: Path, cache: dict[str, str]) -> None:
    """保存磁盘缓存"""
    # Why: 先写临时文件再替换，避免进程中断导致缓存文件半写损坏。
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = cache_file.with_suffix(".tmp")
    payload = json.dumps(cache, ensure_ascii=False)
    tmp_path.write_text(payload, encoding="utf-8")
    tmp_path.replace(cache_file)


def build_cache_key(src: Path, model_path: Path) -> str:
    """构造缓存键"""
    # Why: 路径+尺寸+mtime+模型信息足够表达“同一输入语音上下文”。
    stat = src.stat()
    raw = "|".join(
        [
            str(src.resolve()),
            str(stat.st_size),
            str(stat.st_mtime_ns),
            str(model_path.resolve()),
            DEFAULT_LANG,
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def transcribe_audio(
    audio_path: str,
    cli_path: str,
    model_path: Path,
    cache: dict[str, str],
    cache_file: Path,
) -> str:
    """执行单条语音识别"""
    src = Path(audio_path).expanduser()
    if not src.exists() or not src.is_file():
        raise FileNotFoundError(f"文件不存在: {src}")

    cache_key = build_cache_key(src, model_path)
    if cache_key in cache:
        return cache[cache_key]

    with tempfile.TemporaryDirectory(prefix="whispercpp_") as tmpdir:
        out_prefix = Path(tmpdir) / "result"
        cmd = [
            cli_path,
            "-m",
            str(model_path),
            "-f",
            str(src),
            "-l",
            DEFAULT_LANG,
            "-otxt",
            "-of",
            str(out_prefix),
            "-nt",
            "-np",
        ]

        # Why: 捕获 stderr/stdout，识别失败时把根因回传给上层 AI 便于快速排障。
        proc = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=DEFAULT_TRANSCRIBE_TIMEOUT_SEC,
        )
        if proc.returncode != 0:
            detail = proc.stderr.strip() or proc.stdout.strip() or "unknown error"
            raise RuntimeError(f"whisper-cli 执行失败: {detail}")

        txt_path = Path(f"{out_prefix}.txt")
        if not txt_path.exists():
            raise RuntimeError("whisper-cli 未生成文本输出")

        text = txt_path.read_text(encoding="utf-8").strip()
        cache[cache_key] = text
        save_transcribe_cache(cache_file, cache)
        return text


def run_serve_mode(cli_path: str, model_path: Path, cache_file: Path) -> int:
    """持续模式：串行接收音频路径并逐条返回结果"""
    # Why: 保持单进程串行交互，兼顾连续请求低延迟与90秒空闲自动退出。
    cache = load_transcribe_cache(cache_file)
    stdin_closed = False
    print(
        f"服务模式已启动: backend=whisper.cpp, model={model_path.name}, idle_ttl={DEFAULT_IDLE_TTL}s"
    )
    print(f"缓存文件: {cache_file}，已加载 {len(cache)} 条。")
    print("输入一行一个音频文件路径；输入 quit/exit 主动退出。")
    sys.stdout.flush()

    last_active_at = time.time()
    while True:
        elapsed = time.time() - last_active_at
        if elapsed >= DEFAULT_IDLE_TTL:
            print(f"空闲超过 {DEFAULT_IDLE_TTL}s，服务模式退出。")
            return 0

        if stdin_closed:
            time.sleep(0.2)
            continue

        timeout = max(0.0, DEFAULT_IDLE_TTL - elapsed)
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if not ready:
            continue

        raw = sys.stdin.readline()
        if raw == "":
            # Why: 某些宿主会在单次写入后关闭 stdin；此处延迟退出避免“识别完立刻退”。
            stdin_closed = True
            print("输入流已关闭，将在空闲超时后退出。")
            sys.stdout.flush()
            continue

        audio_path = raw.strip()
        if not audio_path:
            continue

        if audio_path.lower() in {"quit", "exit"}:
            print("收到退出指令，服务模式退出。")
            return 0

        try:
            text = transcribe_audio(audio_path, cli_path, model_path, cache, cache_file)
            print("<<<RESULT_BEGIN>>>")
            print(text)
            print("<<<RESULT_END>>>")
        except Exception as e:
            print(f"<<<ERROR>>> {e}")
        finally:
            last_active_at = time.time()
            sys.stdout.flush()


def main() -> int:
    parser = argparse.ArgumentParser(description="Whisper.cpp 语音转文字（base，90s空闲退出）")
    parser.add_argument("--serve", action="store_true", help="持续模式：从stdin逐行读取音频路径")
    args = parser.parse_args()

    try:
        if not args.serve:
            raise ValueError("仅支持 --serve 模式")

        cli_path = resolve_whisper_cli()
        model_path = resolve_model_path()
        return run_serve_mode(cli_path, model_path, CACHE_FILE)
    except Exception as e:
        print(f"错误: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
