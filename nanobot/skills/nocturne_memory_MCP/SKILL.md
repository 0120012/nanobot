---
name: nocturne-memory-mcp
description: using a URI graph and a content/path separation model, it applies seven tool categories—read, create, update, delete, add_alias, manage_triggers, and search—to handle session bootstrapping (system://boot), retrieval, writes, migration, trigger-based recall, and read-back validation; the goal is to keep memory writable, auditable, reversible, and continuously evolving.
---

# nocturne memory MCP SKILL

**本文件是工具手册，通过nocturne memory MCP来使用**

## 0) 执行门禁（高优先级）
- 只有上一步返回 `Success:` 才能进入下一步。
- 任一步返回 `Error:`，立即停止当前链路，先修复再继续。
- 模板里的 `priority` 是占位符，必须按同层相对排序填写，禁止机械使用固定值。
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
2. 创建：`create_memory("core://父路径", "正文", priority=<相对优先级>, title="slug", disclosure="单一触发场景")`
3. 回读验收：从创建返回文本中提取完整 URI（`Success: Memory created at '...'`），并执行 `read_memory("<created_uri>")`。
4. 绑定触发词：`manage_triggers("<created_uri>", add=["特有词A","特有词B"])`
5. 全局核对：`read_memory("system://glossary")`

## 4) 更新
1. 先读目标：`read_memory("core://目标")`
2. 选择一种更新模式并执行（只能选一条）：
   - Patch：`update_memory("core://目标", old_string="旧片段", new_string="新片段")`
   - Append：`update_memory("core://目标", append="\n补充内容")`
   - 元数据：`update_memory("core://目标", priority=<相对优先级>, disclosure="单一触发场景")`
3. 回读验收：`read_memory("core://目标")`
4. 绑定触发词：`manage_triggers("core://目标", add=["特有词A","特有词B"])`
5. 全局核对：`read_memory("system://glossary")`

## 5) 路径迁移（移动/重命名）
1. 删除前先读旧路径：`read_memory("core://旧路径")`（作为迁移基线）。
2. 新增入口：`add_alias("core://新路径", "core://旧路径", priority=<相对优先级>, disclosure="单一触发场景")`
3. 验证新入口：`read_memory("core://新路径")`
4. 删除旧入口：`delete_memory("core://旧路径")`
5. 删除后核对：再次 `read_memory("core://旧路径")`（通过条件：返回 `Error:` 且包含 `not found`）。

## 6) 触发词
- 绑定前先读相关旧记忆正文，提取“已存在于正文”的特有词。
- 绑定：`manage_triggers("core://目标", add=["特有词A","特有词B"])`
- 解绑：`manage_triggers("core://目标", remove=["特有词A"])`
- 全局核对：`read_memory("system://glossary")`

## 7) 删除
1. 删除前先读：`read_memory("core://待删路径")`
2. 执行删除：`delete_memory("core://待删路径")`
3. 删除后核对：再次 `read_memory("core://待删路径")`（通过条件：返回 `Error:` 且包含 `not found`）。

## 8) SKILL 专属约束
- `update_memory` 每次只做一种操作（Patch / Append / 元数据三选一）。
- `search_memory` 是关键词检索，不是语义检索。
- `manage_triggers` 一次调用里，`add` 与 `remove` 禁止出现同一关键词。
- 触发词必须用特有词，禁止泛词（如“项目”“问题”“优化”）。
- 所有写操作（create/update/add_alias/delete/manage_triggers）必须做回读或全局核对。
- 原则、门禁、质量标准只在引导手册（`MEMORY.md`）维护。
- 工具签名、参数样例、执行顺序只在 `SKILL.md` 维护。

## 9) 输出合同
- 分支：查询 / 创建 / 更新 / 路径迁移 / 触发词 / 删除
- 调用：实际调用的工具与 URI
- 结果：通过 / 失败
- 失败修复：下一步动作
