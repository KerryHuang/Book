---
kind: original
---

# 使用 **Entity Framework Core (EF Core)** 的 Migrations 功能進行版本控制



## **1. 啟動點：現有資料庫**

假設你已經有一個現有的資料庫，並希望使用 EF Core 的 Migrations 來管理後續變更。

------

## **2. 安裝必要的套件**

確保你的專案已安裝以下 EF Core 的必要套件：

```bash
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Design
```

針對其他資料庫（如 MySQL、PostgreSQL），請安裝相應的 EF Core 提供者套件。

------

## **3. 生成模型：`Scaffold-DbContext`**

使用 EF Core 的反向工程功能（`Scaffold-DbContext`）來生成基於現有資料庫的實體模型和 `DbContext` 類。

執行以下指令：

```bash
dotnet ef dbcontext scaffold "Server=localhost;Database=YourDatabase;User Id=sa;Password=YourPassword;" Microsoft.EntityFrameworkCore.SqlServer -o Models
```

- **`-o Models`**：生成的實體類會存放在 `Models` 資料夾中。
- **`Microsoft.EntityFrameworkCore.SqlServer`**：指定資料庫提供者，對於 SQL Server 使用此選項。

### **選擇性參數**

- **`-t TableName`**：僅生成特定資料表的模型。
- **`--schema SchemaName`**：指定特定架構。
- **`--context-dir DirectoryName`**：將 `DbContext` 類別存放於指定資料夾中。
- **`--context ContextName`**：指定生成的 `DbContext` 類別名稱。

------

## **4. 將現有資料庫設定為初始狀態**

要讓 EF Core 知道你的現有資料庫結構是 Migrations 的初始狀態，執行以下操作：

1. **新增初始 Migration** 在專案中執行以下指令：

   ```bash
   dotnet ef migrations add InitialCreate
   ```

2. **移除 `Up()` 和 `Down()` 中的程式碼** 打開剛生成的 `InitialCreate` Migration 檔案，移除 `Up()` 和 `Down()` 方法中的內容，避免重新建立已存在的資料庫結構。

   範例：

   ```csharp
   protected override void Up(MigrationBuilder migrationBuilder)
   {
       // 保留空白
   }
   
   protected override void Down(MigrationBuilder migrationBuilder)
   {
       // 保留空白
   }
   ```

3. **更新資料庫版本記錄** 執行以下指令將這個空的 Migration 應用到資料庫，EF Core 將記錄這個版本：

   ```bash
   dotnet ef database update
   ```

------

## **5. 進行後續變更**

現在你的資料庫已經與 EF Core Migrations 同步，接下來可以使用 Migrations 來管理變更。

### **新增新的變更**

例如，為 `Company` 表新增欄位：

1. 更新模型：

   ```csharp
   public class Company
   {
       public int Id { get; set; }
       public string Name { get; set; }
       public string Address { get; set; }
       public string PhoneNumber { get; set; } // 新增欄位
   }
   ```

2. 生成新的 Migration：

   ```bash
   dotnet ef migrations add AddPhoneNumberToCompany
   ```
   
   生成 Migrations 執行以下指令，生成資料庫結構變更的 SQL 指令碼(選擇)
   
   ```bash
   dotnet ef migrations script -o Migrations.sql
   ```

3. 更新資料庫：

   ```bash
   dotnet ef database update
   ```

------

## **6. Migrations 操作完整範例**

以下為一個典型的操作流程：

1. **生成模型與 DbContext**

   ```bash
   dotnet ef dbcontext scaffold "YourConnectionString" Microsoft.EntityFrameworkCore.SqlServer -o Models
   ```

2. **新增初始 Migration**

   ```bash
   dotnet ef migrations add InitialCreate
   ```

3. **應用初始 Migration**

   ```bash
   dotnet ef database update
   ```

4. **新增結構變更**

   - 更新模型。

   - 執行：

     ```bash
     dotnet ef migrations add AddNewChanges
     dotnet ef database update
     ```

------

## **7. 注意事項**

1. **Migration 歷史表**
   EF Core 會在資料庫中建立 `__EFMigrationsHistory` 表來記錄已應用的 Migrations。如果此表已存在，請確保它的內容正確。
2. **現有資料表命名規範**
   EF Core 預設會使用資料表名稱作為模型名稱。如果你的資料表命名不符合 C# 的命名慣例，可能需要手動調整模型。
3. **變更時的資料遺失風險**
   小心設計 Migrations 中的 `Down()` 方法，避免回滾操作導致資料遺失。