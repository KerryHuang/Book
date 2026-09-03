---
kind: original
---

# Graphify + Claude Code 的實戰安裝手冊（macOS / Windows / WSL）

以下為 **Graphify + Claude Code 實戰安裝手冊**，分成 **macOS / Windows / WSL（推薦）** 三種環境，並附上完整流程與常見問題處理。

------

# 一、前置需求（所有平台共通）

### 必要條件

- Python **3.10 以上**
- 已安裝 **Claude Code CLI**
- Git（建議）
- 網路可正常存取 PyPI

### 注意

Graphify 套件名稱是：

```
graphifyy
```

不是 `graphify`

------

# 二、macOS 安裝流程（最穩定）

## 1. 安裝 Python（如尚未安裝）

```
brew install python
```

確認版本：

```
python3 --version
```

------

## 2. 建立虛擬環境（強烈建議）

```
python3 -m venv .venv
source .venv/bin/activate
```

------

## 3. 安裝 Graphify

```
pip install graphifyy
```

------

## 4. 安裝 Graphify 到 Claude Code

```
graphify install
```

------

## 5. 在專案中建立知識圖譜

```
cd your-project
/graphify .
```

輸出會在：

```
graphify-out/
```

包含：

- GRAPH_REPORT.md
- graph.json
- graph.html

------

## 6. 啟用 Claude Code 整合（關鍵步驟）

```
graphify claude install
```

這會：

- 修改 `CLAUDE.md`
- 加入 PreToolUse hooks
- 讓 Claude 自動先讀 graph report

------

## 7. 驗證

在 Claude Code 中輸入：

```
這個專案的主要模組架構是什麼？
```

若整合成功，Claude 會優先引用 `GRAPH_REPORT.md`

------

# 三、Windows 安裝流程（原生）

## 1. 安裝 Python

下載：
 https://www.python.org/downloads/

安裝時勾選：

```
Add Python to PATH
```

------

## 2. 建立虛擬環境

```
python -m venv .venv
.venv\Scripts\activate
```

------

## 3. 安裝 Graphify

```
pip install graphifyy
```

------

## 4. 安裝 Claude Code integration

```
graphify install --platform windows
```

------

## 5. 建圖

```
/graphify .
```

------

## 6. 啟用 Claude 整合

```
graphify claude install
```

------

## ⚠️ Windows 常見問題

### 問題 1：whisper / 音訊處理失敗

解法：

```
pip install faster-whisper
```

### 問題 2：路徑錯誤

請避免：

- 空格過多
- 中文路徑（部分工具仍可能有問題）

------

# 四、WSL（強烈推薦給 Windows 使用者）

這是 **最穩定且官方建議方式**

------

## 1. 安裝 WSL

```
wsl --install
```

建議 Ubuntu

------

## 2. 進入 WSL

```
wsl
```

------

## 3. 安裝 Python + venv

```
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

------

## 4. 建立虛擬環境

```
python3 -m venv .venv
source .venv/bin/activate
```

------

## 5. 安裝 Graphify（含 MCP 支援）

```
pip install "graphifyy[mcp]"
```

------

## 6. 安裝 Graphify

```
graphify install
```

------

## 7. 建圖

```
/graphify .
```

------

## 8. Claude Code 整合

```
graphify claude install
```

------

# 五、進階：MCP Server（讓 Claude 直接查圖）

## 啟動 MCP server

```
python -m graphify.serve graphify-out/graph.json
```

------

## 設定 `.mcp.json`

```
{
  "mcpServers": {
    "graphify": {
      "command": "/home/your-user/.venv/bin/python",
      "args": ["-m", "graphify.serve", "graphify-out/graph.json"]
    }
  }
}
```

------

## 功能

Claude 可直接呼叫：

- query_graph
- get_node
- shortest_path
- get_neighbors

------

# 六、實戰最佳流程（推薦）

```
# 安裝
pip install graphifyy
graphify install

# 建圖
/graphify .

# 啟用 Claude
graphify claude install
```

------

## 日常使用模式

### 模式 1：自動（推薦）

直接問 Claude：

```
auth flow 是什麼？
```

→ Claude 先看 graph，再搜尋 code

------

### 模式 2：精準查詢

```
graphify query "auth flow"
```

再把結果丟給 Claude 分析

------

### 模式 3：增量更新

```
/graphify . --update
```

------

# 七、效能與品質最佳化

## 1. 使用 `.graphifyignore`

避免污染圖譜：

```
node_modules/
dist/
build/
vendor/
*.log
```

------

## 2. Deep 模式（高品質）

```
/graphify . --mode deep
```

適合：

- 架構分析
- 文件很多的專案

------

## 3. 大型 repo 建議

第一次：

```
/graphify .
```

之後：

```
/graphify . --update
```

------

# 八、常見錯誤排除

## 問題：找不到 graphify 指令

```
which graphify
```

如果沒有：

```
pip install graphifyy
```

------

## 問題：Claude 沒有使用 graph

確認：

- `graphify-out/GRAPH_REPORT.md` 存在
- 已執行：

```
graphify claude install
```

------

## 問題：圖太大 / 太慢

解法：

- 使用 `.graphifyignore`
- 限制資料夾：

```
/graphify src/
```

------

# 九、實務建議（重要）

## 不要這樣用

- 把整個 `graph.json` 丟給 Claude（太大）
- 每次都重建整個圖

------

## 建議這樣用

1. 用 Graphify 建「結構」
2. 用 Claude 解「問題」
3. 用 query 做「精準導航」

------

# 十、結論

Graphify + Claude Code 的最佳實務是：

> **Graphify 負責建立專案地圖，Claude 負責沿著地圖推理與解釋**

這種分工可以：

- 大幅降低 context 消耗
- 提升大型專案理解速度
- 強化架構層級問答能力

------

如果需要，可進一步提供：

- 團隊導入 SOP（多人協作）
- Cursor / Copilot / Codex 整合版本
- Graphify prompt 範本（提高 Claude 表現）