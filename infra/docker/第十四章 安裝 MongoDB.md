---
kind: original
---

# Docker 安裝 MongoDB 教學

## 1. 前言介紹

MongoDB 是一個流行的 NoSQL 資料庫，廣泛用於大數據、IoT、即時分析等現代應用場景。利用 Docker，可以快速建立 MongoDB 容器環境，方便開發、測試與部署。

------

## 2. 環境需求

- 已安裝 Docker (適用 Windows、macOS、Linux)
- 基本 Command Line 操作能力

------

## 3. 拉取 MongoDB Docker 映像檔

```bash
# 適用於 Windows PowerShell、Mac/Linux Terminal
docker pull mongo
```

------

## 4. 建立 MongoDB 容器

### （1）一般啟動範例

```bash
# 適用於 Windows PowerShell、Mac/Linux Terminal
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
  -e MONGO_INITDB_ROOT_PASSWORD=secret123 \
  mongo
```

------

## 5. 資料持久化 (可選)

### （1）Mac / Linux 指令

```bash
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
  -e MONGO_INITDB_ROOT_PASSWORD=secret123 \
  -v ~/mongo-data:/data/db \
  mongo
```

- `~/mongo-data` 是你家目錄下的 mongo-data 資料夾

### （2）Windows 指令

```powershell
docker run -d `
  --name mongodb `
  --restart=always `
  -p 27017:27017 `
  -e MONGO_INITDB_ROOT_USERNAME=mongoadmin `
  -e MONGO_INITDB_ROOT_PASSWORD=secret123 `
  -v E:\Database\mongo-data:/data/db `
  mongo
```

- 反引號 (`) PowerShell 用於換行，也可寫成單行

------

## 6. 連線測試

### (1) 使用 mongo shell

```bash
docker exec -it mongodb mongosh -u mongoadmin -p secret123
```

### (2) 使用 MongoDB GUI (如 Compass)

連線字串：

```perl
mongodb://mongoadmin:secret123@localhost:27017/
```

------

## 7. 常用指令

- 查看容器狀態

  ```bash
  docker ps -a
  ```

- 停止容器

  ```bash
  docker stop mongodb
  ```

- 啟動容器

  ```bash
  docker start mongodb
  ```

- 刪除容器

  ```bash
  docker rm -f mongodb
  ```

------

## 8. 小結與補充

- 可用 Docker Compose 自動化管理多個服務
- 更多設定請參考 MongoDB 官方 Docker 文件



---

# MongoDB Compass 圖形化操作教學

------

## 1. 安裝 MongoDB Compass

1. 前往 [MongoDB Compass 官方下載頁面](https://www.mongodb.com/try/download/compass)
2. 選擇你的作業系統下載安裝（Windows、macOS、Linux）
3. 安裝完成後啟動 Compass

------

## 2. 連線到本地 MongoDB

1. 開啟 Compass，會看到連線畫面

2. 輸入連線字串（如果是 Docker 預設帳密）：

   ```perl
   mongodb://mongoadmin:secret123@localhost:27017/
   ```

3. 點擊「Connect」按鈕

------

## 3. 建立新的資料庫與集合

1. 點左側「Create Database」按鈕
2. **Database Name** 輸入：`testdb`
3. **Collection Name** 輸入：`users`
4. 按下「Create Database」完成建立

------

## 4. 新增文件（新增一筆資料）

1. 點左側選單展開 `testdb` → 選擇 `users`

2. 右側會出現集合內容，點上方「Insert Document」

3. 直接填寫資料（可修改預設 JSON，例如）：

   ```json
   {
     "name": "Alice",
     "age": 30,
     "email": "alice@example.com"
   }
   ```

4. 點擊「Insert」即可新增

------

## 5. 查詢資料

1. 在 `users` 集合畫面，可以直接看到所有文件

2. 如要條件查詢（搜尋），在上方「Filter」輸入：

   ```json
   { "age": { "$gt": 25 } }
   ```

   按 Enter，即可篩選出年齡大於 25 歲的資料

------

## 6. 編輯資料

1. 點想要編輯的那筆資料右上角的「Edit」按鈕（鉛筆圖示）
2. 修改欄位內容，例如把 age 改成 31
3. 按「Update」即可儲存

------

## 7. 刪除資料

1. 點想要刪除的資料右上角「Delete」按鈕（垃圾桶圖示）
2. 會跳出確認視窗，按「Delete」即可

------

## 8. 新增欄位（欄位動態擴充）

1. 在「Edit」模式下，點「Add Field」
2. 新增欄位名稱與數值，例如 `"phone": "0912-345678"`
3. 儲存後，所有文件欄位可自由變動

------

## 9. 匯入/匯出資料

- 上方功能列有「Import」和「Export」按鈕
- 支援 JSON、CSV 格式資料進出

------

## 10. 小結

- MongoDB Compass 提供直觀操作介面，完全不用寫指令
- 資料欄位可動態增減，結構彈性
- 適合新手入門、原型開發、管理 MongoDB

---



# MongoDB 常用語法教學

------

## 1. 切換（建立）資料庫

```javascript
use mydb
```

- 切換到 mydb 資料庫，如果沒有則自動建立。

------

## 2. 建立集合（Collection）

```javascript
db.createCollection("users")
```

- 建立 users 集合，相當於關聯式資料庫的「資料表」。

------

## 3. 新增資料（Insert）

**單筆新增：**

```javascript
db.users.insertOne({
  name: "Alice",
  age: 28,
  email: "alice@example.com"
})
```

**多筆新增：**

```javascript
db.users.insertMany([
  { name: "Bob", age: 35 },
  { name: "Carol", age: 42 }
])
```

------

## 4. 查詢資料（Find）

**查詢全部：**

```javascript
db.users.find()
```

**條件查詢：**

```javascript
db.users.find({ age: 35 })
```

**進階查詢：**

```javascript
db.users.find({ age: { $gt: 30 } })         // 年齡大於 30
db.users.find({ name: { $regex: /^A/ } })   // 名字以 A 開頭
```

------

## 5. 更新資料（Update）

**更新第一筆符合條件的資料：**

```javascript
db.users.updateOne(
  { name: "Alice" },          // 條件
  { $set: { age: 29 } }       // 要更新的欄位
)
```

**更新多筆資料：**

```javascript
db.users.updateMany(
  { age: { $lt: 30 } },
  { $set: { group: "young" } }
)
```

------

## 6. 刪除資料（Delete）

**刪除第一筆符合條件的資料：**

```javascript
db.users.deleteOne({ name: "Bob" })
```

**刪除多筆資料：**

```javascript
db.users.deleteMany({ age: { $gt: 40 } })
```

------

## 7. 欄位操作

**只查詢部分欄位（投影）：**

```javascript
db.users.find({}, { name: 1, age: 1, _id: 0 })
```

- 只顯示 name 和 age 欄位，不顯示 _id。

**排序與限制：**

```javascript
db.users.find().sort({ age: -1 }).limit(2)
```

- 依 age 由大到小排序，僅取前 2 筆。

------

## 8. 聚合查詢（Aggregation）

**群組統計：**

```javascript
db.users.aggregate([
  { $group: { _id: "$group", count: { $sum: 1 } } }
])
```

- 統計 group 欄位有幾筆資料。

------

## 9. 索引（Index）

**建立索引：**

```javascript
db.users.createIndex({ email: 1 })
```

- 為 email 欄位建立升冪索引，加速查詢。

------

## 10. 常見運算子速查表

| 運算子 | 說明             | 範例                     |
| ------ | ---------------- | ------------------------ |
| $gt    | 大於             | { age: { $gt: 30 } }     |
| $lt    | 小於             | { age: { $lt: 40 } }     |
| $gte   | 大於等於         | { age: { $gte: 25 } }    |
| $lte   | 小於等於         | { age: { $lte: 60 } }    |
| $in    | 包含於陣列中     | { age: { $in: [25,30] }} |
| $set   | 更新或新增欄位   | { $set: { score: 90 } }  |
| $push  | 陣列加入一筆資料 | { $push: { tags: "A" }}  |
| $regex | 正則查詢         | { name: { $regex: /A/ }} |



------

## 11. 其他補充

- **MongoDB 文件（document）本質是 JSON/BSON 格式，欄位可動態增加或刪除。**
- **所有指令都在 db.[collection] 進行操作。**
- **MongoDB 無 schema，可儲存不同結構的資料，但建議同一集合盡量維持一致性。**