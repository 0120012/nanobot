<div align="center">
  <img src="nanobot_logo.png" alt="nanobot" width="500">
  <h1>nanobot：超轻量个人 AI 助手</h1>
  <p>
    <a href="https://pypi.org/project/nanobot-ai/"><img src="https://img.shields.io/pypi/v/nanobot-ai" alt="PyPI"></a>
    <a href="https://pepy.tech/project/nanobot-ai"><img src="https://static.pepy.tech/badge/nanobot-ai" alt="Downloads"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
    <a href="https://discord.gg/MnCvHqpUGB"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
</div>

🐈 **nanobot** 是一个受 [OpenClaw](https://github.com/openclaw/openclaw) 启发的**超轻量**个人 AI 助手。

⚡️ 以比 OpenClaw **少 99% 的代码行数**提供核心 Agent 能力。

📏 实时代码行统计：随时运行 `bash core_agent_lines.sh` 验证。

## 📢 新闻

> [!IMPORTANT]
> **安全说明：** 由于 `litellm` 供应链投毒事件，**请尽快检查你的 Python 环境**，并参考此[安全公告](https://github.com/HKUDS/nanobot/discussions/2445)。我们已在[此提交](https://github.com/HKUDS/nanobot/commit/3dfdab7)中完全移除 `litellm` 依赖。

- **2026-03-21** 🔒 用原生 `openai` + `anthropic` SDK 替换 `litellm`。见[提交](https://github.com/HKUDS/nanobot/commit/3dfdab7)。
- **2026-03-20** 🧙 交互式初始化向导：可选择 provider、模型自动补全，快速可用。
- **2026-03-19** 💬 Telegram 在高负载下更稳定；Feishu 代码块渲染更正确。
- **2026-03-18** 📷 Telegram 现可通过 URL 发送媒体；Cron 计划展示更易读。
- **2026-03-17** ✨ Feishu 格式化体验升级、Slack 完成后自动反应、自定义端点支持额外 headers、图片处理更可靠。
- **2026-03-16** 🚀 发布 **v0.1.4.post5**：聚焦打磨与稳定性，增强各渠道支持与日常可用性。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post5)。
- **2026-03-15** 🧩 钉钉富媒体、内置技能更智能、模型兼容性更干净。
- **2026-03-14** 💬 渠道插件、Feishu 回复能力，以及 MCP/QQ/媒体处理稳定性提升。
- **2026-03-13** 🌐 多 provider 网络搜索、LangSmith，以及更广泛稳定性改进。
- **2026-03-12** 🚀 VolcEngine 支持、Telegram 回复上下文、`/restart` 与更稳健记忆。
- **2026-03-11** 🔌 WeCom、Ollama、更清晰发现流程与更安全工具行为。
- **2026-03-10** 🧠 基于 token 的记忆、统一重试机制、网关和 Telegram 行为更整洁。
- **2026-03-09** 💬 Slack 线程优化与 Feishu 音频兼容性改进。
- **2026-03-08** 🚀 发布 **v0.1.4.post4**：高可靠版本，含更安全默认值、更好的多实例支持、更稳健 MCP，以及重大渠道与 provider 改进。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post4)。
- **2026-03-07** 🚀 Azure OpenAI provider、WhatsApp 媒体、QQ 群聊，以及更多 Telegram/Feishu 打磨。
- **2026-03-06** 🪄 更轻量 providers、更智能媒体处理、更稳健记忆与 CLI 兼容性。

<details>
<summary>更早新闻</summary>

- **2026-03-05** ⚡️ Telegram 草稿流式输出、MCP SSE 支持、更多渠道稳定性修复。
- **2026-03-04** 🛠️ 依赖清理、更安全文件读取，以及新一轮测试与 Cron 修复。
- **2026-03-03** 🧠 用户消息合并更干净、多模态保存更安全、Cron 保护更强。
- **2026-03-02** 🛡️ 默认访问控制更安全、Cron 重载更稳、Matrix 媒体处理更清晰。
- **2026-03-01** 🌐 Web 代理支持、Cron 提醒更智能、Feishu 富文本解析改进。
- **2026-02-28** 🚀 发布 **v0.1.4.post3**：上下文更干净、会话历史更稳固、Agent 更智能。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post3)。
- **2026-02-27** 🧠 实验性 thinking 模式支持、钉钉媒体消息、Feishu 与 QQ 渠道修复。
- **2026-02-26** 🛡️ 会话投毒修复、WhatsApp 去重、Windows 路径保护、Mistral 兼容。
- **2026-02-25** 🧹 新增 Matrix 渠道、会话上下文更整洁、workspace 模板自动同步。
- **2026-02-24** 🚀 发布 **v0.1.4.post2**：可靠性导向版本，重构 heartbeat、优化 prompt cache，并强化 provider 与 channel 稳定性。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post2)。
- **2026-02-23** 🔧 虚拟 tool-call heartbeat、prompt cache 优化、Slack mrkdwn 修复。
- **2026-02-22** 🛡️ Slack 线程隔离、Discord 输入状态修复、Agent 可靠性提升。
- **2026-02-21** 🎉 发布 **v0.1.4.post1**：新增 providers、跨渠道媒体支持、稳定性大幅提升。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post1)。
- **2026-02-20** 🐦 Feishu 现可接收用户多模态文件；底层记忆机制更可靠。
- **2026-02-19** ✨ Slack 可发送文件、Discord 自动拆分长消息、CLI 模式支持 subagents。
- **2026-02-18** ⚡️ nanobot 新增 VolcEngine、MCP 自定义鉴权头、Anthropic prompt caching。
- **2026-02-17** 🎉 发布 **v0.1.4**：支持 MCP、进度流式、更多 provider 与多项渠道改进。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4)。
- **2026-02-16** 🦞 nanobot 集成 [ClawHub](https://clawhub.ai) 技能，可搜索并安装公开 Agent 技能。
- **2026-02-15** 🔑 nanobot 支持 OpenAI Codex provider，并支持 OAuth 登录。
- **2026-02-14** 🔌 nanobot 支持 MCP！详见 [MCP 章节](#mcp-model-context-protocol)。
- **2026-02-13** 🎉 发布 **v0.1.3.post7**：包含安全加固与多项改进。**请升级到最新版本以修复安全问题**。详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post7)。
- **2026-02-12** 🧠 记忆系统重构：更少代码、更高可靠性。欢迎参与[讨论](https://github.com/HKUDS/nanobot/discussions/566)！
- **2026-02-11** ✨ 强化 CLI 体验并新增 MiniMax 支持！
- **2026-02-10** 🎉 发布 **v0.1.3.post6**。查看[更新说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post6)与[路线图](https://github.com/HKUDS/nanobot/discussions/431)。
- **2026-02-09** 💬 新增 Slack、Email 与 QQ 支持，nanobot 进入多平台聊天时代。
- **2026-02-08** 🔧 Provider 架构重构：新增 LLM provider 仅需两步！见[这里](#providers)。
- **2026-02-07** 🚀 发布 **v0.1.3.post5**，支持 Qwen 并含多项关键改进！详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5)。
- **2026-02-06** ✨ 新增 Moonshot/Kimi provider、Discord 集成与安全加固。
- **2026-02-05** ✨ 新增 Feishu 渠道、DeepSeek provider，并增强定时任务支持。
- **2026-02-04** 🚀 发布 **v0.1.3.post4**，支持多 provider 与 Docker！详见[发布说明](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post4)。
- **2026-02-03** ⚡ 集成 vLLM 支持本地 LLM，并改进自然语言任务调度。
- **2026-02-02** 🎉 nanobot 正式发布！欢迎体验 🐈 nanobot！

</details>

> 🐈 nanobot 仅用于教育、科研与技术交流。与加密货币无关，不涉及任何官方代币。

## nanobot 核心特性

🪶 **超轻量**：OpenClaw 的超轻实现，体积小 99%，速度显著提升。

🔬 **研究友好**：代码干净可读，易理解、易修改、易扩展。

⚡️ **极速**：更小体积意味着更快启动、更低资源占用、更快迭代。

💎 **易用**：一键部署即可开始使用。

## 🏗️ 架构

<p align="center">
  <img src="nanobot_arch.png" alt="nanobot architecture" width="800">
</p>

## 目录

- [新闻](#-新闻)
- [核心特性](#nanobot-核心特性)
- [架构](#️-架构)
- [功能](#-功能)
- [安装](#-安装)
- [快速开始](#-快速开始)
- [聊天平台](#-聊天平台)
- [Agent 社交网络](#-agent-社交网络)
- [配置](#️-配置)
- [多实例](#-多实例)
- [CLI 参考](#-cli-参考)
- [Docker](#-docker)
- [Linux 服务](#-linux-服务)
- [项目结构](#-项目结构)
- [贡献与路线图](#-贡献与路线图)
- [Star 历史](#-star-历史)

## ✨ 功能

<table align="center">
  <tr align="center">
    <th><p align="center">📈 7x24 实时市场分析</p></th>
    <th><p align="center">🚀 全栈软件工程师</p></th>
    <th><p align="center">📅 智能日常事务管理</p></th>
    <th><p align="center">📚 个人知识助手</p></th>
  </tr>
  <tr>
    <td align="center"><p align="center"><img src="case/search.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/code.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/scedule.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/memory.gif" width="180" height="400"></p></td>
  </tr>
  <tr>
    <td align="center">发现 • 洞察 • 趋势</td>
    <td align="center">开发 • 部署 • 扩展</td>
    <td align="center">计划 • 自动化 • 组织</td>
    <td align="center">学习 • 记忆 • 推理</td>
  </tr>
</table>

## 📦 安装

**从源码安装**（最新功能，推荐开发者）

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

**使用 [uv](https://github.com/astral-sh/uv) 安装**（稳定、快速）

```bash
uv tool install nanobot-ai
```

**从 PyPI 安装**（稳定）

```bash
pip install nanobot-ai
```

### 升级到最新版本

**PyPI / pip**

```bash
pip install -U nanobot-ai
nanobot --version
```

**uv**

```bash
uv tool upgrade nanobot-ai
nanobot --version
```

**使用 WhatsApp？** 升级后请重建本地 bridge：

```bash
rm -rf ~/.nanobot/bridge
nanobot channels login whatsapp
```

## 🚀 快速开始

> [!TIP]
> 在 `~/.nanobot/config.json` 中设置 API Key。
> 获取 API Key：[OpenRouter](https://openrouter.ai/keys)（全球可用）
>
> 其他 LLM provider 请见 [Providers](#providers) 章节。
>
> Web 搜索能力配置请见 [Web Search](#web-search)。

**1. 初始化**

```bash
nanobot onboard
```

如果你想用交互式向导：`nanobot onboard --wizard`。

**2. 配置**（`~/.nanobot/config.json`）

在配置里只需先设置**两个部分**（其他都有默认值）。

*设置 API Key*（例如 OpenRouter，推荐全球用户）：
```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  }
}
```

*设置模型*（可选指定 provider，默认自动检测）：
```json
{
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5",
      "provider": "openrouter"
    }
  }
}
```

**3. 开聊**

```bash
nanobot agent
```

就这样！2 分钟内就能得到一个可用的 AI 助手。

## 💬 聊天平台

把 nanobot 接入你常用的聊天平台。想自建渠道？见 [Channel Plugin Guide](./docs/CHANNEL_PLUGIN_GUIDE.md)。

| 渠道 | 你需要准备的内容 |
|---------|---------------|
| **Telegram** | 从 @BotFather 获取 Bot Token |
| **Discord** | Bot Token + Message Content intent |
| **WhatsApp** | 扫码登录（`nanobot channels login whatsapp`） |
| **WeChat (Weixin)** | 扫码登录（`nanobot channels login weixin`） |
| **Feishu** | App ID + App Secret |
| **DingTalk** | App Key + App Secret |
| **Slack** | Bot Token + App-Level Token |
| **Matrix** | Homeserver URL + Access Token |
| **Email** | IMAP/SMTP 凭据 |
| **QQ** | App ID + App Secret |
| **Wecom** | Bot ID + Bot Secret |
| **Mochat** | Claw Token（支持自动配置） |

<details>
<summary><b>Telegram</b>（推荐）</summary>

**1. 创建机器人**
- 打开 Telegram，搜索 `@BotFather`
- 发送 `/newbot`，按提示完成
- 复制 token

**2. 配置**

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["YOUR_USER_ID"]
    }
  }
}
```

> 你可以在 Telegram 设置中找到 **User ID**，显示形式为 `@yourUserId`。
> 复制该值并**去掉 `@` 前缀**后填入配置文件。


**3. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Mochat (Claw IM)</b></summary>

默认使用 **Socket.IO WebSocket**，并带有 HTTP polling 回退。

**1. 让 nanobot 自动帮你配置 Mochat**

直接给 nanobot 发送这条消息（把 `xxx@xxx` 改成你的真实邮箱）：

```
Read https://raw.githubusercontent.com/HKUDS/MoChat/refs/heads/main/skills/nanobot/skill.md and register on MoChat. My Email account is xxx@xxx Bind me as your owner and DM me on MoChat.
```

nanobot 会自动完成注册、写入 `~/.nanobot/config.json`，并连接 Mochat。

**2. 重启网关**

```bash
nanobot gateway
```

就这样，剩下的 nanobot 会自动处理！

<br>

<details>
<summary>手动配置（高级）</summary>

如果你更偏好手动配置，请在 `~/.nanobot/config.json` 中添加：

> 请妥善保管 `claw_token`。它只应通过 `X-Claw-Token` 请求头发送到你的 Mochat API 端点。

```json
{
  "channels": {
    "mochat": {
      "enabled": true,
      "base_url": "https://mochat.io",
      "socket_url": "https://mochat.io",
      "socket_path": "/socket.io",
      "claw_token": "claw_xxx",
      "agent_user_id": "6982abcdef",
      "sessions": ["*"],
      "panels": ["*"],
      "reply_delay_mode": "non-mention",
      "reply_delay_ms": 120000
    }
  }
}
```



</details>

</details>

<details>
<summary><b>Discord</b></summary>

**1. 创建机器人**
- 打开 https://discord.com/developers/applications
- 创建应用 → Bot → Add Bot
- 复制 Bot Token

**2. 开启 intents**
- 在 Bot 设置中开启 **MESSAGE CONTENT INTENT**
- （可选）若你计划基于成员信息做 allow 列表，再开启 **SERVER MEMBERS INTENT**

**3. 获取你的 User ID**
- Discord 设置 → Advanced → 开启 **Developer Mode**
- 右键你的头像 → **Copy User ID**

**4. 配置**

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["YOUR_USER_ID"],
      "groupPolicy": "mention"
    }
  }
}
```

> `groupPolicy` 控制机器人在群组频道中的响应方式：
> - `"mention"`（默认）— 仅在被 @ 时回复
> - `"open"` — 回复所有消息
> 私聊会在发送者位于 `allowFrom` 时始终回复。
> - 如果你把 group policy 设为 open，请将新线程建为 private thread，然后在其中 @ 机器人；否则线程本身及其所在频道都会生成 bot 会话。

**5. 邀请机器人**
- OAuth2 → URL Generator
- Scopes：`bot`
- Bot Permissions：`Send Messages`、`Read Message History`
- 打开生成的邀请链接，把机器人添加到你的服务器

**6. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Matrix (Element)</b></summary>

先安装 Matrix 依赖：

```bash
pip install nanobot-ai[matrix]
```

**1. 创建/选择 Matrix 账号**

- 在你的 homeserver（例如 `matrix.org`）上创建或复用一个 Matrix 账号。
- 确认可用 Element 正常登录。

**2. 获取凭据**

- 你需要：
  - `userId`（示例：`@nanobot:matrix.org`）
  - `accessToken`
  - `deviceId`（推荐；可让重启后恢复 sync token）
- 这些可从 homeserver 登录 API（`/_matrix/client/v3/login`）或客户端高级会话设置中获取。

**3. 配置**

```json
{
  "channels": {
    "matrix": {
      "enabled": true,
      "homeserver": "https://matrix.org",
      "userId": "@nanobot:matrix.org",
      "accessToken": "syt_xxx",
      "deviceId": "NANOBOT01",
      "e2eeEnabled": true,
      "allowFrom": ["@your_user:matrix.org"],
      "groupPolicy": "open",
      "groupAllowFrom": [],
      "allowRoomMentions": false,
      "maxMediaBytes": 20971520
    }
  }
}
```

> 请保持持久化 `matrix-store` 和稳定 `deviceId`。若重启后这些发生变化，加密会话状态会丢失。

| 选项 | 说明 |
|--------|-------------|
| `allowFrom` | 允许交互的用户 ID。空数组表示拒绝所有；`["*"]` 表示允许所有。 |
| `groupPolicy` | `open`（默认）、`mention` 或 `allowlist`。 |
| `groupAllowFrom` | 房间白名单（当策略为 `allowlist` 时生效）。 |
| `allowRoomMentions` | mention 模式下是否接受 `@room`。 |
| `e2eeEnabled` | 是否启用 E2EE（默认 `true`）。设为 `false` 表示仅明文。 |
| `maxMediaBytes` | 附件大小上限（默认 `20MB`）。设为 `0` 可禁用全部媒体。 |




**4. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>WhatsApp</b></summary>

需要 **Node.js ≥18**。

**1. 绑定设备**

```bash
nanobot channels login whatsapp
# 用 WhatsApp 扫码：Settings → Linked Devices
```

**2. 配置**

```json
{
  "channels": {
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["+1234567890"]
    }
  }
}
```

**3. 运行**（两个终端）

```bash
# 终端 1
nanobot channels login whatsapp

# 终端 2
nanobot gateway
```

> 已有安装不会自动应用 WhatsApp bridge 更新。
> 升级 nanobot 后，请执行：
> `rm -rf ~/.nanobot/bridge && nanobot channels login whatsapp`

</details>

<details>
<summary><b>Feishu</b></summary>

使用 **WebSocket** 长连接，无需公网 IP。

**1. 创建 Feishu 机器人**
- 访问 [Feishu Open Platform](https://open.feishu.cn/app)
- 新建应用 → 启用 **Bot** 能力
- **权限**：
  - `im:message`（发消息）和 `im:message.p2p_msg:readonly`（收消息）
  - **流式回复**（nanobot 默认）：添加 **`cardkit:card:write`**（在飞书控制台常显示为 **创建和更新卡片**）。这对 CardKit 实体和流式文本是必需的。老应用可能暂时没有该项，请在**权限管理**中勾选并按控制台要求**发布**新版本。
  - 若你**无法**添加 `cardkit:card:write`，请把 `channels.feishu` 下的 `"streaming"` 设为 `false`（见下文）。机器人仍可用，只是回复改为普通交互卡片，不做逐 token 流式输出。
- **事件**：添加 `im.message.receive_v1`（接收消息）
  - 选择 **Long Connection** 模式（需先运行 nanobot 建立连接）
- 在“凭证与基础信息”中获取 **App ID** 与 **App Secret**
- 发布应用

**2. 配置**

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxx",
      "appSecret": "xxx",
      "encryptKey": "",
      "verificationToken": "",
      "allowFrom": ["ou_YOUR_OPEN_ID"],
      "groupPolicy": "mention",
      "streaming": true
    }
  }
}
```

> `streaming` 默认是 `true`。如果你的应用没有 **`cardkit:card:write`** 权限，请改为 `false`。
> `encryptKey` 与 `verificationToken` 在 Long Connection 模式下是可选项。
> `allowFrom`：填你的 open_id（给机器人发消息后可在 nanobot 日志中看到）。使用 `["*"]` 可允许所有用户。
> `groupPolicy`：`"mention"`（默认，仅被 @ 时回复）或 `"open"`（回复群内所有消息）。私聊始终回复。

**3. 运行**

```bash
nanobot gateway
```

> [!TIP]
> Feishu 通过 WebSocket 收消息，不需要 webhook 或公网 IP！

</details>

<details>
<summary><b>QQ (QQ单聊)</b></summary>

使用 **botpy SDK** + WebSocket，无需公网 IP。目前仅支持**私聊消息**。

**1. 注册并创建机器人**
- 打开 [QQ Open Platform](https://q.qq.com) → 注册开发者（个人或企业）
- 创建新的机器人应用
- 进入 **开发设置 (Developer Settings)** → 复制 **AppID** 与 **AppSecret**

**2. 配置测试沙箱**
- 在机器人管理后台找到 **沙箱配置 (Sandbox Config)**
- 在 **在消息列表配置** 下点击 **添加成员**，添加你的 QQ 号
- 添加后，用手机 QQ 扫机器人二维码 → 打开机器人资料页 → 点击“发消息”开始测试

**3. 配置**

> - `allowFrom`：填你的 openid（给机器人发消息后在 nanobot 日志可见）。`["*"]` 表示公开访问。
> - `msgFormat`：可选。`"plain"`（默认）兼容旧版 QQ 客户端；`"markdown"` 在新客户端有更丰富格式。
> - 生产环境：请在机器人控制台提交审核并发布。完整流程见 [QQ Bot Docs](https://bot.q.qq.com/wiki/)。

```json
{
  "channels": {
    "qq": {
      "enabled": true,
      "appId": "YOUR_APP_ID",
      "secret": "YOUR_APP_SECRET",
      "allowFrom": ["YOUR_OPENID"],
      "msgFormat": "plain"
    }
  }
}
```

**4. 运行**

```bash
nanobot gateway
```

现在从 QQ 给机器人发消息，它应该会回复。

</details>

<details>
<summary><b>DingTalk (钉钉)</b></summary>

使用 **Stream Mode**，无需公网 IP。

**1. 创建钉钉机器人**
- 打开 [DingTalk Open Platform](https://open-dev.dingtalk.com/)
- 创建新应用 → 添加 **Robot** 能力
- **配置**：
  - 打开 **Stream Mode**
- **权限**：添加发送消息所需权限
- 在“凭证”中获取 **AppKey**（Client ID）和 **AppSecret**（Client Secret）
- 发布应用

**2. 配置**

```json
{
  "channels": {
    "dingtalk": {
      "enabled": true,
      "clientId": "YOUR_APP_KEY",
      "clientSecret": "YOUR_APP_SECRET",
      "allowFrom": ["YOUR_STAFF_ID"]
    }
  }
}
```

> `allowFrom`：填写你的 staff ID。`["*"]` 表示允许所有用户。

**3. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Slack</b></summary>

使用 **Socket Mode**，无需公网 URL。

**1. 创建 Slack 应用**
- 打开 [Slack API](https://api.slack.com/apps) → **Create New App** → "From scratch"
- 选择名称并绑定 workspace

**2. 配置应用**
- **Socket Mode**：开启 → 生成带 `connections:write` scope 的 **App-Level Token** → 复制（`xapp-...`）
- **OAuth & Permissions**：添加 bot scopes：`chat:write`、`reactions:write`、`app_mentions:read`
- **Event Subscriptions**：开启 → 订阅 bot events：`message.im`、`message.channels`、`app_mention` → Save Changes
- **App Home**：下拉到 **Show Tabs** → 开启 **Messages Tab** → 勾选 **Allow users to send Slash commands and messages from the messages tab**
- **Install App**：点击 **Install to Workspace** → 授权 → 复制 **Bot Token**（`xoxb-...`）

**3. 配置 nanobot**

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "botToken": "xoxb-...",
      "appToken": "xapp-...",
      "allowFrom": ["YOUR_SLACK_USER_ID"],
      "groupPolicy": "mention"
    }
  }
}
```

**4. 运行**

```bash
nanobot gateway
```

直接私聊机器人，或在频道中 @ 它，它就会回复。

> [!TIP]
> - `groupPolicy`：`"mention"`（默认，仅被 @ 时回复）、`"open"`（回复所有频道消息）或 `"allowlist"`（仅指定频道）。
> - 私聊策略默认开放。设置 `"dm": {"enabled": false}` 可禁用私聊。

</details>

<details>
<summary><b>Email</b></summary>

给 nanobot 一个独立邮箱账号。它会轮询 **IMAP** 收信，并通过 **SMTP** 回信，像一个邮件助理。

**1. 获取凭据（以 Gmail 为例）**
- 为机器人创建独立 Gmail（例如 `my-nanobot@gmail.com`）
- 开启 2-Step Verification → 创建 [App Password](https://myaccount.google.com/apppasswords)
- 该 app password 同时用于 IMAP 与 SMTP

**2. 配置**

> - `consentGranted` 必须为 `true` 才允许访问邮箱。这是安全闸门；设为 `false` 可完全禁用。
> - `allowFrom`：填写允许发件人的邮箱地址。`["*"]` 表示接受任何人来信。
> - `smtpUseTls` 与 `smtpUseSsl` 默认分别为 `true` / `false`，适配 Gmail（587 + STARTTLS），通常不必显式设置。
> - 若你只想读/分析邮件，不自动回复，请设 `"autoReplyEnabled": false`。

```json
{
  "channels": {
    "email": {
      "enabled": true,
      "consentGranted": true,
      "imapHost": "imap.gmail.com",
      "imapPort": 993,
      "imapUsername": "my-nanobot@gmail.com",
      "imapPassword": "your-app-password",
      "smtpHost": "smtp.gmail.com",
      "smtpPort": 587,
      "smtpUsername": "my-nanobot@gmail.com",
      "smtpPassword": "your-app-password",
      "fromAddress": "my-nanobot@gmail.com",
      "allowFrom": ["your-real-email@gmail.com"]
    }
  }
}
```


**3. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>WeChat (微信 / Weixin)</b></summary>

通过 ilinkai 个人微信 API 进行 **HTTP long-poll** + 扫码登录，不需要本地微信桌面端。

> Weixin 在源码安装中可用，但当前 PyPI 版本尚未包含该功能。

**1. 从源码安装**

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e ".[weixin]"
```

**2. 配置**

```json
{
  "channels": {
    "weixin": {
      "enabled": true,
      "allowFrom": ["YOUR_WECHAT_USER_ID"]
    }
  }
}
```

> - `allowFrom`：填写你在 nanobot 日志里看到的微信发送者 ID。`["*"]` 可允许所有用户。
> - `token`：可选。若不填，可走交互式登录，nanobot 会自动保存 token。
> - `routeTag`：可选。当上游 Weixin 部署要求路由时，nanobot 会作为 `SKRouteTag` 请求头发送。
> - `stateDir`：可选。默认使用 nanobot 的 Weixin 运行时目录。
> - `pollTimeout`：可选，长轮询超时时间（秒）。

**3. 登录**

```bash
nanobot channels login weixin
```

用 `--force` 可强制重新认证，忽略已保存 token：

```bash
nanobot channels login weixin --force
```

**4. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Wecom (企业微信)</b></summary>

> 这里使用 [wecom-aibot-sdk-python](https://github.com/chengyongru/wecom_aibot_sdk)（官方 [@wecom/aibot-node-sdk](https://www.npmjs.com/package/@wecom/aibot-node-sdk) 的社区 Python 版本）。
>
> 使用 **WebSocket** 长连接，无需公网 IP。

**1. 安装可选依赖**

```bash
pip install nanobot-ai[wecom]
```

**2. 创建企业微信 AI Bot**

进入企业微信管理后台 → 智能机器人 → 创建机器人 → 选择 **API 模式** + **长连接**。复制 Bot ID 和 Secret。

**3. 配置**

```json
{
  "channels": {
    "wecom": {
      "enabled": true,
      "botId": "your_bot_id",
      "secret": "your_bot_secret",
      "allowFrom": ["your_id"]
    }
  }
}
```

**4. 运行**

```bash
nanobot gateway
```

</details>

## 🌐 Agent 社交网络

🐈 nanobot 可以连接 Agent 社交网络（Agent 社区）。**只要发一条消息，你的 nanobot 就会自动加入！**

| 平台 | 如何加入（把这条消息发给你的机器人） |
|----------|-------------|
| [**Moltbook**](https://www.moltbook.com/) | `Read https://moltbook.com/skill.md and follow the instructions to join Moltbook` |
| [**ClawdChat**](https://clawdchat.ai/) | `Read https://clawdchat.ai/skill.md and follow the instructions to join ClawdChat` |

把上面的命令发给 nanobot（通过 CLI 或任意聊天渠道），它会自动处理后续。

## ⚙️ 配置

配置文件：`~/.nanobot/config.json`

### 模型提供商（Providers）

> [!TIP]
> - **Groq** 提供免费的 Whisper 语音转写。配置后，Telegram 语音消息会自动转写。
> - **MiniMax Coding Plan**：nanobot 社区专属优惠链接：[海外](https://platform.minimax.io/subscribe/coding-plan?code=9txpdXw04g&source=link) · [中国大陆](https://platform.minimaxi.com/subscribe/token-plan?code=GILTJpMTqZ&source=link)
> - **MiniMax（中国大陆）**：如果 API Key 来自 minimaxi.com，请在 minimax provider 中设置 `"apiBase": "https://api.minimaxi.com/v1"`。
> - **VolcEngine / BytePlus Coding Plan**：请使用专用 provider `volcengineCodingPlan` 或 `byteplusCodingPlan`，不要使用按量计费的 `volcengine` / `byteplus`。
> - **Zhipu Coding Plan**：如果你使用智谱 coding plan，请在 zhipu provider 中设置 `"apiBase": "https://open.bigmodel.cn/api/coding/paas/v4"`。
> - **Alibaba Cloud BaiLian**：如果你使用百炼 OpenAI 兼容端点，请在 dashscope provider 中设置 `"apiBase": "https://dashscope.aliyuncs.com/compatible-mode/v1"`。
> - **Step Fun（中国大陆）**：如果 API Key 来自 stepfun.com，请在 stepfun provider 中设置 `"apiBase": "https://api.stepfun.com/v1"`。
> - **Step Fun Step Plan**：nanobot 社区专属优惠链接：[海外](https://platform.stepfun.ai/step-plan) · [中国大陆](https://platform.stepfun.com/step-plan)

| Provider | 用途 | 获取 API Key |
|----------|---------|-------------|
| `custom` | 任意 OpenAI 兼容端点 | — |
| `openrouter` | LLM（推荐，可访问全模型） | [openrouter.ai](https://openrouter.ai) |
| `volcengine` | LLM（VolcEngine，按量计费） | [Coding Plan](https://www.volcengine.com/activity/codingplan?utm_campaign=nanobot&utm_content=nanobot&utm_medium=devrel&utm_source=OWO&utm_term=nanobot) · [volcengine.com](https://www.volcengine.com) |
| `byteplus` | LLM（VolcEngine 国际版，按量计费） | [Coding Plan](https://www.byteplus.com/en/activity/codingplan?utm_campaign=nanobot&utm_content=nanobot&utm_medium=devrel&utm_source=OWO&utm_term=nanobot) · [byteplus.com](https://www.byteplus.com) |
| `anthropic` | LLM（Claude 官方） | [console.anthropic.com](https://console.anthropic.com) |
| `azure_openai` | LLM（Azure OpenAI） | [portal.azure.com](https://portal.azure.com) |
| `openai` | LLM（GPT 官方） | [platform.openai.com](https://platform.openai.com) |
| `deepseek` | LLM（DeepSeek 官方） | [platform.deepseek.com](https://platform.deepseek.com) |
| `groq` | LLM + **语音转写**（Whisper） | [console.groq.com](https://console.groq.com) |
| `minimax` | LLM（MiniMax 官方） | [platform.minimaxi.com](https://platform.minimaxi.com) |
| `gemini` | LLM（Gemini 官方） | [aistudio.google.com](https://aistudio.google.com) |
| `aihubmix` | LLM（API 网关，可访问全模型） | [aihubmix.com](https://aihubmix.com) |
| `siliconflow` | LLM（SiliconFlow/硅基流动） | [siliconflow.cn](https://siliconflow.cn) |
| `dashscope` | LLM（Qwen） | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) |
| `moonshot` | LLM（Moonshot/Kimi） | [platform.moonshot.cn](https://platform.moonshot.cn) |
| `zhipu` | LLM（智谱 GLM） | [open.bigmodel.cn](https://open.bigmodel.cn) |
| `ollama` | LLM（本地，Ollama） | — |
| `mistral` | LLM | [docs.mistral.ai](https://docs.mistral.ai/) |
| `stepfun` | LLM（Step Fun/阶跃星辰） | [platform.stepfun.com](https://platform.stepfun.com) |
| `ovms` | LLM（本地，OpenVINO Model Server） | [docs.openvino.ai](https://docs.openvino.ai/2026/model-server/ovms_docs_llm_quickstart.html) |
| `vllm` | LLM（本地，任意 OpenAI 兼容服务） | — |
| `openai_codex` | LLM（Codex，OAuth） | `nanobot provider login openai-codex` |
| `github_copilot` | LLM（GitHub Copilot，OAuth） | `nanobot provider login github-copilot` |

<details>
<summary><b>OpenAI Codex (OAuth)</b></summary>

Codex 使用 OAuth，而不是 API Key。需要 ChatGPT Plus 或 Pro 账号。
`config.json` 不需要 `providers.openaiCodex` 配置块；`nanobot provider login` 会把 OAuth 会话存储在配置外。

**1. 登录：**
```bash
nanobot provider login openai-codex
```

**2. 设置模型**（合并到 `~/.nanobot/config.json`）：
```json
{
  "agents": {
    "defaults": {
      "model": "openai-codex/gpt-5.1-codex"
    }
  }
}
```

**3. 开聊：**
```bash
nanobot agent -m "Hello!"

# 本地指定某个 workspace/config
nanobot agent -c ~/.nanobot-telegram/config.json -m "Hello!"

# 在该 config 基础上临时覆盖 workspace
nanobot agent -c ~/.nanobot-telegram/config.json -w /tmp/nanobot-telegram-test -m "Hello!"
```

> Docker 用户：交互式 OAuth 登录请使用 `docker run -it`。

</details>


<details>
<summary><b>GitHub Copilot (OAuth)</b></summary>

GitHub Copilot 使用 OAuth，而不是 API Key。需要配置好套餐的 [GitHub 账号](https://github.com/features/copilot/plans)。
`config.json` 不需要 `providers.githubCopilot` 配置块；`nanobot provider login` 会把 OAuth 会话存储在配置外。

**1. 登录：**
```bash
nanobot provider login github-copilot
```

**2. 设置模型**（合并到 `~/.nanobot/config.json`）：
```json
{
  "agents": {
    "defaults": {
      "model": "github-copilot/gpt-4.1"
    }
  }
}
```

**3. 开聊：**
```bash
nanobot agent -m "Hello!"

# 本地指定某个 workspace/config
nanobot agent -c ~/.nanobot-telegram/config.json -m "Hello!"

# 在该 config 基础上临时覆盖 workspace
nanobot agent -c ~/.nanobot-telegram/config.json -w /tmp/nanobot-telegram-test -m "Hello!"
```

> Docker 用户：交互式 OAuth 登录请使用 `docker run -it`。

</details>

<details>
<summary><b>自定义 Provider（任意 OpenAI 兼容 API）</b></summary>

可直连任何 OpenAI 兼容端点：LM Studio、llama.cpp、Together AI、Fireworks、Azure OpenAI 或任意自托管服务。模型名按原样透传。

```json
{
  "providers": {
    "custom": {
      "apiKey": "your-api-key",
      "apiBase": "https://api.your-provider.com/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "your-model-name"
    }
  }
}
```

> 对于不需要 key 的本地服务，请把 `apiKey` 设为任意非空字符串（例如 `"no-key"`）。

</details>

<details>
<summary><b>Ollama（本地）</b></summary>

使用 Ollama 跑本地模型，然后加入配置：

**1. 启动 Ollama**（示例）：
```bash
ollama run llama3.2
```

**2. 写入配置**（部分配置，合并到 `~/.nanobot/config.json`）：
```json
{
  "providers": {
    "ollama": {
      "apiBase": "http://localhost:11434"
    }
  },
  "agents": {
    "defaults": {
      "provider": "ollama",
      "model": "llama3.2"
    }
  }
}
```

> 当 `providers.ollama.apiBase` 已配置时，`provider: "auto"` 也可工作；但显式设为 `"provider": "ollama"` 更清晰。

</details>

<details>
<summary><b>OpenVINO Model Server（本地 / OpenAI 兼容）</b></summary>

使用 [OpenVINO Model Server](https://docs.openvino.ai/2026/model-server/ovms_docs_llm_quickstart.html) 在 Intel GPU 上本地运行 LLM。OVMS 在 `/v3` 暴露 OpenAI 兼容 API。

> 需要 Docker 和带驱动访问（`/dev/dri`）的 Intel GPU。

**1. 拉取模型**（示例）：

```bash
mkdir -p ov/models && cd ov

docker run -d \
  --rm \
  --user $(id -u):$(id -g) \
  -v $(pwd)/models:/models \
  openvino/model_server:latest-gpu \
  --pull \
  --model_name openai/gpt-oss-20b \
  --model_repository_path /models \
  --source_model OpenVINO/gpt-oss-20b-int4-ov \
  --task text_generation \
  --tool_parser gptoss \
  --reasoning_parser gptoss \
  --enable_prefix_caching true \
  --target_device GPU
```

> 这一步会下载模型权重。请等待容器执行完成后再继续。

**2. 启动服务**（示例）：

```bash
docker run -d \
  --rm \
  --name ovms \
  --user $(id -u):$(id -g) \
  -p 8000:8000 \
  -v $(pwd)/models:/models \
  --device /dev/dri \
  --group-add=$(stat -c "%g" /dev/dri/render* | head -n 1) \
  openvino/model_server:latest-gpu \
  --rest_port 8000 \
  --model_name openai/gpt-oss-20b \
  --model_repository_path /models \
  --source_model OpenVINO/gpt-oss-20b-int4-ov \
  --task text_generation \
  --tool_parser gptoss \
  --reasoning_parser gptoss \
  --enable_prefix_caching true \
  --target_device GPU
```

**3. 写入配置**（部分配置，合并到 `~/.nanobot/config.json`）：

```json
{
  "providers": {
    "ovms": {
      "apiBase": "http://localhost:8000/v3"
    }
  },
  "agents": {
    "defaults": {
      "provider": "ovms",
      "model": "openai/gpt-oss-20b"
    }
  }
}
```

> OVMS 是本地服务，不需要 API Key。支持工具调用（`--tool_parser gptoss`）、推理（`--reasoning_parser gptoss`）和流式输出。
> 更多细节见 [官方 OVMS 文档](https://docs.openvino.ai/2026/model-server/ovms_docs_llm_quickstart.html)。
</details>

<details>
<summary><b>vLLM（本地 / OpenAI 兼容）</b></summary>

使用 vLLM 或其他 OpenAI 兼容服务运行你自己的模型，然后加入配置：

**1. 启动服务**（示例）：
```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

**2. 写入配置**（部分配置，合并到 `~/.nanobot/config.json`）：

*Provider（本地服务可用任意非空字符串作为 key）：*
```json
{
  "providers": {
    "vllm": {
      "apiKey": "dummy",
      "apiBase": "http://localhost:8000/v1"
    }
  }
}
```

*模型：*
```json
{
  "agents": {
    "defaults": {
      "model": "meta-llama/Llama-3.1-8B-Instruct"
    }
  }
}
```

</details>

<details>
<summary><b>新增 Provider（开发者指南）</b></summary>

nanobot 使用 **Provider Registry**（`nanobot/providers/registry.py`）作为唯一事实来源。
新增一个 provider 只需 **2 步**，无需修改 if-elif 链。

**步骤 1：** 在 `nanobot/providers/registry.py` 的 `PROVIDERS` 中添加一个 `ProviderSpec`：

```python
ProviderSpec(
    name="myprovider",                   # 配置字段名
    keywords=("myprovider", "mymodel"),  # 模型名关键词（自动匹配）
    env_key="MYPROVIDER_API_KEY",        # 环境变量名
    display_name="My Provider",          # 在 `nanobot status` 中显示
    default_api_base="https://api.myprovider.com/v1",  # OpenAI 兼容端点
)
```

**步骤 2：** 在 `nanobot/config/schema.py` 的 `ProvidersConfig` 中增加字段：

```python
class ProvidersConfig(BaseModel):
    ...
    myprovider: ProviderConfig = ProviderConfig()
```

完成。环境变量、模型路由、配置匹配和 `nanobot status` 展示都会自动生效。

**常用 `ProviderSpec` 选项：**

| 字段 | 说明 | 示例 |
|-------|-------------|---------|
| `default_api_base` | OpenAI 兼容 base URL | `"https://api.deepseek.com"` |
| `env_extras` | 需要额外设置的环境变量 | `(("ZHIPUAI_API_KEY", "{api_key}"),)` |
| `model_overrides` | 按模型覆盖参数 | `(("kimi-k2.5", {"temperature": 1.0}),)` |
| `is_gateway` | 是否可路由任意模型（类似 OpenRouter） | `True` |
| `detect_by_key_prefix` | 按 API key 前缀识别网关 | `"sk-or-"` |
| `detect_by_base_keyword` | 按 API base URL 关键词识别网关 | `"openrouter"` |
| `strip_model_prefix` | 发送到网关前去掉 provider 前缀 | `True`（AiHubMix） |
| `supports_max_completion_tokens` | 使用 `max_completion_tokens` 代替 `max_tokens`；适用于拒绝同时设置两者的 provider（如 VolcEngine） | `True` |

</details>

### 渠道通用设置

适用于所有渠道的全局设置。请在 `~/.nanobot/config.json` 的 `channels` 下配置：

```json
{
  "channels": {
    "sendProgress": true,
    "sendToolHints": false,
    "sendMaxRetries": 3,
    "telegram": { ... }
  }
}
```

| 设置项 | 默认值 | 说明 |
|---------|---------|-------------|
| `sendProgress` | `true` | 把 agent 的文本进度流式发送到渠道 |
| `sendToolHints` | `false` | 流式发送工具调用提示（如 `read_file("…")`） |
| `sendMaxRetries` | `3` | 每条外发消息最大投递次数（含首次发送；配置范围 0-10，实际最少 1 次） |

#### 重试机制

当渠道发送发生错误时，nanobot 使用指数退避重试：

- **第 1 次**：首次发送
- **第 2-4 次**：重试间隔分别为 1s、2s、4s
- **第 5 次及以后**：重试间隔封顶为 4s
- **瞬时故障**（网络抖动、临时限流）：通常重试可恢复
- **永久故障**（token 无效、渠道封禁）：所有重试都会失败

> [!NOTE]
> 当某个渠道完全不可达时，我们无法通过该渠道通知用户。请监控日志中的 “Failed to send to {channel} after N attempts” 以识别持续投递失败。

### 网络搜索

> [!TIP]
> 在 `tools.web` 里设置 `proxy`，可将所有 web 请求（搜索 + 抓取）走代理：
> ```json
> { "tools": { "web": { "proxy": "http://127.0.0.1:7890" } } }
> ```

nanobot 支持多种 web 搜索 provider。配置路径：`~/.nanobot/config.json` 的 `tools.web.search`。

| Provider | 配置字段 | 环境变量回退 | 免费 |
|----------|--------------|------------------|------|
| `brave`（默认） | `apiKey` | `BRAVE_API_KEY` | 否 |
| `tavily` | `apiKey` | `TAVILY_API_KEY` | 否 |
| `jina` | `apiKey` | `JINA_API_KEY` | 免费额度（10M tokens） |
| `searxng` | `baseUrl` | `SEARXNG_BASE_URL` | 是（自托管） |
| `duckduckgo` | — | — | 是 |

当缺少凭据时，nanobot 会自动回退到 DuckDuckGo。

**Brave**（默认）：
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "brave",
        "apiKey": "BSA..."
      }
    }
  }
}
```

**Tavily：**
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "tavily",
        "apiKey": "tvly-..."
      }
    }
  }
}
```

**Jina**（免费额度 10M tokens）：
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "jina",
        "apiKey": "jina_..."
      }
    }
  }
}
```

**SearXNG**（自托管，无需 API key）：
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "searxng",
        "baseUrl": "https://searx.example"
      }
    }
  }
}
```

**DuckDuckGo**（零配置）：
```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "duckduckgo"
      }
    }
  }
}
```

| 选项 | 类型 | 默认值 | 说明 |
|--------|------|---------|-------------|
| `provider` | string | `"brave"` | 搜索后端：`brave`、`tavily`、`jina`、`searxng`、`duckduckgo` |
| `apiKey` | string | `""` | Brave 或 Tavily 的 API key |
| `baseUrl` | string | `""` | SearXNG 的 base URL |
| `maxResults` | integer | `5` | 每次搜索返回数量（1–10） |

### MCP（Model Context Protocol）

> [!TIP]
> 该配置格式兼容 Claude Desktop / Cursor。你可以把任意 MCP 服务 README 里的配置直接复制过来。

nanobot 支持 [MCP](https://modelcontextprotocol.io/) —— 可接入外部工具服务，并把它们当作原生工具使用。

在你的 `config.json` 中添加 MCP 服务：

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
      },
      "my-remote-mcp": {
        "url": "https://example.com/mcp/",
        "headers": {
          "Authorization": "Bearer xxxxx"
        }
      }
    }
  }
}
```

支持两种传输模式：

| 模式 | 配置 | 示例 |
|------|--------|---------|
| **Stdio** | `command` + `args` | 通过 `npx` / `uvx` 启动本地进程 |
| **HTTP** | `url` + `headers`（可选） | 远端端点（`https://mcp.example.com/sse`） |

对较慢服务，可用 `toolTimeout` 覆盖默认单次调用 30s 超时：

```json
{
  "tools": {
    "mcpServers": {
      "my-slow-server": {
        "url": "https://example.com/mcp/",
        "toolTimeout": 120
      }
    }
  }
}
```

使用 `enabledTools` 仅注册某个 MCP 服务中的部分工具：

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
        "enabledTools": ["read_file", "mcp_filesystem_write_file"]
      }
    }
  }
}
```

`enabledTools` 可写原始 MCP 工具名（如 `read_file`），也可写 nanobot 包装后的工具名（如 `mcp_filesystem_write_file`）。

- 省略 `enabledTools`，或设为 `["*"]`，表示注册全部工具。
- 设为 `[]`，表示该服务不注册任何工具。
- 设为非空列表，表示仅注册名单内工具。

MCP 工具会在启动时自动发现并注册。LLM 可与内置工具一起调用，无需额外配置。




### 安全

> [!TIP]
> 生产环境建议在配置中设置 `"restrictToWorkspace": true`，将 agent 限制在工作目录内。
> 在 `v0.1.4.post3` 及更早版本中，空 `allowFrom` 表示允许全部发送者；从 `v0.1.4.post4` 起，空 `allowFrom` 默认拒绝全部访问。若需允许所有发送者，请显式设置 `"allowFrom": ["*"]`。

| 选项 | 默认值 | 说明 |
|--------|---------|-------------|
| `tools.restrictToWorkspace` | `false` | 为 `true` 时，将**所有** agent 工具（shell、文件读写/编辑、list）限制在 workspace 目录内，防止路径穿越和越界访问。 |
| `tools.exec.enable` | `true` | 为 `false` 时，不注册 shell `exec` 工具，可彻底禁用命令执行。 |
| `tools.exec.pathAppend` | `""` | 执行 shell 命令时追加到 `PATH` 的目录（如 `ufw` 可能需要 `/usr/sbin`）。 |
| `channels.*.allowFrom` | `[]`（拒绝全部） | 用户 ID 白名单。空数组拒绝全部；`["*"]` 允许所有。 |


### 时区

时间是上下文。上下文应当精确。

默认情况下，nanobot 使用 `UTC` 作为运行时时间上下文。若希望 agent 按你的本地时间思考，请设置 `agents.defaults.timezone` 为合法的 [IANA 时区名](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)：

```json
{
  "agents": {
    "defaults": {
      "timezone": "Asia/Shanghai"
    }
  }
}
```

这会影响传给模型的运行时时间字符串（例如 runtime context 与 heartbeat prompts）。当 cron 表达式未显式提供 `tz` 时，也会作为默认时区；同样地，当一次性 `at` 时间的 ISO datetime 没有显式 offset 时，也使用该时区。

常见示例：`UTC`、`America/New_York`、`America/Los_Angeles`、`Europe/London`、`Europe/Berlin`、`Asia/Tokyo`、`Asia/Shanghai`、`Asia/Singapore`、`Australia/Sydney`。

> 需要其他时区？查看完整 [IANA 时区数据库](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)。

## 🧩 多实例

你可以同时运行多个 nanobot 实例，每个实例使用独立配置与运行时数据。主入口是 `--config`。当你想为特定实例初始化或更新已保存 workspace 时，可在 `onboard` 时额外传 `--workspace`。

### 快速开始

如果你希望每个实例一开始就使用独立 workspace，请在 onboarding 时同时传 `--config` 与 `--workspace`。

**初始化实例：**

```bash
# 创建独立实例配置与工作目录
nanobot onboard --config ~/.nanobot-telegram/config.json --workspace ~/.nanobot-telegram/workspace
nanobot onboard --config ~/.nanobot-discord/config.json --workspace ~/.nanobot-discord/workspace
nanobot onboard --config ~/.nanobot-feishu/config.json --workspace ~/.nanobot-feishu/workspace
```

**配置各实例：**

分别编辑 `~/.nanobot-telegram/config.json`、`~/.nanobot-discord/config.json` 等，写入不同渠道配置。你在 `onboard` 传入的 workspace 会保存为该实例默认 workspace。

**运行实例：**

```bash
# 实例 A - Telegram bot
nanobot gateway --config ~/.nanobot-telegram/config.json

# 实例 B - Discord bot  
nanobot gateway --config ~/.nanobot-discord/config.json

# 实例 C - Feishu bot（自定义端口）
nanobot gateway --config ~/.nanobot-feishu/config.json --port 18792
```

### 路径解析

使用 `--config` 时，nanobot 会基于配置文件位置推导运行时数据目录。workspace 仍来自 `agents.defaults.workspace`，除非你用 `--workspace` 覆盖。

如果你想在本地 CLI 会话中操作某个实例：

```bash
nanobot agent -c ~/.nanobot-telegram/config.json -m "Hello from Telegram instance"
nanobot agent -c ~/.nanobot-discord/config.json -m "Hello from Discord instance"

# 可选：临时覆盖 workspace
nanobot agent -c ~/.nanobot-telegram/config.json -w /tmp/nanobot-telegram-test
```

> `nanobot agent` 启动的是本地 CLI agent，会使用所选 workspace/config。它不会附着或代理到已在运行的 `nanobot gateway` 进程。

| 组件 | 来源 | 示例 |
|-----------|---------------|---------|
| **Config** | `--config` 路径 | `~/.nanobot-A/config.json` |
| **Workspace** | `--workspace` 或配置文件 | `~/.nanobot-A/workspace/` |
| **Cron Jobs** | 配置目录 | `~/.nanobot-A/cron/` |
| **Media / runtime state** | 配置目录 | `~/.nanobot-A/media/` |

### 工作机制

- `--config` 决定加载哪个配置文件
- 默认 workspace 来自该配置中的 `agents.defaults.workspace`
- 若传入 `--workspace`，会覆盖配置中的 workspace

### 最小化配置

1. 复制基础配置到新的实例目录。
2. 为该实例设置不同的 `agents.defaults.workspace`。
3. 使用 `--config` 启动该实例。

示例配置：

```json
{
  "agents": {
    "defaults": {
      "workspace": "~/.nanobot-telegram/workspace",
      "model": "anthropic/claude-sonnet-4-6"
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_TELEGRAM_BOT_TOKEN"
    }
  },
  "gateway": {
    "port": 18790
  }
}
```

启动独立实例：

```bash
nanobot gateway --config ~/.nanobot-telegram/config.json
nanobot gateway --config ~/.nanobot-discord/config.json
```

按需在单次运行中覆盖 workspace：

```bash
nanobot gateway --config ~/.nanobot-telegram/config.json --workspace /tmp/nanobot-telegram-test
```

### 常见使用场景

- 为 Telegram、Discord、Feishu 等平台分别运行独立机器人
- 隔离测试环境与生产环境
- 不同团队使用不同模型或 provider
- 用独立配置与运行时数据服务多租户

### 说明

- 多实例同时运行时必须使用不同端口
- 若希望记忆、会话、技能彼此隔离，请为每个实例使用不同 workspace
- `--workspace` 会覆盖配置文件中的 workspace
- Cron 与媒体/状态目录由配置目录推导

## 💻 CLI 参考

| 命令 | 说明 |
|---------|-------------|
| `nanobot onboard` | 在 `~/.nanobot/` 初始化配置与 workspace |
| `nanobot onboard --wizard` | 启动交互式初始化向导 |
| `nanobot onboard -c <config> -w <workspace>` | 初始化或刷新指定实例的配置与 workspace |
| `nanobot agent -m "..."` | 与 agent 对话 |
| `nanobot agent -w <workspace>` | 在指定 workspace 下对话 |
| `nanobot agent -w <workspace> -c <config>` | 在指定 workspace/config 下对话 |
| `nanobot agent` | 交互式聊天模式 |
| `nanobot agent --no-markdown` | 以纯文本显示回复 |
| `nanobot agent --logs` | 对话时显示运行日志 |
| `nanobot gateway` | 启动网关 |
| `nanobot status` | 查看状态 |
| `nanobot provider login openai-codex` | provider 的 OAuth 登录 |
| `nanobot channels login <channel>` | 交互式鉴权某渠道 |
| `nanobot channels status` | 查看渠道状态 |

交互模式退出方式：`exit`、`quit`、`/exit`、`/quit`、`:q` 或 `Ctrl+D`。

<details>
<summary><b>Heartbeat（周期任务）</b></summary>

网关每 30 分钟唤醒一次，并检查你的 workspace（`~/.nanobot/workspace/`）中的 `HEARTBEAT.md`。如果文件里有任务，agent 会执行并把结果发送到你最近活跃的聊天渠道。

**配置方式：** 编辑 `~/.nanobot/workspace/HEARTBEAT.md`（`nanobot onboard` 会自动创建）：

```markdown
## Periodic Tasks

- [ ] Check weather forecast and send a summary
- [ ] Scan inbox for urgent emails
```

agent 也可以自行维护这个文件。你只要让它“add a periodic task”，它就会帮你更新 `HEARTBEAT.md`。

> **注意：** 网关必须在运行（`nanobot gateway`），且你至少与机器人聊过一次，它才能知道把结果发送到哪个渠道。

</details>

## 🐳 Docker

> [!TIP]
> `-v ~/.nanobot:/root/.nanobot` 会把你本地配置目录挂载进容器，因此配置和 workspace 在容器重启后仍会保留。

### Docker Compose

```bash
docker compose run --rm nanobot-cli onboard   # 首次初始化
vim ~/.nanobot/config.json                     # 添加 API keys
docker compose up -d nanobot-gateway           # 启动网关
```

```bash
docker compose run --rm nanobot-cli agent -m "Hello!"   # 运行 CLI
docker compose logs -f nanobot-gateway                   # 查看日志
docker compose down                                      # 停止
```

### Docker

```bash
# 构建镜像
docker build -t nanobot .

# 初始化配置（仅首次）
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot onboard

# 在宿主机编辑配置，添加 API keys
vim ~/.nanobot/config.json

# 运行网关（连接已启用渠道，如 Telegram/Discord/Mochat）
docker run -v ~/.nanobot:/root/.nanobot -p 18790:18790 nanobot gateway

# 或执行单条命令
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot agent -m "Hello!"
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot status
```

## 🐧 Linux 服务

把网关作为 systemd 用户服务运行，以实现开机自启和故障自动重启。

**1. 查找 nanobot 可执行路径：**

```bash
which nanobot   # 例如 /home/user/.local/bin/nanobot
```

**2. 创建服务文件** `~/.config/systemd/user/nanobot-gateway.service`（必要时替换 `ExecStart` 路径）：

```ini
[Unit]
Description=Nanobot Gateway
After=network.target

[Service]
Type=simple
ExecStart=%h/.local/bin/nanobot gateway
Restart=always
RestartSec=10
NoNewPrivileges=yes
ProtectSystem=strict
ReadWritePaths=%h

[Install]
WantedBy=default.target
```

**3. 启用并启动：**

```bash
systemctl --user daemon-reload
systemctl --user enable --now nanobot-gateway
```

**常用操作：**

```bash
systemctl --user status nanobot-gateway        # 查看状态
systemctl --user restart nanobot-gateway       # 配置变更后重启
journalctl --user -u nanobot-gateway -f        # 实时查看日志
```

如果你修改了 `.service` 文件本身，重启前请先执行 `systemctl --user daemon-reload`。

> **注意：** 用户服务仅在登录状态下运行。若希望退出登录后仍持续运行，请启用 lingering：
>
> ```bash
> loginctl enable-linger $USER
> ```

## 📁 项目结构

```
nanobot/
├── agent/          # 🧠 核心 agent 逻辑
│   ├── loop.py     #    Agent 循环（LLM ↔ 工具执行）
│   ├── context.py  #    Prompt 构建
│   ├── memory.py   #    持久化记忆
│   ├── skills.py   #    Skills 加载
│   ├── subagent.py #    后台任务执行
│   └── tools/      #    内置工具（含 spawn）
├── skills/         # 🎯 内置技能（github、weather、tmux...）
├── channels/       # 📱 聊天渠道集成（支持插件）
├── bus/            # 🚌 消息路由
├── cron/           # ⏰ 定时任务
├── heartbeat/      # 💓 主动唤醒
├── providers/      # 🤖 LLM providers（OpenRouter 等）
├── session/        # 💬 对话会话
├── config/         # ⚙️ 配置
└── cli/            # 🖥️ 命令行入口
```

## 🤝 贡献与路线图

欢迎 PR！代码库刻意保持小而可读。🤗

### 分支策略

| 分支 | 用途 |
|--------|---------|
| `main` | 稳定发布：bug 修复与小幅改进 |
| `nightly` | 实验特性：新功能和破坏性变更 |

**不确定该往哪个分支提？** 见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

**路线图** —— 认领一项并[提交 PR](https://github.com/HKUDS/nanobot/pulls)！

- [ ] **多模态** —— 看见与听见（图像、语音、视频）
- [ ] **长期记忆** —— 不遗忘关键上下文
- [ ] **更强推理** —— 多步规划与反思
- [ ] **更多集成** —— 日历等能力
- [ ] **自我改进** —— 从反馈与错误中学习

### 贡献者

<a href="https://github.com/HKUDS/nanobot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/nanobot&max=100&columns=12&updated=20260210" alt="Contributors" />
</a>


## ⭐ Star 历史

<div align="center">
  <a href="https://star-history.com/#HKUDS/nanobot&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" style="border-radius: 15px; box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);" />
    </picture>
  </a>
</div>

<p align="center">
  <em> 感谢访问 ✨ nanobot！</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.nanobot&style=for-the-badge&color=00d4ff" alt="Views">
</p>


<p align="center">
  <sub>nanobot 仅用于教育、科研与技术交流</sub>
</p>
