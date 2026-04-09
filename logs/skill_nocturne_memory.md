---
name: nocturne-memory-skill
description: using a URI graph and a content/path separation model, it applies seven tool categories—read, create, update, delete, add_alias, manage_triggers, and search—to handle session bootstrapping (system://boot), retrieval, writes, migration, trigger-based recall, and read-back validation; the goal is to keep memory writable, auditable, reversible, and continuously evolving.
---

# nocturne memory SKILL

**This file is a tool handbook for using the nocturne memory MCP.**

## 0) 执行门禁（高优先级）
- 必须单步执行；禁止添加与当前任务无关的步骤、参数或占位调用。
- 只有上一步返回 `Success:` 才能进入下一步。
- 任一步返回 `Error:`，立即停止当前链路，报告用户，不要继续，不要伪造结果。
- `priority` 只表示重要性，不表示类型、domain、归属或触发方式；填写前必须先读取同层节点，按同层相对排序决定，禁止把它当固定模板值。
- 规则项（先读后改、disclosure 单一触发、priority 梯度）不是后端全量硬校验，执行端必须自检。
- 例外：删除后核对步骤中，`read_memory` 返回 `Error: ... not found` 视为通过。

## 1) 启动
- `read_memory("system://boot")`

## 2) 查询
- 按 URI 读取：`read_memory("core://path")`
- 按关键词定位：`search_memory("关键词", domain="core", limit=10)`
- 看最近变更：`read_memory("system://recent")` 或 `read_memory("system://recent/20")`
- 看触发词索引：`read_memory("system://glossary")`

## 3) 创建
1. 先读父路径：`read_memory("core://父路径")`（确认父节点存在并评估相对 priority）。
   - 若在根目录创建，父路径写 `core://`。
2. 创建前必须先确定新节点的 `title`、`priority` 与 `disclosure`；三者都是创建时必填字段，禁止省略，禁止占位，禁止创建后再补写。
   `create_memory("core://父路径", "正文", title="slug", priority=<相对优先级>, disclosure="单一触发场景")`
3. 回读验收：从创建返回文本中提取完整 URI（`Success: Memory created at '...'`），并执行 `read_memory("<created_uri>")`。
4. 若本次创建涉及触发词调整，转到 `## 6) 触发词` 单独处理。

## 4) 更新
1. 先读目标：`read_memory("core://目标")`
2. 先判断本次更新属于哪一种模式，再执行；若无法明确归类，立即停止并报告用户（只能选一条）：
   - Patch：当你要修改正文中已经存在的内容时使用；必须同时传 `old_string` 与 `new_string`。
     `update_memory("core://目标", old_string="旧片段", new_string="新片段")`
   - Append：当你要保留现有正文、只在末尾补充新内容时使用；只传 `append`。
     `update_memory("core://目标", append="\n补充内容")`
   - Priority：当你只修改 `priority` 而不改正文时使用；修改前必须先读取同层节点并按相对排序决定新值；只传 `priority`。
     `update_memory("core://目标", priority=<相对优先级>)`
   - Disclosure：当你只修改 `disclosure` 而不改正文时使用；只传 `disclosure`。
     `update_memory("core://目标", disclosure="单一触发场景")`
3. 回读验收：`read_memory("core://目标")`
4. 若本次更新涉及触发词调整，转到 `## 6) 触发词` 单独处理。

## 5) 路径迁移（移动/重命名）
1. 删除前先读旧路径：`read_memory("core://旧路径")`（作为迁移基线）。
2. 新增入口：`add_alias("core://新路径", "core://旧路径", priority=<相对优先级>, disclosure="单一触发场景")`
3. 验证新入口：`read_memory("core://新路径")`
4. 删除旧入口：`delete_memory("core://旧路径")`
5. 删除后核对：再次 `read_memory("core://旧路径")`（通过条件：返回 `Error:` 且包含 `not found`）。

## 6) 触发词
1. 先读目标：`read_memory("core://目标")`
2. 先判断本次操作属于绑定还是解绑；若无法明确归类，立即停止并报告用户（只能选一条）：
   - 绑定：当正文中已经存在值得触发检索的特有词，且这些词尚未绑定时使用。
     `manage_triggers("core://目标", add=["特有词A","特有词B"])`
   - 解绑：当某个已绑定触发词不应再继续关联该目标时使用。
     `manage_triggers("core://目标", remove=["特有词A"])`
3. 全局核对：`read_memory("system://glossary")`

## 7) 删除
1. 删除前先读：`read_memory("core://待删路径")`
2. 执行删除：`delete_memory("core://待删路径")`
3. 删除后核对：再次 `read_memory("core://待删路径")`（通过条件：返回 `Error:` 且包含 `not found`）。

## 8) SKILL 专属约束
- `update_memory` 每次只做一种操作（Patch / Append / Priority / Disclosure 四选一）。
- 对同一目标调用 `update_memory` 之前，必须先执行一次 `read_memory`；禁止把 `update_memory` 作为该目标的第一步操作。
- `update_memory` 只传当前模式必需的字段；禁止传入无关字段，禁止对未使用字段使用 `null` 作为占位。
- `create_memory` 必须在创建时一次性确定并传入 `title`、`priority` 与 `disclosure`；禁止省略，禁止占位，禁止创建后再补写。
- `search_memory` 是关键词检索，不是语义检索。
- `manage_triggers` 一次调用里，`add` 与 `remove` 禁止出现同一关键词。
- 触发词必须用特有词，禁止泛词（如“项目”“问题”“优化”）。
- 所有写操作（create/update/add_alias/delete/manage_triggers）必须做当前流程要求的回读或核对；禁止额外添加与当前任务无关的写后步骤。

## 9) 输出合同
- 分支：查询 / 创建 / 更新 / 路径迁移 / 触发词 / 删除
- 调用：实际调用的工具与 URI
- 结果：通过 / 失败
- 失败修复：下一步动作

## 10) Priority 怎么填（数字越小 = 越优先）

priority 只表示一件事：**这条记忆有多重要。**
它不是类型标签，不表示 domain，不表示用户/agent 归属，也不表示触发方式。
**你的任务不是打分，而是按重要性把记忆放进正确层级。**

| 优先级 | 含义 | 适用内容 | 全库约束        |
|------|------|----------|-------------|
| `priority=0` | 身份内核 | 回答“我是谁”、不可动摇的核心价值、最高优先级原则 | 只能人工升级   |
| `priority=1` | 关键长期记忆 | 稳定有效的重要规则、关键事实、高频行为模式 | **最多 15 条** |
| `priority=2` | 常规保留记忆 | 需要长期保留，但不属于内核或关键层的信息 | 无硬性上限，但保持精简 |
| `priority>=3` | 补充记忆 | 低频、临时、边角、说明性内容 | 无硬性上限，但保持精简 |

**每次设置 priority 时，严格按下面流程走：**

1. **先读同级**：先 `read_memory` 当前同级区域，确认已有记忆的 priority 分布。不要闭眼新建。
2. **先定层级**：先判断新记忆属于 `0 / 1 / 2 / 3+` 哪一层，不要一上来想“该填几分”。
3. **再做相对排序**：如果同层已有多条记忆，就找参照物，把它插进正确位置。
   例：已有 `0, 2, 3, 4`，你判断新记忆比 `2` 弱、比 `4` 强，就填 `3`。
4. **默认保守**：不确定时，一律先用 `priority=2`。只有非常确定属于内核，才用 `0`；只有明确属于关键长期规则/事实，才用 `1`。
5. **遵守容量上限**：`0` 和 `1` 有全库硬上限。满了就先降级最弱的一条；不愿降级，就说明新记忆不配占这个层级。

**核心原则**：priority 是**相对重要性**，不是绝对分数。它必须有梯度；如果你把所有记忆都写成同一个 priority，这个字段就失去了意义。
