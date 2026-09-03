---
kind: original
---

# 第十三章：安裝 Qdrant（向量資料庫）到 Docker

Qdrant 是專為 AI、搜尋與相似度查詢所設計的向量資料庫，支援高效的向量檢索。以下將介紹如何在本機環境利用 Docker 快速安裝 Qdrant，適合想嘗試 AI 向量搜尋、建置 RAG 系統、或資料科學相關應用的開發者。

## 前言

Qdrant 是一款開源的向量資料庫，支援高維向量的儲存、查詢與篩選，常見應用於語意搜尋、推薦系統、聊天機器人等。利用 Docker 安裝能快速建置可移植的測試或開發環境。

## 步驟一：準備環境

### 1. 安裝 Docker

請先確認你的電腦已安裝好 Docker。
若尚未安裝，請參考官方教學：Docker 官方安裝教學

### 2. 下載 Qdrant 映像檔

Qdrant 官方提供 Docker 映像檔，可以直接從 Docker Hub 取得。

```bash
docker pull qdrant/qdrant
```

## 步驟二：啟動 Qdrant 容器（含 Windows / Mac 環境指令）

### 1. 於 Linux / macOS 終端機

可直接於專案目錄下輸入：

```bash
docker run -d \
  -p 6333:6333 \
  -v $(pwd)/qdrant_data:/qdrant/storage \
  --name qdrant \
  qdrant/qdrant
```

- `$(pwd)` 會自動取得目前目錄路徑。

### 2. 於 Windows CMD / PowerShell

需改用絕對路徑，例如：

```bash
docker run -d -p 6333:6333 -v E:/docker/qdrant_data:/qdrant/storage --name qdrant qdrant/qdrant
```

- `E:/docker/qdrant_data` 請自行建立對應資料夾，或改成你想存放的資料路徑。
- 若使用 PowerShell，可用 `${PWD}` 取得目前目錄：

```bash
docker run -d -p 6333:6333 -v ${PWD}/qdrant_data:/qdrant/storage --name qdrant qdrant/qdrant
```

> 建議路徑以英文資料夾命名避免權限或特殊字元問題。

### 3. 開發環境直接啟動（資料不需持久化）

#### Linux / macOS

```bash
docker run -d -p 6333:6333 --name qdrant-dev qdrant/qdrant
```

#### Windows CMD / PowerShell

```bash
docker run -d -p 6333:6333 --name qdrant-dev qdrant/qdrant
```

### 資料持久化

#### Linux / macOS

```bash
docker run -d \
  -p 6333:6333 \
  -v ~/qdrant_data:/qdrant/storage \
  --restart=always \
  --name qdrant \
  qdrant/qdrant

```

#### Windows CMD / PowerShell

```bash
docker run -d `
  -p 6333:6333 `
  -v E:\docker\qdrant_data:/qdrant/storage `
  --restart=always `
  --name qdrant `
  qdrant/qdrant
```


- `-p 6333:6333`：將本機 6333 埠口對應到容器內的 6333 埠口（REST API 入口）。
- `-v $(pwd)/qdrant_data:/qdrant/storage`：將本機的 `qdrant_data` 資料夾對應到容器內的資料存放路徑，方便資料持久化。
- `--name qdrant`：命名此容器為 qdrant。

> 若你在 Windows，`$(pwd)` 請改為對應本機資料夾路徑（例如 `C:/qdrant_data:/qdrant/storage`）。

---

## 步驟三：開發用法 - 直接啟動快速測試

開發階段若只需快速啟動（不需資料持久化），可以簡化為下列指令：

```bash
docker run -d -p 6333:6333 --name qdrant-dev qdrant/qdrant
```

- **說明**：這樣啟動的 Qdrant 資料將只存在於容器中，關閉或刪除容器即會消失。適合用於開發、測試、CI/CD pipeline。

如需重新啟動開發容器：

```bash
docker stop qdrant-dev
# 再啟動
docker start qdrant-dev
```

如需清除：

```bash
docker rm -f qdrant-dev
```

## 步驟四：測試 Qdrant 是否安裝成功

啟動後，可用瀏覽器或 `curl` 測試 Qdrant API 是否正常運作：

```bash
curl http://localhost:6333/collections
```

如果看到空集合（或 JSON 回應），表示 Qdrant 已成功啟動。

## 常用指令

- **查看容器狀態**

  ```bash
  docker ps
  ```

- **停止容器**

  ```bash
  docker stop qdrant
  ```

- **重啟容器**

  ```bash
  docker start qdrant
  ```

- **移除容器**

  ```bash
  docker rm -f qdrant
  ```

## 常見問題

### 1. 埠號衝突怎麼辦？

如本機 6333 埠已被佔用，可將 `-p 6333:6333` 改為其他未被佔用的埠口，例如 `-p 7000:6333`，使用時記得改用 `http://localhost:7000/collections`。

### 2. 如何更改資料保存路徑？

預設會將資料儲存在 `$(pwd)/qdrant_data`，可自行更換路徑，但要確保對應資料夾已建立且有權限。

### 3. 如何升級 Qdrant 版本？

執行 `docker pull qdrant/qdrant:latest` 取得最新版本，再重啟容器即可。

## 參考資源

- Qdrant 官方文件
- Docker Hub - qdrant/qdrant
- 向量資料庫應用介紹