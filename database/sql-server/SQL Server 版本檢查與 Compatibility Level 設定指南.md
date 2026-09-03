---
kind: original
---

- # SQL Server 版本檢查、Compatibility Level 設定與版本升級指南

  本文件包含：

  - SQL Server 版本查詢方式
  - Compatibility Level 對照與設定方式
  - EF Core 支援版本
  - 從 SQL Server 2008 升級到 SQL Server 2022 的完整流程
  - `.bak` 還原後 Compatibility Level 不會更新的處理方式

  ------

  ## 1. 查詢 SQL Server 版本

  ### 1.1 使用 `@@VERSION`

  ```
  SELECT @@VERSION;
  ```

  ### 1.2 使用 `SERVERPROPERTY`

  ```
  SELECT 
      SERVERPROPERTY('ProductVersion') AS ProductVersion,
      SERVERPROPERTY('ProductLevel') AS ProductLevel,
      SERVERPROPERTY('Edition') AS Edition,
      SERVERPROPERTY('EngineEdition') AS EngineEdition,
      SERVERPROPERTY('ProductMajorVersion') AS MajorVersion;
  ```

  ------

  ## 2. Compatibility Level（相容性層級）

  ### 2.1 Compatibility Level 對照表

  | Compatibility Level | SQL Server 版本           |
  | ------------------- | ------------------------- |
  | 100                 | SQL Server 2008 / 2008 R2 |
  | 110                 | SQL Server 2012           |
  | 120                 | SQL Server 2014           |
  | 130                 | SQL Server 2016           |
  | 140                 | SQL Server 2017           |
  | 150                 | SQL Server 2019           |
  | 160                 | SQL Server 2022           |

  ------

  ## 3. 查詢 Compatibility Level

  ### 3.1 所有資料庫

  ```
  SELECT 
      name AS DatabaseName,
      compatibility_level
  FROM sys.databases;
  ```

  ### 3.2 指定資料庫

  ```
  SELECT compatibility_level 
  FROM sys.databases 
  WHERE name = 'YourDatabaseName';
  ```

  ------

  ## 4. 設定 Compatibility Level

  ### 設為 SQL Server 2019 (150)

  ```
  ALTER DATABASE YourDatabaseName 
  SET COMPATIBILITY_LEVEL = 150;
  ```

  ### 設為 SQL Server 2022 (160)

  ```
  ALTER DATABASE YourDatabaseName 
  SET COMPATIBILITY_LEVEL = 160;
  ```

  ------

  # 5. SQL Server 與 EF Core 支援版本對照

  | EF Core 版本         | 支援之 SQL Server | 說明                         |
  | -------------------- | ----------------- | ---------------------------- |
  | EF Core 2.x          | SQL 2008+         | 建議至少 SQL 2012            |
  | EF Core 3.x          | SQL 2012+         | 需使用 System.Data.SqlClient |
  | EF Core 5.x          | SQL 2012+         | .NET 5                       |
  | EF Core 6.x (LTS)    | SQL 2012+         | .NET 6                       |
  | EF Core 7.x          | SQL 2012+         | 最佳效能                     |
  | EF Core 8.x (.NET 8) | SQL 2012+         | 建議 SQL 2016+               |
  | EF Core 9.x (.NET 9) | SQL 2012+         | 建議 SQL 2017+               |

  ------

  # 6. SQL Server 2008 → SQL Server 2022 升級指南

  SQL Server 2008 已於 2019 年停止支援，建議升級至 SQL Server 2022 以獲得更新功能、效能與安全性。

  此升級方式採用最通用、最安全的方法：
   **使用 .bak 備份還原至新伺服器，並更新 Compatibility Level。**

  ------

  ## 6.1 升級方式總覽

  | 升級方式                            | 支援                                  | 風險   | 建議             |
  | ----------------------------------- | ------------------------------------- | ------ | ---------------- |
  | **直接 In-place Upgrade（舊機器）** | 不支援 2008 → 2022                    | 不可行 | ❌ 不可使用       |
  | **Detach/Attach**                   | 支援，但需注意 FILESTREAM / FILEGROUP | 中     | ⚠️ 不建議         |
  | **使用 `.bak` 備份還原**            | 完全支援                              | 低     | ⭐ **最推薦方式** |
  | **使用 SSIS / DMS（Azure）**        | 可行                                  | 中     | 適合雲端         |

  ------

  # 6.2 使用 `.bak` 還原的完整升級流程

  ## 步驟 1：在 SQL Server 2008 備份資料庫

  ```
  BACKUP DATABASE YourDB
  TO DISK = 'D:\Backup\YourDB_2008.bak'
  WITH INIT, COMPRESSION;
  ```

  ## 步驟 2：將 .bak 檔移至 SQL Server 2022 伺服器

  可透過 SMB / FTP / SCP / 網路分享。

  ## 步驟 3：在 SQL Server 2022 還原

  於 SSMS 或 T-SQL：

  ```
  RESTORE DATABASE YourDB
  FROM DISK = 'D:\Backup\YourDB_2008.bak'
  WITH MOVE 'YourDB' TO 'D:\SQLData\YourDB.mdf',
       MOVE 'YourDB_log' TO 'D:\SQLLog\YourDB_log.ldf',
       REPLACE, RECOVERY;
  ```

  ------

  # 6.3 **重要：還原後 Compatibility Level 不會更新**

  這是 SQL Server 的正常行為。

  **SQL Server 會保留舊版資料庫的 Compatibility Level：**

  例如：

  - 從 SQL Server **2008** 還原 → Compatibility Level 會是 **100**
  - 即使 SQL Server 是 2022，也不會自動變更

  📌 **你必須手動將它升級到 160（SQL Server 2022）**

  ------

  # 6.4 更新 Compatibility Level 至 SQL Server 2022

  ```
  ALTER DATABASE YourDB 
  SET COMPATIBILITY_LEVEL = 160;
  ```

  若你想查確認：

  ```
  SELECT name, compatibility_level 
  FROM sys.databases 
  WHERE name = 'YourDB';
  ```

  ------

  # 6.5 建議執行升級後檢查

  ### 1. 更新所有統計資料

  ```
  EXEC sp_updatestats;
  ```

  ### 2. 檢查損毀（強烈建議）

  ```
  DBCC CHECKDB('YourDB');
  ```

  ### 3. 建議重建索引

  ```
  ALTER INDEX ALL ON YourTableName REBUILD;
  ```

  ------

  # 6.6 建議升級策略

  - 若應用程式很舊 → 升級後建議先使用 **Compatibility Level 110 (SQL 2012)** 運行一段時間
  - 完整測試後再升至 **150 (SQL 2019)** 或 **160 (SQL 2022)**
  - 若是使用 EF Core → 建議至少 130（SQL 2016）

  ------

  # 7. 升級的常見問題

  ### Q1：直接 Attach MDF 會成功嗎？

  可能，但容易遇到：

  - FILESTREAM/FILEGROUP 不相容
  - 2008 → 2022 跨版本太大

  建議避免。

  ### Q2：Compatibility Level 100 會影響 EF Core？

  是的。
   某些 SQL 語法（尤其是 LINQ group by、cross apply）在 100 上會失敗。

  ### Q3：Compatibility Level 必須與版本一致嗎？

  不一定，但 **不要低於 SQL Server 所能支援的最低版本**。