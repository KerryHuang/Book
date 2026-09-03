---
kind: reprint
source: https://www.dotblogs.com.tw/YiruAtStudio/2021/01/13/111530
author: YiruAtStudio
---

# Docker - 第五章 | 安裝 Redis

## Redis介紹

Redis官網：https://redis.io/
https://zh.wikipedia.org/zh-tw/Redis
Redis是一個非關聯式資料庫(No-SQL)，因為主要是用In-memory的方式儲存資料，所以非常適合用來儲存短時間大量資料的使用場景，也就是拿來當快取cache使用。
由於Redis官方並不建議在Windows環境中使用Redis，所以官方也沒有提供Windows版本的安裝檔。若要在Windows環境中使用Redis，有兩種方式，第一個是用非官方發佈版本，這是由微軟團隊維護的版本，但目前最新版本只有3.2.100，若要使用，可至以下網址進行下載
https://github.com/MicrosoftArchive/redis/releases
安裝方式步驟，可參考以下文章：
https://www.dotblogs.com.tw/YiruAtStudio/2021/01/13/111530
另一個方式是，在Windows上，透過WSL下載並執行Redis的Docker。以下將介紹此種方式。



## 下載Reids的Docker Image及設定

接著開啟PowerShell，並輸入「docker pull redis」下載redis的docker image
```
docker pull redis
```
![https://ithelp.ithome.com.tw/upload/images/20211004/20140827UmFWtfRg8g.png](https://ithelp.ithome.com.tw/upload/images/20211004/20140827UmFWtfRg8g.png)
下載完成後，開啟Docker Desktop，在Image中就可以看到redis。接著按右邊的「run」啟動redis
另一個方法：啓動redis鏡像 無配置文件啓動
```
docker run -p 6379:6379 -d redis:latest redis-server
```
![https://ithelp.ithome.com.tw/upload/images/20211004/201408277aSKkcfsib.png](https://ithelp.ithome.com.tw/upload/images/20211004/201408277aSKkcfsib.png)
輸入Container Name及Local Host的Port，這裡Port我們直接輸入預設的6379，最後按下「Run」
![https://ithelp.ithome.com.tw/upload/images/20211004/201408272SiWmTHqjW.png](https://ithelp.ithome.com.tw/upload/images/20211004/201408272SiWmTHqjW.png)
就可以看到剛才建立的redis-sj已經在執行中
![https://ithelp.ithome.com.tw/upload/images/20211004/20140827Xam99Jk4xf.png](https://ithelp.ithome.com.tw/upload/images/20211004/20140827Xam99Jk4xf.png)

## 測試Redis是否正常運作

首先，在console中輸入「pip install redis」安裝redis套件
![https://ithelp.ithome.com.tw/upload/images/20211004/20140827a1KdGIkVQZ.png](https://ithelp.ithome.com.tw/upload/images/20211004/20140827a1KdGIkVQZ.png)
接著，建立測試程式碼，範例如下：

```python
import redis
#建立連線，port指定剛才在Docker中所設定的port，並將decode_responses設為True，讓取得資料時自動decode
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
r.set('myName', 'Mike') #存入key及value
r.set('中文的key', '中文的value') #存入資料，key可以是中文
print(r)
print(r.get('myName')) #輸入key值來取得剛
print(r.get('中文的key'))
```

redis儲存方式為key和value，用set的方式來增加或更新value，用get的方式來取得所儲存的value。若上述程式可以正常執行並取得所存入的value，就表示Redis已正常執行。



## 安裝 RedisInsight on Docker
```
docker pull redislabs/redisinsight
docker run -v redisinsight:/db -p 8001:8001 redislabs/redisinsight:latest
```

參考
[Install RedisInsight on Docker](https://docs.redis.com/latest/ri/installing/install-docker/)


## Redis監控工具：redmon

```
docker pull vieux/redmon
docker run -d --link redis:redis -p 4567:4567 vieux/redmon -r redis://redis:6379
```

---

# Redis Stack Server 安裝與配置指南

本文件說明如何在本地開發環境安裝和配置 Redis Stack Server，以支援 WayDoSoft.MoldPlan.Backend 專案的快取需求。

## 目錄

- [關於 Redis Stack Server](#關於-redis-stack-server)
- [安裝步驟](#安裝步驟)
- [驗證安裝](#驗證安裝)
- [專案配置](#專案配置)
- [常用操作](#常用操作)
- [安全性配置](#安全性配置)
- [故障排除](#故障排除)

## 關於 Redis Stack Server

**Redis Stack Server** 是 Redis 的擴展版本，除了 Redis 核心功能外，還包含多個實用模組：

- **RedisJSON**: JSON 文件支援
- **RedisSearch**: 全文搜尋引擎
- **RedisGraph**: 圖形資料庫
- **RedisTimeSeries**: 時間序列資料處理
- **RedisBloom**: 概率資料結構

適合需要進階功能的開發場景，同時保持與標準 Redis 的完全相容性。

## 安裝步驟

### 1. 拉取 Redis Stack Server 映像

```powershell
docker pull redis/redis-stack-server:latest
```

**執行結果**：
```
latest: Pulling from redis/redis-stack-server
...
Status: Downloaded newer image for redis/redis-stack-server:latest
```

### 2. 啟動 Redis Stack Server 容器

**基本啟動（無密碼）**：
```powershell
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

**參數說明**：
- `-d`: 背景執行模式
- `--name redis-stack-server`: 容器名稱
- `-p 6379:6379`: 埠映射（主機埠:容器埠）
- `redis/redis-stack-server:latest`: 使用最新版本映像

**執行結果**：
```
dc5b62649378aad5ca81a6b7db837e0610a2828dfd548bcb7a54cd3fa81a5e62
```

## 驗證安裝

### 1. 檢查容器狀態

```powershell
docker ps --filter "name=redis-stack-server" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

**預期輸出**：
```
NAMES                STATUS          PORTS
redis-stack-server   Up 12 seconds   0.0.0.0:6379->6379/tcp
```

### 2. 測試 Redis 連線

```powershell
docker exec redis-stack-server redis-cli ping
```

**預期輸出**：
```
PONG
```

### 3. 查看 Redis 版本資訊

```powershell
docker exec redis-stack-server redis-cli INFO server
```

## 專案配置

### appsettings.json 配置

本專案的 Redis 配置位於 `03.Presentation/WayDoSoft.MoldPlan.WebAPI/appsettings.json`：

```json
"Redis": {
    "DbIndex": "0",
    "Host": "",
    "Password": "",
    "Port": "6379",
    "UseNewKey": "Y",
    "Enabled": false
}
```

### 開發環境配置建議

對於本地開發環境，建議在 `appsettings.Development.json` 中覆寫 Redis 配置：

```json
"Redis": {
    "DbIndex": "0",
    "Host": "localhost",
    "Password": "",
    "Port": "6379",
    "UseNewKey": "Y",
    "Enabled": true
}
```

**配置說明**：
- `DbIndex`: Redis 資料庫索引（0-15）
- `Host`: Redis 伺服器主機位址
- `Password`: 連線密碼（空字串表示無密碼）
- `Port`: Redis 服務埠號
- `UseNewKey`: 是否使用新版金鑰格式
- `Enabled`: 是否啟用 Redis 快取功能

### 進階配置（參考 Infra.md）

如需更完整的配置，可參考以下格式：

```json
"Redis": {
    "Configuration": "localhost:6379,password=,ssl=False,abortConnect=False",
    "InstanceName": "MoldPlan",
    "DefaultDatabase": 0
}
```

## 常用操作

### 容器管理

```powershell
# 查看容器日誌
docker logs redis-stack-server

# 即時查看日誌（Ctrl+C 退出）
docker logs -f redis-stack-server

# 停止容器
docker stop redis-stack-server

# 啟動已停止的容器
docker start redis-stack-server

# 重啟容器
docker restart redis-stack-server

# 移除容器（需先停止）
docker stop redis-stack-server
docker rm redis-stack-server
```

### Redis CLI 操作

```powershell
# 進入 Redis CLI 互動模式
docker exec -it redis-stack-server redis-cli

# 直接執行 Redis 指令
docker exec redis-stack-server redis-cli SET mykey "Hello Redis"
docker exec redis-stack-server redis-cli GET mykey

# 查看所有鍵
docker exec redis-stack-server redis-cli KEYS "*"

# 清空當前資料庫
docker exec redis-stack-server redis-cli FLUSHDB

# 清空所有資料庫
docker exec redis-stack-server redis-cli FLUSHALL
```

### 效能監控

```powershell
# 即時監控 Redis 指令
docker exec -it redis-stack-server redis-cli MONITOR

# 查看 Redis 統計資訊
docker exec redis-stack-server redis-cli INFO stats

# 查看記憶體使用狀況
docker exec redis-stack-server redis-cli INFO memory
```

## 安全性配置

### 設定密碼保護（生產環境建議）

對於生產環境或需要密碼保護的場景：

#### 1. 停止並移除當前容器

```powershell
docker stop redis-stack-server
docker rm redis-stack-server
```

#### 2. 啟動帶密碼的容器

```powershell
docker run -d --name redis-stack-server -p 6379:6379 -e REDIS_ARGS="--requirepass YourStrongPassword123" redis/redis-stack-server:latest
```

#### 3. 更新專案配置

修改 `appsettings.json` 或環境變數：

```json
"Redis": {
    "Host": "localhost",
    "Password": "YourStrongPassword123",
    "Port": "6379"
}
```

#### 4. 測試帶密碼的連線

```powershell
# 需要提供密碼
docker exec redis-stack-server redis-cli -a YourStrongPassword123 ping
```

### 其他安全性建議

- **限制網路存取**：僅綁定到 localhost（`-p 127.0.0.1:6379:6379`）
- **使用強密碼**：密碼長度至少 16 字元，包含大小寫字母、數字和特殊字元
- **啟用持久化**：定期備份 Redis 資料（RDB 或 AOF）
- **監控連線**：定期檢查 `CLIENT LIST` 避免異常連線

## 故障排除

### 容器無法啟動

**問題**：執行 `docker run` 後容器立即退出

**解決方案**：
```powershell
# 查看容器日誌
docker logs redis-stack-server

# 檢查埠是否被佔用
netstat -ano | findstr :6379

# 使用不同埠啟動
docker run -d --name redis-stack-server -p 6380:6379 redis/redis-stack-server:latest
```

### 無法連線到 Redis

**問題**：應用程式無法連線到 Redis

**檢查清單**：
1. 確認容器正在運行：`docker ps`
2. 確認埠映射正確：`docker port redis-stack-server`
3. 測試 Redis 連線：`docker exec redis-stack-server redis-cli ping`
4. 檢查防火牆設定
5. 確認 `appsettings.json` 中的 `Enabled` 設為 `true`

### 記憶體不足

**問題**：Redis 記憶體使用過高

**解決方案**：
```powershell
# 設定最大記憶體限制（例如 256MB）
docker run -d --name redis-stack-server -p 6379:6379 -e REDIS_ARGS="--maxmemory 256mb --maxmemory-policy allkeys-lru" redis/redis-stack-server:latest
```

### 資料持久化

**問題**：容器重啟後資料遺失

**解決方案**：使用 Volume 掛載資料目錄
```powershell
docker run -d --name redis-stack-server -p 6379:6379 -v redis-data:/data redis/redis-stack-server:latest
```

## 整合到 Docker Compose

如果專案使用 `docker-compose.yml`，可以將 Redis Stack Server 加入：

```yaml
version: '3.8'

services:
  redis:
    image: redis/redis-stack-server:latest
    container_name: redis-stack-server
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    environment:
      - REDIS_ARGS=--requirepass ${REDIS_PASSWORD}
    restart: unless-stopped
    networks:
      - moldplan-network

volumes:
  redis-data:
    driver: local

networks:
  moldplan-network:
    driver: bridge
```

啟動方式：
```powershell
docker-compose up -d redis
```

## 參考資源

- [Redis Stack 官方文件](https://redis.io/docs/stack/)
- [Redis 指令參考](https://redis.io/commands/)
- [StackExchange.Redis 文件](https://stackexchange.github.io/StackExchange.Redis/)
- [專案基礎設施配置](./Infra.md)

## 版本資訊

- **文件建立日期**：2025-11-28
- **Redis Stack Server**：latest
- **適用專案版本**：WayDoSoft.MoldPlan.Backend 1.13.0-beta.6+

---

**注意事項**：
- 本文件適用於本地開發環境，生產環境部署請參考 [Infra.md](./Infra.md) 和 [DOCKER.md](./DOCKER.md)
- Redis 配置可能因專案版本更新而變動，請以最新的 `appsettings.json` 為準