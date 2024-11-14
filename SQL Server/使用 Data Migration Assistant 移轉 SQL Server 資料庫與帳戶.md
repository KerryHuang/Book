# 使用 Data Migration Assistant 移轉 SQL Server 資料庫與帳戶

使用 **Data Migration Assistant (DMA)** 將本地 SQL Server 資料庫遷移到 Azure SQL Database，可以有效地遷移資料、結構和帳戶。以下是詳細的教學步驟，包括遷移資料庫和帳戶的完整過程。

### 前置準備

1. **下載並安裝 Data Migration Assistant (DMA)**：
   - 前往 [Microsoft 官方網站](https://www.microsoft.com/en-us/download/details.aspx?id=53595) 下載 Data Migration Assistant，並安裝於本地電腦上。
2. **準備源資料庫**：
   - 確保本地 SQL Server 資料庫的連線正常，並確認您具備管理權限來遷移資料和帳戶。
3. **準備目標 Azure SQL Database**：
   - 在 Azure 入口網站建立目標 Azure SQL Database。
   - 確保有足夠的存取權限和資料庫大小，以容納遷移的資料。

### Step 1：評估源資料庫的相容性

1. **開啟 DMA**：
   - 啟動 Data Migration Assistant 應用程式。
2. **建立新專案**：
   - 點擊 **+ New** 建立新專案。
   - 選擇 **Project type** 為 **Assessment**（評估），並填寫項目名稱。
   - **選擇目標伺服器類型**為 **Azure SQL Database**，然後按 **Create**。
3. **選擇評估的範圍**：
   - 在 `Options` 中選擇 **Database compatibility issues** 和 **Feature parity**。
   - 點選 **Next**，選擇您要評估的 SQL Server 資料庫。
4. **執行評估**：
   - 按下 **Start Assessment** 開始評估。
   - DMA 會生成報告，顯示不相容的功能或需要修改的結構。仔細檢查報告，並在 SQL Server 中解決任何不相容的項目。

### Step 2：建立並執行遷移專案

1. **建立遷移專案**：
   - 返回主畫面，選擇 **+ New** 建立新專案。
   - **選擇專案類型**為 **Migration**（遷移），然後設定項目名稱。
   - **目標伺服器類型**選擇 **Azure SQL Database**，然後點擊 **Create**。
2. **設定遷移範圍**：
   - 在 `Select Source` 中，選擇本地的 SQL Server，輸入伺服器名稱和驗證方式，並選擇要遷移的資料庫。
   - 在 `Select Target` 中，輸入 Azure SQL Database 的伺服器名稱和驗證方式，並選擇目標資料庫。
3. **選擇遷移的資料類型**：
   - 在 `Migration Scope` 中，選擇 **Schema only**、**Data only** 或 **Schema and Data**（通常選擇 `Schema and Data` 以完整遷移結構與數據）。
   - 按 **Next** 開始設定。
4. **選擇資料庫結構與帳戶**：
   - 在 `Select schema objects` 中，選擇要遷移的資料庫結構和帳戶。
   - 若有需要，您也可以自訂要遷移的資料表和物件。
5. **執行遷移**：
   - 點擊 **Start Migration** 開始遷移。
   - DMA 會顯示遷移進度，包括成功和失敗的項目。針對失敗的項目，可以查看錯誤訊息，並在原資料庫進行修正後重新執行遷移。

### Step 3：驗證遷移結果

1. **檢查資料結構和帳戶**：

   - 登入 Azure SQL Database，檢查所有資料表、索引、檢視、儲存程序和帳戶是否已成功遷移。

2. **檢查資料一致性**：

   - 使用查詢工具（如 SQL Server Management Studio 或 Azure Data Studio），在源資料庫和 Azure SQL Database 進行數據比對，確認資料一致性。

3. **建立新帳戶**

   - 在 Azure SQL Database 中，建立新使用者登入及帳號

     ```sql
     Use [master];
     Create Login [username] With Password = 'password'
     
     Use [databasename];
     Create User [username] For Login [username] With DEFAULT_SCHEMA = dbo;
     ```

4. **設定帳戶權限**：

   - 在 Azure SQL Database 中，為遷移過來的帳戶分配適當的權限。例如：

     ```sql
     --ALTER ROLE db_datareader ADD MEMBER [username];
     --ALTER ROLE db_datawriter ADD MEMBER [username];
     ALTER Role db_owner ADD MEMBER [username];
     ```

### Step 4：測試應用程式的連線

1. 更新連線字串：

   - 將應用程式中的連線字串更新為 Azure SQL Database 的連線字串。

2. 驗證應用程式：

   - 在應用程式中執行基本操作，以確認其能夠正常連接並與 Azure SQL Database 互動。

### 常見注意事項

- **相容性**：確保所有不相容的功能在遷移之前得到解決。
- **資料庫大小**：確認目標 Azure SQL Database 的定價層和大小足夠。
- **安全性**：設定防火牆規則允許公司 IP 存取 Azure SQL Database。

### 參考文件

[使用 Data Migration Assistant 移轉 SQL Server 資料庫與帳戶](https://jeffprogrammer.wordpress.com/2020/01/02/使用-data-migration-assistant-移轉-sql-server-資料庫與帳戶/)