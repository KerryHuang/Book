---
kind: original
---

# 第二章 docker-compose 教學

## 安裝RabbitMQ

要在 Windows 上使用 Docker 建立 RabbitMQ 服務，根據你提供的 `docker-compose.yml` 內容，可以依照以下步驟操作：

1. **建立 `docker-compose.yml` 檔案**： 首先，在你的專案資料夾（或任何你想要的位置）建立一個 `docker-compose.yml` 檔案，並貼上你提供的內容：

   ```yaml
   version: '3.8'
   services:
     rabbitmq:
       container_name: rabbitmq.3
       image: "rabbitmq:3-management"
       ports:
         - "5672:5672"   # RabbitMQ 主要連接埠
         - "15672:15672" # 管理介面連接埠
       environment:
         RABBITMQ_DEFAULT_USER: guest
         RABBITMQ_DEFAULT_PASS: guest
   ```

2. **在該資料夾開啟命令提示字元 (CMD) 或 PowerShell**： 使用 `cd` 指令移動到 `docker-compose.yml` 所在的資料夾。

3. **啟動 RabbitMQ 服務**： 執行以下指令來啟動服務：

   ```bash
   docker-compose up -d
   ```

   `-d` 參數表示以背景模式執行，這樣可以讓你繼續使用命令提示字元。

4. **確認 RabbitMQ 是否啟動成功**： 可以使用以下指令檢查 RabbitMQ 的執行狀態：

   ```bash
   docker ps
   ```

   你應該會看到一個名為 `rabbitmq.3` 的容器正在執行。

5. **訪問管理介面**： 開啟瀏覽器並輸入 `http://localhost:15672`，使用預設的帳號和密碼（`guest/guest`）登入管理介面。

這樣就完成了 RabbitMQ 容器的設定！

---

### **基礎指令**

1. **`docker-compose up`**

   - 啟動並運行服務（根據 `docker-compose.yml` 文件）。

   - 常用參數：

     - `-d`：在後台運行容器。
     - `--build`：在啟動服務之前重新構建映像。
     - `--force-recreate`：即使配置沒有更改，也強制重新創建容器。

   - 範例：

     ```bash
     docker-compose up
     docker-compose up -d --build
     ```
     
     然後運行時指定 `.env` 文件：
     
     ```bash
     docker-compose --env-file .env up -d --build
     ```

2. **`docker-compose down`**

   - 停止並移除服務容器、網路和掛載的卷。

   - 常用參數：

     - `--volumes`：同時移除數據卷。
     - `--rmi all`：移除與服務相關的所有映像。

   - 範例：

     ```bash
     docker-compose down --volumes
     ```

3. **`docker-compose build`**

   - 構建服務定義的映像。

   - 常用參數：

     - `--no-cache`：忽略緩存，重新構建映像。
     - `--pull`：始終拉取最新的基礎映像。

   - 範例：

     ```bash
     docker-compose build --no-cache
     ```

4. **`docker-compose start`**

   - 啟動已停止的容器。

   - 範例：

     ```bash
     docker-compose start
     ```

5. **`docker-compose stop`**

   - 停止運行中的容器。

   - 範例：

     ```bash
     docker-compose stop
     ```

6. **`docker-compose restart`**

   - 重新啟動服務容器。

   - 範例

     ：

     ```bash
     docker-compose restart
     ```

------

### **容器操作指令**

1. **`docker-compose ps`**

   - 列出服務容器的狀態。

   - 範例

     ：

     ```bash
     docker-compose ps
     ```

2. **`docker-compose logs`**

   - 查看容器日誌。

   - 常用參數：

     - `-f`：實時查看日誌。
     - `--tail=N`：顯示最近 N 行日誌。

   - 範例：

     ```bash
     docker-compose logs -f
     ```

3. **`docker-compose exec`**

   - 在運行中的容器內執行指令。

   - 範例：

     ```bash
     docker-compose exec service_name bash
     ```

4. **`docker-compose run`**

   - 執行臨時容器來執行指令。

   - 範例：

     ```bash
     docker-compose run service_name command
     ```

------

### **管理與除錯指令**

1. **`docker-compose config`**

   - 驗證並檢查 `docker-compose.yml` 文件的配置。

   - 常用參數：

     - `--services`：僅顯示服務名稱。
     - `--volumes`：顯示卷的定義。

   - 範例：

     ```bash
     docker-compose config --services
     ```

2. **`docker-compose images`**

   - 列出服務使用的映像。

   - 範例：

     ```bash
     docker-compose images
     ```

3. **`docker-compose top`**

   - 顯示容器中的運行進程。

   - 範例：

     ```bash
     docker-compose top
     ```

------

### **清理指令**

1. **`docker-compose rm`**

   - 移除已停止的容器。

   - 常用參數：

     - `-f`：強制移除。
     - `-v`：移除與容器關聯的卷。

   - 範例：

     ```bash
     docker-compose rm -f
     ```

2. **`docker-compose prune`**

   - 刪除未使用的卷和網路（需要確認）。

   - 範例：

     ```bash
     docker-compose prune
     ```

------

### **開發相關指令**

1. **`docker-compose pause`**

   - 暫停服務容器。

   - 範例：

     ```bash
     docker-compose pause
     ```

2. **`docker-compose unpause`**

   - 恢復已暫停的服務容器。

   - 範例：

     ```bash
     docker-compose unpause
     ```

3. **`docker-compose scale`**

   - 調整服務的容器數量。

   - 範例：

     ```bash
     docker-compose scale web=3
     ```

------

### **進階指令**

1. **`docker-compose version`**

   - 顯示 Docker Compose 的版本資訊。

   - 範例：

     ```bash
     docker-compose version
     ```

2. **`docker-compose help`**

   - 顯示幫助資訊及所有指令清單。

   - 範例：

     ```bash
     docker-compose help
     ```

------
