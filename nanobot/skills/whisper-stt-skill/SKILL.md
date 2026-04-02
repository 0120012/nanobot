---
name: local-whisper-cpp
description: Local speech-to-text using whisper-cli (whisper.cpp) with base model.
---

# Local Whisper (cpp)

使用 `whisper-cli` 在本地离线转写语音，固定使用 `base` 模型（`ggml-base.bin`）。
当前实现固定中文识别（`-l zh`）。

## 使用方式

持续串行模式（仅此模式）：

```bash
python3 transcribe.py --serve
```

输入规则（`--serve`）：
- 调用方通过 `stdin` 写入音频文件路径。
- 严格串行：必须等待上一条处理完成后再发送下一条。
- 在收到上述结束标记之前，禁止发送下一条音频路径。
- 输入 `quit` 或 `exit` 主动退出。
- 空闲 90 秒自动退出。

输出规则：
- 成功结果包裹在 `<<<RESULT_BEGIN>>>` 与 `<<<RESULT_END>>>`。
- 失败输出：`<<<ERROR>>> <错误信息>`。
- 单条语音识别超时为 180 秒。

## 模型与路径

固定路径（与脚本实现一致）：
- whisper-cli：`~/.local/bin/whisper-cli`
- 模型文件：`/www/.cache/whisper.cpp/ggml-base.bin`

## 安装

在本 skill 目录执行：

```bash
bash scripts/install_whisper_cpp.sh
bash scripts/download_models.sh base
```

说明：
- `install_whisper_cpp.sh` 固定构建 `whisper.cpp v1.8.4`。
- `download_models.sh base` 默认下载到 `/www/.cache/whisper.cpp/`。
- `download_models.sh` 内置了 `base` 模型 SHA256 校验；可用 `OPENCLAW_WHISPER_SHA256_BASE` 覆盖。

## 说明

- 转写过程本地执行，不依赖联网。
- 只有“下载模型文件”这一步需要网络。
- 支持 MP3/WAV/M4A/OGG/FLAC/WebM（由 ffmpeg 解码）。
