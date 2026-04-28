# 從 SQL Server 2008 升級至 Azure SQL 的完整指南

本文件說明如何將 SQL Server 2008 (含 2008 R2) 的資料庫升級與遷移至 Azure SQL，包括 Azure SQL Database 與 Azure SQL Managed Instance（MI）。

------

# 1. 升級前評估

SQL Server 2008 與 Azure SQL Database 之間存在 **重大差異**，包括：

### 不支援的項目

- SQL Server Agent（Azure SQL Database 不支援）
- CLR（部分限制）
- Cross-database query 限制
- USE database 指令
- Linked Server
- FileStream / FileTables
- XP_CMDSHELL
- Service Broker（僅 Managed Instance 支援）
- SQL Server Logins → 需要重建

### 資料庫相容性層級

2008 的 Compatibility Level 為 **100**，Azure SQL 最低要求 **100（仍支援）**，但建議升級至 **150 或 160**。

------

# 2. 遷移至 Azure 的三種方式

| 方法                                   | 支援性             | 適合環境                   | 風險 | 推薦  |
| -------------------------------------- | ------------------ | -------------------------- | ---- | ----- |
| **(A) Azure DMS（資料遷移服務）**      | 完整支援           | 最佳方法，可在線或離線遷移 | 低   | ⭐⭐⭐⭐⭐ |
| **(B) BACPAC（匯出為 .bacpac）**       | 支援，但有格式限制 | 小型資料庫                 | 中   | ⭐⭐    |
| **(C) Data Migration Assistant (DMA)** | 兼具評估與匯入     | 有些限制                   | 中   | ⭐⭐⭐   |

結論：
 **優先選 A（Azure Data Migration Service） → 官方推薦、企業級、安全可靠。**

------

# 3. 使用 Azure DMS 遷移（最推薦）

以下為最完整、最穩定的遷移方式。

------

## 3.1 前置作業

### (1) 下載工具：Data Migration Assistant (DMA)

https://learn.microsoft.com/sql/dma/dma-overview

用來檢查：

- Schema 是否相容 Azure SQL
- T-SQL 是否不支援
- 是否需要改寫 Stored Procedure/Trigger

執行時選擇：

```
Assessment → SQL Server → Azure SQL Database
```

### (2) 建立 Azure SQL 資源

可選：

- Azure SQL Database（最常用）
- Azure SQL Managed Instance（較貼近 SQL Server）

### (3) 開啟防火牆

在 Azure SQL 的 "Firewall Rule" 新增：

- SQL Server 2008 的 IP
- DMS 服務的 IP（如果使用 Integration Runtime）

------

## 3.2 建立 Azure DMS 資料遷移專案

1. 在 Azure 入口網站搜尋 **Azure Database Migration Service**
2. 建立新的 Migration Project
3. 選擇來源：
   - **SQL Server**（2008）
4. 選擇目的地：
   - **Azure SQL Database** 或 **Azure SQL MI**
5. 選擇遷移模式：
   - **Offline migration（停機可接受）**
   - **Online migration（低停機）**

------

## 3.3 離線遷移流程（Offline Migration）

```
停機時間短、適合中小型資料庫
```

步驟：

### (1) 建立 .bak 或直接從本機連線

不需先匯出 BACPAC。

### (2) DMS 自動執行資料搬移

包括：

- Schema
- Index
- Data
- Constraint
- View
- Stored Procedure

### (3) 遷移完成後停機切換

手動切換應用程式 Connection String 至 Azure SQL。

------

## 3.4 線上遷移流程（Online Migration）

```
近乎零停機、高可用需求建議使用
```

Azure DMS 會自動：

- 建立 CDC（Change Data Capture）
- 持續同步資料變動
- 最後只需短暫停機進行 Cutover

------

# 4. 使用 BACPAC 遷移（次佳方式）

適合資料庫較小（< 200GB）、Schema 少複雜者。

## 步驟：

### 4.1 匯出 BACPAC

```
右鍵資料庫 → Tasks → Export Data-tier Application
```

### 4.2 上傳至 Azure Storage

### 4.3 在 Azure SQL 匯入 BACPAC

Azure Portal → Import database

------

# 5. 使用 DMA + BACPAC 混合遷移

流程如下：

1. 使用 **DMA Assessment** → 檢查相容性問題
2. 使用 **DMA Migration** → 將 Schema 遷移至 Azure SQL
3. 再使用 BACPAC → 匯入資料

適合：

- Schema 複雜但資料量小
- 部分 T-SQL 不相容需人工修正

------

# 6. 遷移後檢查與調整

## 6.1 設定 Compatibility Level

Azure SQL 預設可能仍保留 100（相容 2008）

建議設定為：

```
ALTER DATABASE YourDB
SET COMPATIBILITY_LEVEL = 150;  -- SQL 2019 level
```

或 Azure 最新：

```
ALTER DATABASE YourDB
SET COMPATIBILITY_LEVEL = 160;  -- SQL 2022
```

------

## 6.2 更新統計資料

```
EXEC sp_updatestats;
```

## 6.3 檢查資料完整性

```
DBCC CHECKDB;
```

------

# 7. 遷移後常見問題（FAQ）

### Q1：SQL Server Agent 工作怎麼辦？

Azure SQL Database 不支援
 → 使用 **Azure Automation** 或 **Elastic Job Agent**。

### Q2：跨資料庫查詢？

Azure SQL Database 不支援 `USE DB`，可用：

```
SELECT * FROM [database].[schema].[table]
```

### Q3：Login / User 會一起搬過去嗎？

不會。

Login 需重新建立：

```
CREATE LOGIN loginname WITH PASSWORD = 'StrongPwd#123';
```

### Q4：FileStream / SQLCLR?

- Azure SQL Database 不支援
- Azure SQL MI 支援大部份功能

### Q5：遷移後效能變差？

需重新建立：

- 統計資料
- 索引
   並調整 DTU / vCore 設定。

------

# 8. 建議的升級流程（最佳實務）

1. **在 SQL Server 2008 執行 DMA Assessment**
2. 修正不相容的 Stored Procedure / Trigger / Cursor
3. 建立 Azure SQL
4. 使用 **Azure DMS 線上遷移（Online Migration）**
5. 切換 Connection String
6. 升級 Compatibility Level
7. 更新統計資料 + 重建索引
8. 完整驗證應用程式