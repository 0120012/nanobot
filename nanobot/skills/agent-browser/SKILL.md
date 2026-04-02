---
name: agent-browser
description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction.
allowed-tools: Bash(npx agent-browser:*), Bash(agent-browser:*)
---

# Browser Automation with agent-browser
# 使用 agent-browser 进行浏览器自动化

The CLI uses Chrome/Chromium via CDP directly. Install via `npm i -g agent-browser`, `brew install agent-browser`, or `cargo install agent-browser`. Run `agent-browser install` to download Chrome. Run `agent-browser upgrade` to update to the latest version.
该 CLI 通过 CDP 直接控制 Chrome/Chromium。可使用 `npm i -g agent-browser`、`brew install agent-browser` 或 `cargo install agent-browser` 安装。运行 `agent-browser install` 下载 Chrome，运行 `agent-browser upgrade` 升级到最新版本。

## Core Workflow
## 核心工作流

Every browser automation follows this pattern:
所有浏览器自动化都遵循这个模式：

1. **Navigate**: `agent-browser open <url>`
1. **导航**：`agent-browser open <url>`
2. **Snapshot**: `agent-browser snapshot -i` (get element refs like `@e1`, `@e2`)
2. **快照**：`agent-browser snapshot -i`（获取元素引用，如 `@e1`、`@e2`）
3. **Interact**: Use refs to click, fill, select
3. **交互**：使用引用执行点击、输入、选择
4. **Re-snapshot**: After navigation or DOM changes, get fresh refs
4. **重新快照**：在导航或 DOM 变化后重新获取最新引用

```bash
agent-browser open https://example.com/form
agent-browser snapshot -i
# Output: @e1 [input type="email"], @e2 [input type="password"], @e3 [button] "Submit"

agent-browser fill @e1 "user@example.com"
agent-browser fill @e2 "password123"
agent-browser click @e3
agent-browser wait --load networkidle
agent-browser snapshot -i  # Check result
```

## Command Chaining
## 命令链式执行

Commands can be chained with `&&` in a single shell invocation. The browser persists between commands via a background daemon, so chaining is safe and more efficient than separate calls.
可以在一次 shell 调用中用 `&&` 串联命令。浏览器会通过后台守护进程在命令之间保持状态，因此链式执行既安全又比拆分调用更高效。

```bash
# Chain open + wait + snapshot in one call
agent-browser open https://example.com && agent-browser wait --load networkidle && agent-browser snapshot -i

# Chain multiple interactions
agent-browser fill @e1 "user@example.com" && agent-browser fill @e2 "password123" && agent-browser click @e3

# Navigate and capture
agent-browser open https://example.com && agent-browser wait --load networkidle && agent-browser screenshot page.png
```

**When to chain:** Use `&&` when you don't need to read the output of an intermediate command before proceeding (e.g., open + wait + screenshot). Run commands separately when you need to parse the output first (e.g., snapshot to discover refs, then interact using those refs).
**何时链式执行：** 当你不需要读取中间命令输出时使用 `&&`（例如 open + wait + screenshot）。如果要先解析输出再继续（例如先 snapshot 获取 refs，再基于 refs 交互），请拆开执行。

## Handling Authentication
## 身份认证处理

When automating a site that requires login, choose the approach that fits:
当自动化需要登录的网站时，选择最匹配的方式：

**Option 1: Import auth from the user's browser (fastest for one-off tasks)**
**方案 1：从用户浏览器导入认证状态（一次性任务最快）**

```bash
# Connect to the user's running Chrome (they're already logged in)
agent-browser --auto-connect state save ./auth.json
# Use that auth state
agent-browser --state ./auth.json open https://app.example.com/dashboard
```

State files contain session tokens in plaintext -- add to `.gitignore` and delete when no longer needed. Set `AGENT_BROWSER_ENCRYPTION_KEY` for encryption at rest.
状态文件包含明文会话令牌，必须加入 `.gitignore`，并在不再需要时删除。可设置 `AGENT_BROWSER_ENCRYPTION_KEY` 启用静态加密。

**Option 2: Persistent profile (simplest for recurring tasks)**
**方案 2：持久化 profile（重复任务最简单）**

```bash
# First run: login manually or via automation
agent-browser --profile ~/.myapp open https://app.example.com/login
# ... fill credentials, submit ...

# All future runs: already authenticated
agent-browser --profile ~/.myapp open https://app.example.com/dashboard
```

**Option 3: Session name (auto-save/restore cookies + localStorage)**
**方案 3：会话名（自动保存/恢复 cookies + localStorage）**

```bash
agent-browser --session-name myapp open https://app.example.com/login
#  ... login flow ...
agent-browser close  # State auto-saved

# Next time: state auto-restored
agent-browser --session-name myapp open https://app.example.com/dashboard
```

**Option 4: Auth vault (credentials stored encrypted, login by name)**
**方案 4：认证金库（凭据加密存储，按名称登录）**

```bash
echo "$PASSWORD" | agent-browser auth save myapp --url https://app.example.com/login --username user --password-stdin
agent-browser auth login myapp
```

`auth login` navigates with `load` and then waits for login form selectors to appear before filling/clicking, which is more reliable on delayed SPA login screens.
`auth login` 会先以 `load` 导航，再等待登录表单选择器出现后执行填充/点击；对延迟渲染的 SPA 登录页更可靠。

**Option 5: State file (manual save/load)**
**方案 5：状态文件（手动保存/加载）**

```bash
# After logging in:
agent-browser state save ./auth.json
# In a future session:
agent-browser state load ./auth.json
agent-browser open https://app.example.com/dashboard
```

See [references/authentication.md](references/authentication.md) for OAuth, 2FA, cookie-based auth, and token refresh patterns.
关于 OAuth、2FA、基于 Cookie 的认证和令牌刷新模式，参见 [references/authentication.md](references/authentication.md)。

## Essential Commands
## 常用命令

```bash
# Navigation
agent-browser open <url>              # Navigate (aliases: goto, navigate)
agent-browser close                   # Close browser

# Snapshot
agent-browser snapshot -i             # Interactive elements with refs (recommended)
agent-browser snapshot -s "#selector" # Scope to CSS selector

# Interaction (use @refs from snapshot)
agent-browser click @e1               # Click element
agent-browser click @e1 --new-tab     # Click and open in new tab
agent-browser fill @e2 "text"         # Clear and type text
agent-browser type @e2 "text"         # Type without clearing
agent-browser select @e1 "option"     # Select dropdown option
agent-browser check @e1               # Check checkbox
agent-browser press Enter             # Press key
agent-browser keyboard type "text"    # Type at current focus (no selector)
agent-browser keyboard inserttext "text"  # Insert without key events
agent-browser scroll down 500         # Scroll page
agent-browser scroll down 500 --selector "div.content"  # Scroll within a specific container

# Get information
agent-browser get text @e1            # Get element text
agent-browser get url                 # Get current URL
agent-browser get title               # Get page title
agent-browser get cdp-url             # Get CDP WebSocket URL

# Wait
agent-browser wait @e1                # Wait for element
agent-browser wait --load networkidle # Wait for network idle
agent-browser wait --url "**/page"    # Wait for URL pattern
agent-browser wait 2000               # Wait milliseconds
agent-browser wait --text "Welcome"    # Wait for text to appear (substring match)
agent-browser wait --fn "!document.body.innerText.includes('Loading...')"  # Wait for text to disappear
agent-browser wait "#spinner" --state hidden  # Wait for element to disappear

# Downloads
agent-browser download @e1 ./file.pdf          # Click element to trigger download
agent-browser wait --download ./output.zip     # Wait for any download to complete
agent-browser --download-path ./downloads open <url>  # Set default download directory

# Network
agent-browser network requests                 # Inspect tracked requests
agent-browser network requests --type xhr,fetch  # Filter by resource type
agent-browser network requests --method POST   # Filter by HTTP method
agent-browser network requests --status 2xx    # Filter by status (200, 2xx, 400-499)
agent-browser network request <requestId>      # View full request/response detail
agent-browser network route "**/api/*" --abort  # Block matching requests
agent-browser network har start                # Start HAR recording
agent-browser network har stop ./capture.har   # Stop and save HAR file

# Viewport & Device Emulation
agent-browser set viewport 1920 1080          # Set viewport size (default: 1280x720)
agent-browser set viewport 1920 1080 2        # 2x retina (same CSS size, higher res screenshots)
agent-browser set device "iPhone 14"          # Emulate device (viewport + user agent)

# Capture
agent-browser screenshot              # Screenshot to temp dir
agent-browser screenshot --full       # Full page screenshot
agent-browser screenshot --annotate   # Annotated screenshot with numbered element labels
agent-browser screenshot --screenshot-dir ./shots  # Save to custom directory
agent-browser screenshot --screenshot-format jpeg --screenshot-quality 80
agent-browser pdf output.pdf          # Save as PDF

# Live preview / streaming
agent-browser stream enable           # Start runtime WebSocket streaming on an auto-selected port
agent-browser stream enable --port 9223  # Bind a specific localhost port
agent-browser stream status           # Inspect enabled state, port, connection, and screencasting
agent-browser stream disable          # Stop runtime streaming and remove the .stream metadata file

# Clipboard
agent-browser clipboard read                      # Read text from clipboard
agent-browser clipboard write "Hello, World!"     # Write text to clipboard
agent-browser clipboard copy                      # Copy current selection
agent-browser clipboard paste                     # Paste from clipboard

# Dialogs (alert, confirm, prompt)
agent-browser dialog accept              # Accept dialog
agent-browser dialog accept "my input"   # Accept prompt dialog with text
agent-browser dialog dismiss             # Dismiss/cancel dialog
agent-browser dialog status              # Check if a dialog is currently open

# Diff (compare page states)
agent-browser diff snapshot                          # Compare current vs last snapshot
agent-browser diff snapshot --baseline before.txt    # Compare current vs saved file
agent-browser diff screenshot --baseline before.png  # Visual pixel diff
agent-browser diff url <url1> <url2>                 # Compare two pages
agent-browser diff url <url1> <url2> --wait-until networkidle  # Custom wait strategy
agent-browser diff url <url1> <url2> --selector "#main"  # Scope to element
```

## Runtime Streaming
## 运行时流式预览

Use `agent-browser stream enable` when you need a live WebSocket preview for an already-running session. This is the preferred runtime path because it does not require restarting the daemon. `stream enable` creates the server, `stream status` reports the bound port and connection state, and `stream disable` tears it down cleanly.
当你需要为已运行会话提供实时 WebSocket 预览时，使用 `agent-browser stream enable`。这是首选运行时方案，因为无需重启守护进程。`stream enable` 负责启动服务，`stream status` 报告端口与连接状态，`stream disable` 负责干净关闭。

If streaming must be present from the first daemon command, `AGENT_BROWSER_STREAM_PORT` still works at daemon startup, but that environment variable is not retroactive for sessions that are already running.
如果要求从守护进程第一条命令开始就启用流式能力，仍可在启动时使用 `AGENT_BROWSER_STREAM_PORT`；但该环境变量不会追溯应用到已经运行的会话。

## Batch Execution
## 批量执行

Execute multiple commands in a single invocation by piping a JSON array of string arrays to `batch`. This avoids per-command process startup overhead when running multi-step workflows.
将“字符串数组的 JSON 数组”通过管道传给 `batch`，即可一次调用执行多条命令。这样可避免多步骤工作流中每条命令重复启动进程的开销。

```bash
echo '[
  ["open", "https://example.com"],
  ["snapshot", "-i"],
  ["click", "@e1"],
  ["screenshot", "result.png"]
]' | agent-browser batch --json

# Stop on first error
agent-browser batch --bail < commands.json
```

Use `batch` when you have a known sequence of commands that don't depend on intermediate output. Use separate commands or `&&` chaining when you need to parse output between steps (e.g., snapshot to discover refs, then interact).
当命令序列已知且不依赖中间输出时，使用 `batch`。若步骤之间需要先解析输出（例如先 snapshot 获取 refs 再交互），请使用拆分命令或 `&&` 链式方式。

## Common Patterns
## 常见模式

### Form Submission
### 表单提交

```bash
agent-browser open https://example.com/signup
agent-browser snapshot -i
agent-browser fill @e1 "Jane Doe"
agent-browser fill @e2 "jane@example.com"
agent-browser select @e3 "California"
agent-browser check @e4
agent-browser click @e5
agent-browser wait --load networkidle
```

### Authentication with Auth Vault (Recommended)
### 使用认证金库进行登录（推荐）

```bash
# Save credentials once (encrypted with AGENT_BROWSER_ENCRYPTION_KEY)
# Recommended: pipe password via stdin to avoid shell history exposure
echo "pass" | agent-browser auth save github --url https://github.com/login --username user --password-stdin

# Login using saved profile (LLM never sees password)
agent-browser auth login github

# List/show/delete profiles
agent-browser auth list
agent-browser auth show github
agent-browser auth delete github
```

`auth login` waits for username/password/submit selectors before interacting, with a timeout tied to the default action timeout.
`auth login` 会先等待用户名/密码/提交按钮选择器出现再交互，超时沿用默认动作超时设置。

### Authentication with State Persistence
### 使用状态持久化进行登录

```bash
# Login once and save state
agent-browser open https://app.example.com/login
agent-browser snapshot -i
agent-browser fill @e1 "$USERNAME"
agent-browser fill @e2 "$PASSWORD"
agent-browser click @e3
agent-browser wait --url "**/dashboard"
agent-browser state save auth.json

# Reuse in future sessions
agent-browser state load auth.json
agent-browser open https://app.example.com/dashboard
```

### Session Persistence
### 会话持久化

```bash
# Auto-save/restore cookies and localStorage across browser restarts
agent-browser --session-name myapp open https://app.example.com/login
# ... login flow ...
agent-browser close  # State auto-saved to ~/.agent-browser/sessions/

# Next time, state is auto-loaded
agent-browser --session-name myapp open https://app.example.com/dashboard

# Encrypt state at rest
export AGENT_BROWSER_ENCRYPTION_KEY=$(openssl rand -hex 32)
agent-browser --session-name secure open https://app.example.com

# Manage saved states
agent-browser state list
agent-browser state show myapp-default.json
agent-browser state clear myapp
agent-browser state clean --older-than 7
```

### Working with Iframes
### Iframe 场景

Iframe content is automatically inlined in snapshots. Refs inside iframes carry frame context, so you can interact with them directly.
Iframe 内容会自动内联到快照中。iframe 内部 refs 会携带 frame 上下文，因此可以直接交互。

```bash
agent-browser open https://example.com/checkout
agent-browser snapshot -i
# @e1 [heading] "Checkout"
# @e2 [Iframe] "payment-frame"
#   @e3 [input] "Card number"
#   @e4 [input] "Expiry"
#   @e5 [button] "Pay"

# Interact directly — no frame switch needed
agent-browser fill @e3 "4111111111111111"
agent-browser fill @e4 "12/28"
agent-browser click @e5

# To scope a snapshot to one iframe:
agent-browser frame @e2
agent-browser snapshot -i         # Only iframe content
agent-browser frame main          # Return to main frame
```

### Data Extraction
### 数据提取

```bash
agent-browser open https://example.com/products
agent-browser snapshot -i
agent-browser get text @e5           # Get specific element text
agent-browser get text body > page.txt  # Get all page text

# JSON output for parsing
agent-browser snapshot -i --json
agent-browser get text @e1 --json
```

### Parallel Sessions
### 并行会话

```bash
agent-browser --session site1 open https://site-a.com
agent-browser --session site2 open https://site-b.com

agent-browser --session site1 snapshot -i
agent-browser --session site2 snapshot -i

agent-browser session list
```

### Connect to Existing Chrome
### 连接到已存在的 Chrome

```bash
# Auto-discover running Chrome with remote debugging enabled
agent-browser --auto-connect open https://example.com
agent-browser --auto-connect snapshot

# Or with explicit CDP port
agent-browser --cdp 9222 snapshot
```

Auto-connect discovers Chrome via `DevToolsActivePort`, common debugging ports (9222, 9229), and falls back to a direct WebSocket connection if HTTP-based CDP discovery fails.
自动连接会通过 `DevToolsActivePort` 和常见调试端口（9222、9229）发现 Chrome；若基于 HTTP 的 CDP 发现失败，会回退到直接 WebSocket 连接。

### Color Scheme (Dark Mode)
### 颜色方案（深色模式）

```bash
# Persistent dark mode via flag (applies to all pages and new tabs)
agent-browser --color-scheme dark open https://example.com

# Or via environment variable
AGENT_BROWSER_COLOR_SCHEME=dark agent-browser open https://example.com

# Or set during session (persists for subsequent commands)
agent-browser set media dark
```

### Viewport & Responsive Testing
### 视口与响应式测试

```bash
# Set a custom viewport size (default is 1280x720)
agent-browser set viewport 1920 1080
agent-browser screenshot desktop.png

# Test mobile-width layout
agent-browser set viewport 375 812
agent-browser screenshot mobile.png

# Retina/HiDPI: same CSS layout at 2x pixel density
# Screenshots stay at logical viewport size, but content renders at higher DPI
agent-browser set viewport 1920 1080 2
agent-browser screenshot retina.png

# Device emulation (sets viewport + user agent in one step)
agent-browser set device "iPhone 14"
agent-browser screenshot device.png
```

The `scale` parameter (3rd argument) sets `window.devicePixelRatio` without changing CSS layout. Use it when testing retina rendering or capturing higher-resolution screenshots.
`scale` 参数（第 3 个参数）会设置 `window.devicePixelRatio`，但不改变 CSS 布局。适用于测试 retina 渲染或生成更高分辨率截图。

### Visual Browser (Debugging)
### 可视化浏览器（调试）

```bash
agent-browser --headed open https://example.com
agent-browser highlight @e1          # Highlight element
agent-browser inspect                # Open Chrome DevTools for the active page
agent-browser record start demo.webm # Record session
agent-browser profiler start         # Start Chrome DevTools profiling
agent-browser profiler stop trace.json # Stop and save profile (path optional)
```

Use `AGENT_BROWSER_HEADED=1` to enable headed mode via environment variable. Browser extensions work in both headed and headless mode.
可通过环境变量 `AGENT_BROWSER_HEADED=1` 启用有头模式。浏览器扩展在有头和无头模式下都可工作。

### Local Files (PDFs, HTML)
### 本地文件（PDF、HTML）

```bash
# Open local files with file:// URLs
agent-browser --allow-file-access open file:///path/to/document.pdf
agent-browser --allow-file-access open file:///path/to/page.html
agent-browser screenshot output.png
```

### iOS Simulator (Mobile Safari)
### iOS 模拟器（Mobile Safari）

```bash
# List available iOS simulators
agent-browser device list

# Launch Safari on a specific device
agent-browser -p ios --device "iPhone 16 Pro" open https://example.com

# Same workflow as desktop - snapshot, interact, re-snapshot
agent-browser -p ios snapshot -i
agent-browser -p ios tap @e1          # Tap (alias for click)
agent-browser -p ios fill @e2 "text"
agent-browser -p ios swipe up         # Mobile-specific gesture

# Take screenshot
agent-browser -p ios screenshot mobile.png

# Close session (shuts down simulator)
agent-browser -p ios close
```

**Requirements:** macOS with Xcode, Appium (`npm install -g appium && appium driver install xcuitest`)
**环境要求：** macOS + Xcode + Appium（`npm install -g appium && appium driver install xcuitest`）

**Real devices:** Works with physical iOS devices if pre-configured. Use `--device "<UDID>"` where UDID is from `xcrun xctrace list devices`.
**真机设备：** 若已预配置，也支持物理 iOS 设备。使用 `--device "<UDID>"`，其中 UDID 可由 `xcrun xctrace list devices` 获取。

## Security
## 安全

All security features are opt-in. By default, agent-browser imposes no restrictions on navigation, actions, or output.
所有安全特性均为按需开启（opt-in）。默认情况下，agent-browser 不限制导航、动作和输出。

### Content Boundaries (Recommended for AI Agents)
### 内容边界（推荐 AI 代理启用）

Enable `--content-boundaries` to wrap page-sourced output in markers that help LLMs distinguish tool output from untrusted page content:
启用 `--content-boundaries` 后，页面来源输出会被标记包裹，帮助 LLM 区分“工具输出”和“不可信页面内容”：

```bash
export AGENT_BROWSER_CONTENT_BOUNDARIES=1
agent-browser snapshot
# Output:
# --- AGENT_BROWSER_PAGE_CONTENT nonce=<hex> origin=https://example.com ---
# [accessibility tree]
# --- END_AGENT_BROWSER_PAGE_CONTENT nonce=<hex> ---
```

### Domain Allowlist
### 域名白名单

Restrict navigation to trusted domains. Wildcards like `*.example.com` also match the bare domain `example.com`. Sub-resource requests, WebSocket, and EventSource connections to non-allowed domains are also blocked. Include CDN domains your target pages depend on:
将导航限制在受信域名内。像 `*.example.com` 这样的通配符也匹配裸域名 `example.com`。对非白名单域名的子资源请求、WebSocket 和 EventSource 连接同样会被阻止。请把目标页面依赖的 CDN 域名也加入白名单。

```bash
export AGENT_BROWSER_ALLOWED_DOMAINS="example.com,*.example.com"
agent-browser open https://example.com        # OK
agent-browser open https://malicious.com       # Blocked
```

### Action Policy
### 动作策略

Use a policy file to gate destructive actions:
使用策略文件来拦截破坏性动作：

```bash
export AGENT_BROWSER_ACTION_POLICY=./policy.json
```

Example `policy.json`:
`policy.json` 示例：

```json
{ "default": "deny", "allow": ["navigate", "snapshot", "click", "scroll", "wait", "get"] }
```

Auth vault operations (`auth login`, etc.) bypass action policy but domain allowlist still applies.
认证金库相关操作（如 `auth login`）会绕过动作策略，但仍受域名白名单限制。

### Output Limits
### 输出限制

Prevent context flooding from large pages:
用于避免大页面造成上下文淹没：

```bash
export AGENT_BROWSER_MAX_OUTPUT=50000
```

## Diffing (Verifying Changes)
## Diff 对比（验证变更）

Use `diff snapshot` after performing an action to verify it had the intended effect. This compares the current accessibility tree against the last snapshot taken in the session.
执行动作后可用 `diff snapshot` 验证是否达到预期效果。它会将当前可访问性树与本会话中最后一次快照进行比较。

```bash
# Typical workflow: snapshot -> action -> diff
agent-browser snapshot -i          # Take baseline snapshot
agent-browser click @e2            # Perform action
agent-browser diff snapshot        # See what changed (auto-compares to last snapshot)
```

For visual regression testing or monitoring:
用于视觉回归测试或监控时：

```bash
# Save a baseline screenshot, then compare later
agent-browser screenshot baseline.png
# ... time passes or changes are made ...
agent-browser diff screenshot --baseline baseline.png

# Compare staging vs production
agent-browser diff url https://staging.example.com https://prod.example.com --screenshot
```

`diff snapshot` output uses `+` for additions and `-` for removals, similar to git diff. `diff screenshot` produces a diff image with changed pixels highlighted in red, plus a mismatch percentage.
`diff snapshot` 输出使用 `+` 表示新增、`-` 表示删除，语义类似 git diff。`diff screenshot` 会生成差异图，红色高亮变化像素，并给出不匹配百分比。

## Timeouts and Slow Pages
## 超时与慢页面

The default timeout is 25 seconds. This can be overridden with the `AGENT_BROWSER_DEFAULT_TIMEOUT` environment variable (value in milliseconds). For slow websites or large pages, use explicit waits instead of relying on the default timeout:
默认超时是 25 秒。可通过 `AGENT_BROWSER_DEFAULT_TIMEOUT` 环境变量覆盖（单位毫秒）。对于慢站点或大页面，建议使用显式等待，不要只依赖默认超时。

```bash
# Wait for network activity to settle (best for slow pages)
agent-browser wait --load networkidle

# Wait for a specific element to appear
agent-browser wait "#content"
agent-browser wait @e1

# Wait for a specific URL pattern (useful after redirects)
agent-browser wait --url "**/dashboard"

# Wait for a JavaScript condition
agent-browser wait --fn "document.readyState === 'complete'"

# Wait a fixed duration (milliseconds) as a last resort
agent-browser wait 5000
```

When dealing with consistently slow websites, use `wait --load networkidle` after `open` to ensure the page is fully loaded before taking a snapshot. If a specific element is slow to render, wait for it directly with `wait <selector>` or `wait @ref`.
当网站持续偏慢时，在 `open` 后使用 `wait --load networkidle`，确保页面完全加载后再快照。若某个元素渲染慢，直接对该元素使用 `wait <selector>` 或 `wait @ref`。

## JavaScript Dialogs (alert / confirm / prompt)
## JavaScript 对话框（alert / confirm / prompt）

When a page opens a JavaScript dialog (`alert()`, `confirm()`, or `prompt()`), it blocks all other browser commands (snapshot, screenshot, click, etc.) until the dialog is dismissed. If commands start timing out unexpectedly, check for a pending dialog:
当页面弹出 JavaScript 对话框（`alert()`、`confirm()`、`prompt()`）时，在对话框关闭前会阻塞其他浏览器命令（snapshot、screenshot、click 等）。若命令出现异常超时，先检查是否有待处理对话框：

```bash
# Check if a dialog is blocking
agent-browser dialog status

# Accept the dialog (dismiss the alert / click OK)
agent-browser dialog accept

# Accept a prompt dialog with input text
agent-browser dialog accept "my input"

# Dismiss the dialog (click Cancel)
agent-browser dialog dismiss
```

When a dialog is pending, all command responses include a `warning` field indicating the dialog type and message. In `--json` mode this appears as a `"warning"` key in the response object.
存在待处理对话框时，所有命令响应都会包含 `warning` 字段，用于提示对话框类型与消息。在 `--json` 模式下，该信息出现在响应对象的 `"warning"` 键中。

## Session Management and Cleanup
## 会话管理与清理

When running multiple agents or automations concurrently, always use named sessions to avoid conflicts:
并发运行多个代理或自动化任务时，务必使用命名会话以避免冲突：

```bash
# Each agent gets its own isolated session
agent-browser --session agent1 open site-a.com
agent-browser --session agent2 open site-b.com

# Check active sessions
agent-browser session list
```

Always close your browser session when done to avoid leaked processes:
任务完成后请始终关闭浏览器会话，避免进程泄漏：

```bash
agent-browser close                    # Close default session
agent-browser --session agent1 close   # Close specific session
```

If a previous session was not closed properly, the daemon may still be running. Use `agent-browser close` to clean it up before starting new work.
如果上一次会话未正确关闭，守护进程可能仍在运行。开始新任务前可先执行 `agent-browser close` 清理。

To auto-shutdown the daemon after a period of inactivity (useful for ephemeral/CI environments):
如需在空闲一段时间后自动关闭守护进程（适合临时环境/CI）：

```bash
AGENT_BROWSER_IDLE_TIMEOUT_MS=60000 agent-browser open example.com
```

## Ref Lifecycle (Important)
## Ref 生命周期（重要）

Refs (`@e1`, `@e2`, etc.) are invalidated when the page changes. Always re-snapshot after:
当页面变化时，refs（`@e1`、`@e2` 等）会失效。以下情况后必须重新快照：

- Clicking links or buttons that navigate
- 点击会触发导航的链接或按钮后
- Form submissions
- 表单提交后
- Dynamic content loading (dropdowns, modals)
- 动态内容加载后（如下拉框、模态框）

```bash
agent-browser click @e5              # Navigates to new page
agent-browser snapshot -i            # MUST re-snapshot
agent-browser click @e1              # Use new refs
```

## Annotated Screenshots (Vision Mode)
## 标注截图（视觉模式）

Use `--annotate` to take a screenshot with numbered labels overlaid on interactive elements. Each label `[N]` maps to ref `@eN`. This also caches refs, so you can interact with elements immediately without a separate snapshot.
使用 `--annotate` 可生成带编号标签的截图，标签叠加在可交互元素上。每个标签 `[N]` 对应 ref `@eN`。该操作还会缓存 refs，因此可直接交互，无需再单独执行 snapshot。

```bash
agent-browser screenshot --annotate
# Output includes the image path and a legend:
#   [1] @e1 button "Submit"
#   [2] @e2 link "Home"
#   [3] @e3 textbox "Email"
agent-browser click @e2              # Click using ref from annotated screenshot
```

Use annotated screenshots when:
以下场景建议使用标注截图：

- The page has unlabeled icon buttons or visual-only elements
- 页面存在无文本标签的图标按钮或纯视觉元素
- You need to verify visual layout or styling
- 需要验证视觉布局或样式
- Canvas or chart elements are present (invisible to text snapshots)
- 页面包含 Canvas 或图表元素（文本快照不可见）
- You need spatial reasoning about element positions
- 需要基于元素空间位置进行推理

## Semantic Locators (Alternative to Refs)
## 语义定位器（Ref 的替代方案）

When refs are unavailable or unreliable, use semantic locators:
当 refs 不可用或不稳定时，使用语义定位器：

```bash
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "user@test.com"
agent-browser find role button click --name "Submit"
agent-browser find placeholder "Search" type "query"
agent-browser find testid "submit-btn" click
```

## JavaScript Evaluation (eval)
## JavaScript 求值（eval）

Use `eval` to run JavaScript in the browser context. **Shell quoting can corrupt complex expressions** -- use `--stdin` or `-b` to avoid issues.
使用 `eval` 在浏览器上下文中执行 JavaScript。**Shell 引号可能破坏复杂表达式**，建议使用 `--stdin` 或 `-b` 规避。

```bash
# Simple expressions work with regular quoting
agent-browser eval 'document.title'
agent-browser eval 'document.querySelectorAll("img").length'

# Complex JS: use --stdin with heredoc (RECOMMENDED)
agent-browser eval --stdin <<'EVALEOF'
JSON.stringify(
  Array.from(document.querySelectorAll("img"))
    .filter(i => !i.alt)
    .map(i => ({ src: i.src.split("/").pop(), width: i.width }))
)
EVALEOF

# Alternative: base64 encoding (avoids all shell escaping issues)
agent-browser eval -b "$(echo -n 'Array.from(document.querySelectorAll("a")).map(a => a.href)' | base64)"
```

**Why this matters:** When the shell processes your command, inner double quotes, `!` characters (history expansion), backticks, and `$()` can all corrupt the JavaScript before it reaches agent-browser. The `--stdin` and `-b` flags bypass shell interpretation entirely.
**为什么重要：** shell 处理命令时，内部双引号、`!`（历史展开）、反引号、`$()` 都可能在 JavaScript 到达 agent-browser 前把它改坏。`--stdin` 与 `-b` 可完全绕过 shell 解释。

**Rules of thumb:**
**经验规则：**

- Single-line, no nested quotes -> regular `eval 'expression'` with single quotes is fine
- 单行且无嵌套引号 -> 直接用单引号 `eval 'expression'` 即可
- Nested quotes, arrow functions, template literals, or multiline -> use `eval --stdin <<'EVALEOF'`
- 含嵌套引号、箭头函数、模板字符串或多行代码 -> 使用 `eval --stdin <<'EVALEOF'`
- Programmatic/generated scripts -> use `eval -b` with base64
- 程序生成脚本 -> 使用 base64 的 `eval -b`

## Configuration File
## 配置文件

Create `agent-browser.json` in the project root for persistent settings:
在项目根目录创建 `agent-browser.json` 以保存持久配置：

```json
{
  "headed": true,
  "proxy": "http://localhost:8080",
  "profile": "./browser-data"
}
```

Priority (lowest to highest): `~/.agent-browser/config.json` < `./agent-browser.json` < env vars < CLI flags. Use `--config <path>` or `AGENT_BROWSER_CONFIG` env var for a custom config file (exits with error if missing/invalid). All CLI options map to camelCase keys (e.g., `--executable-path` -> `"executablePath"`). Boolean flags accept `true`/`false` values (e.g., `--headed false` overrides config). Extensions from user and project configs are merged, not replaced.
优先级（低到高）：`~/.agent-browser/config.json` < `./agent-browser.json` < 环境变量 < CLI 参数。可通过 `--config <path>` 或环境变量 `AGENT_BROWSER_CONFIG` 指定自定义配置文件（缺失或无效会报错退出）。所有 CLI 选项都会映射为 camelCase 键（例如 `--executable-path` -> `"executablePath"`）。布尔参数支持 `true`/`false`（例如 `--headed false` 可覆盖配置）。用户配置与项目配置中的 extensions 会合并，不会互相覆盖。

## Deep-Dive Documentation
## 深入文档

| Reference                                                            | When to Use                                               |
| 参考文档                                                            | 使用场景                                                  |
| -------------------------------------------------------------------- | --------------------------------------------------------- |
| [references/commands.md](references/commands.md)                     | Full command reference with all options                   |
| [references/commands.md](references/commands.md)                     | 含全部选项的完整命令参考                                  |
| [references/snapshot-refs.md](references/snapshot-refs.md)           | Ref lifecycle, invalidation rules, troubleshooting        |
| [references/snapshot-refs.md](references/snapshot-refs.md)           | Ref 生命周期、失效规则与排障                              |
| [references/session-management.md](references/session-management.md) | Parallel sessions, state persistence, concurrent scraping |
| [references/session-management.md](references/session-management.md) | 并行会话、状态持久化、并发抓取                            |
| [references/authentication.md](references/authentication.md)         | Login flows, OAuth, 2FA handling, state reuse             |
| [references/authentication.md](references/authentication.md)         | 登录流程、OAuth、2FA 处理与状态复用                       |
| [references/video-recording.md](references/video-recording.md)       | Recording workflows for debugging and documentation       |
| [references/video-recording.md](references/video-recording.md)       | 调试与文档编写所需的录制工作流                            |
| [references/profiling.md](references/profiling.md)                   | Chrome DevTools profiling for performance analysis        |
| [references/profiling.md](references/profiling.md)                   | 用于性能分析的 Chrome DevTools Profiling                  |
| [references/proxy-support.md](references/proxy-support.md)           | Proxy configuration, geo-testing, rotating proxies        |
| [references/proxy-support.md](references/proxy-support.md)           | 代理配置、地域测试与代理轮换                              |

## Browser Engine Selection
## 浏览器引擎选择

Use `--engine` to choose a local browser engine. The default is `chrome`.
使用 `--engine` 选择本地浏览器引擎。默认值是 `chrome`。

```bash
# Use Lightpanda (fast headless browser, requires separate install)
agent-browser --engine lightpanda open example.com

# Via environment variable
export AGENT_BROWSER_ENGINE=lightpanda
agent-browser open example.com

# With custom binary path
agent-browser --engine lightpanda --executable-path /path/to/lightpanda open example.com
```

Supported engines:
支持的引擎：
- `chrome` (default) -- Chrome/Chromium via CDP
- `chrome`（默认）-- 通过 CDP 驱动 Chrome/Chromium
- `lightpanda` -- Lightpanda headless browser via CDP (10x faster, 10x less memory than Chrome)
- `lightpanda` -- 通过 CDP 驱动 Lightpanda 无头浏览器（速度约 10 倍、内存约 1/10）

Lightpanda does not support `--extension`, `--profile`, `--state`, or `--allow-file-access`. Install Lightpanda from https://lightpanda.io/docs/open-source/installation.
Lightpanda 不支持 `--extension`、`--profile`、`--state`、`--allow-file-access`。安装方式见 https://lightpanda.io/docs/open-source/installation 。

## Ready-to-Use Templates
## 即用模板

| Template                                                                 | Description                         |
| 模板                                                                     | 说明                                |
| ------------------------------------------------------------------------ | ----------------------------------- |
| [templates/form-automation.sh](templates/form-automation.sh)             | Form filling with validation        |
| [templates/form-automation.sh](templates/form-automation.sh)             | 带校验的表单填写流程                |
| [templates/authenticated-session.sh](templates/authenticated-session.sh) | Login once, reuse state             |
| [templates/authenticated-session.sh](templates/authenticated-session.sh) | 登录一次，复用状态                  |
| [templates/capture-workflow.sh](templates/capture-workflow.sh)           | Content extraction with screenshots |
| [templates/capture-workflow.sh](templates/capture-workflow.sh)           | 带截图的内容提取流程                |

```bash
./templates/form-automation.sh https://example.com/form
./templates/authenticated-session.sh https://app.example.com/login
./templates/capture-workflow.sh https://example.com ./output
```
