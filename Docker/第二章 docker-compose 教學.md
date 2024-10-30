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