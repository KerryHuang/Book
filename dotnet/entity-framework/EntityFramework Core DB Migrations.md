---
kind: original
---

# EntityFramework Core DB Migrations

### **說明**

1. **傳遞參數 `-a`**

   - 程式透過 `args` 接收第一個參數，並根據值執行對應的資料庫操作。
   - 支援的參數：
     - **`C`**：創建資料庫。
     - **`D`**：刪除資料庫。
     - **`M`**：執行遷移。
   
1. Migration

   ```
   dotnet ef migrations add <Migration Name> --startup-project 03.Presentation/WayDoSoft.MoldPlan.DbMigration --project 01.Core/WayDoSoft.MoldPlan.Domain
   ```
   
   

---

### **執行指令範例**

#### **1. 創建資料庫**

執行以下命令：

```bash
dotnet run -- -a C
```

輸出：

```
Creating the database...
Database created successfully.
Operation completed.
```

#### **2. 刪除資料庫**

執行以下命令：

```bash
dotnet run -- -a D
```

輸出：

```
Deleting the database...
Database deleted successfully.
Operation completed.
```

#### **3. 套用遷移**

執行以下命令：

```bash
dotnet run -- -a M
```

輸出：

```
Applying migrations...
Migrations applied successfully.
Operation completed.
```

#### **4. 提供錯誤參數**

執行以下命令：

```bash
dotnet run -- -a X
```

輸出：

```mathematica
Invalid action. Use C for Create, D for Delete, or M for Migrate.
```

---

# IDesignTimeDbContextFactory 介紹

`IDesignTimeDbContextFactory` 是 Entity Framework Core 提供的一個介面，用於在設計階段生成 `DbContext` 實例，主要被 `dotnet ef` 工具使用。例如，當你執行 `dotnet ef migrations` 或 `dotnet ef database update` 等命令時，EF Core 工具需要一個 `DbContext` 的實例來執行這些操作。

------

## **使用場景**

- **無法自動解析 `DbContext` 的建構邏輯**：當 `DbContext` 的建構函數需要特定參數（如依賴注入或自定義邏輯）時，EF Core 工具可能無法自動初始化它。
- **多個 `DbContext`**：在一個專案中包含多個 `DbContext`，需要指定一個 `DbContext` 來使用時。
- **設計階段特定邏輯**：需要在設計階段（如遷移）執行特定的初始化或設定。

---

## **如何實現和使用 `IDesignTimeDbContextFactory`**

### **1. 創建一個 `DbContext` 的工廠類**

實現 `IDesignTimeDbContextFactory<T>` 介面，並返回 `DbContext` 的實例。

#### **範例**

假設有一個 `AppDbContext` 類：

```csharp
public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        if (!optionsBuilder.IsConfigured)
        {
            optionsBuilder.UseSqlServer("YourDefaultConnectionString");
        }
    }
}
```

實現工廠類：

```csharp
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

public class AppDbContextFactory : IDesignTimeDbContextFactory<AppDbContext>
{
    public AppDbContext CreateDbContext(string[] args)
    {
        var optionsBuilder = new DbContextOptionsBuilder<AppDbContext>();
        optionsBuilder.UseSqlServer("Server=localhost;Database=MyDatabase;User Id=sa;Password=YourPassword;");

        return new AppDbContext(optionsBuilder.Options);
    }
}
```

------

### **2. 使用 `dotnet ef` 工具時的行為**

`dotnet ef` 工具會自動查找並使用實現了 `IDesignTimeDbContextFactory` 的工廠類。如果找到了該工廠，EF Core 會通過 `CreateDbContext` 方法生成 `DbContext` 的實例。

例如：

```bash
dotnet ef migrations add InitialCreate
dotnet ef database update
```

此時，EF Core 會使用 `AppDbContextFactory.CreateDbContext()` 方法來創建 `AppDbContext` 的實例。

------

### **3. 使用參數化連接字串或配置檔**

如果需要從配置檔中動態加載連接字串，可以在 `CreateDbContext` 方法中使用：

#### **改進範例**

```csharp
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;

public class AppDbContextFactory : IDesignTimeDbContextFactory<AppDbContext>
{
    public AppDbContext CreateDbContext(string[] args)
    {
        // 讀取 appsettings.json 配置檔
        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json")
            .Build();

        var connectionString = configuration.GetConnectionString("DefaultConnection");

        var optionsBuilder = new DbContextOptionsBuilder<AppDbContext>();
        optionsBuilder.UseSqlServer(connectionString);

        return new AppDbContext(optionsBuilder.Options);
    }
}
```

---

## **注意事項**

1. **設計階段和運行時的區別**：
   - `IDesignTimeDbContextFactory` 的作用僅限於設計階段（如使用 `dotnet ef` 命令時），並不影響應用程式在運行時的 `DbContext` 初始化。
   - 運行時的 `DbContext` 應通過依賴注入配置。
2. **多個工廠類**：
   - 如果有多個 `IDesignTimeDbContextFactory` 的實現，EF Core 工具會根據需要自動選擇正確的工廠類。
   - 若出現衝突，可以在 `CreateDbContext` 中根據條件進行過濾。
3. **不使用 `IDesignTimeDbContextFactory` 時的行為**： 如果沒有定義 `IDesignTimeDbContextFactory`，EF Core 工具會嘗試從應用程式的依賴注入容器中解析 `DbContext`。