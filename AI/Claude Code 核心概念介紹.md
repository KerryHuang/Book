# Claude Code 核心概念介紹

## 一、子代理 (Agents)

放在 `.claude/agents/{name}/AGENT.md`，是在**獨立上下文**中運行的專業 AI 助手。

| 特性       | 說明                             |
| ---------- | -------------------------------- |
| 隔離上下文 | 不污染主對話                     |
| 工具限制   | 可限定只讀或特定工具             |
| 模型選擇   | 可指定 sonnet/opus/haiku         |
| 自動委託   | Claude 根據 description 自動選擇 |

**內建子代理**：Explore（快速搜尋）、Plan（規劃）、General-purpose（多步驟任務）

**Frontmatter 重要欄位**：`name`、`description`、`tools`、`model`、`maxTurns`、`isolation`

------

## 二、技能/斜線命令 (Skills/Commands)

放在 `.claude/skills/{name}/SKILL.md`，是**可重用的工作流程模板**，透過 `/skill-name` 呼叫。

| 特性     | 說明                                                         |
| -------- | ------------------------------------------------------------ |
| 手動呼叫 | `/deploy production`、`/commit`                              |
| 自動呼叫 | Claude 根據 description 判斷（除非 `disable-model-invocation: true`） |
| 引數支援 | `$ARGUMENTS` 替換使用者傳入的參數                            |
| 動態內容 | `!`command`` 語法執行命令並注入結果                          |
| 隔離執行 | `context: fork` 在子代理中運行                               |

**Frontmatter 重要欄位**：`name`、`description`、`user-invocable`、`disable-model-invocation`、`allowed-tools`、`argument-hint`

------

## 三、規則 (Rules)

放在 `.claude/rules/*.md`，是**路徑相關的條件指引**。

| 特性       | 說明                                |
| ---------- | ----------------------------------- |
| 全域規則   | 無 `paths` frontmatter → 始終載入   |
| 路徑限定   | 有 `paths` → 僅當操作匹配路徑時載入 |
| 節省上下文 | 不需要的規則不會佔用 token          |



```yaml
---
paths:
  - "src/api/**/*.ts"
---
# 僅對 API 檔案生效的規則
```

------

## 四、CLAUDE.md vs Rules vs Skills vs Agents



```
Layer 1: CLAUDE.md <law> — 強制性系統法則，啟動時全部載入
Layer 2: Rules           — 條件性指導，按路徑載入
Layer 3: Skills          — 可重用任務流程，按需呼叫
Layer 4: Agents          — 專業化委託，隔離上下文執行
```

| 需求                     | 選擇              |
| ------------------------ | ----------------- |
| 全專案強制規範           | CLAUDE.md `<law>` |
| 特定檔案類型約定         | Rule（加 paths）  |
| 可重用工作流程/模板      | Skill             |
| 需要隔離上下文的專業任務 | Agent             |

本專案已有完整配置：14 個 skills、6 個 agents、12 個 rules，覆蓋從需求撰寫到部署提交的完整開發流程。