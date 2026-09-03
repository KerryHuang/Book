---
kind: original
---

# SQL Server 查詢伺服器主機上的檔案



## 1. 使用 `xp_cmdshell`

`xp_cmdshell` 是 SQL Server 的一個擴充儲存過程，可以讓你執行作業系統命令（如 `dir`）。預設是關閉的，需要先啟用。

### 啟用 `xp_cmdshell`：

```sql
-- 允許進階選項
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
-- 啟用 xp_cmdshell
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
```

### 查詢本地資料夾檔案（例如查詢 D:\Test 資料夾）：

```sql
EXEC xp_cmdshell 'dir D:\Test';
```

> 查出來的結果會顯示檔名、檔案大小、建立日期等資訊。

------

## 2. 使用 `sys.xp_dirtree`

如果只需要**檔案和目錄清單**，可用 `sys.xp_dirtree`：

```sql
EXEC master.sys.xp_dirtree 'D:\Test', 1, 1;
```

- 第一個參數是資料夾路徑。
- 第二個參數表示要遞迴查詢的層數（1 為只查一層）。
- 第三個參數 1 表示包含檔案（0 只查資料夾）。

------

## 3. 進階 — 將結果寫入暫存表

若你要處理、過濾結果，可用暫存表儲存查詢結果：

```sql
CREATE TABLE #Files (Output NVARCHAR(2000));
INSERT INTO #Files
EXEC xp_cmdshell 'dir D:\Test';
SELECT * FROM #Files WHERE Output LIKE '%.txt';  -- 只查詢 .txt 檔
DROP TABLE #Files;
```

------

## 4. 注意事項

- 必須**有 SQL Server 的管理權限**才可執行 `xp_cmdshell`。
- `xp_cmdshell` 有資安風險，生產環境要特別注意權限控管。
- 查詢的是「SQL Server 主機」的檔案，不是你的「用戶端電腦」。