---
kind: original
---

# Serilog

**Serilog** 是一個 .NET 平台上強大的日誌紀錄框架。它提供了結構化日誌記錄功能，使得日誌的資料更加結構化和有意義，便於在不同環境中進行搜尋、篩選和分析。Serilog 支援多種目標（稱為“接收器”，如檔案、資料庫、控制台、遠端伺服器等）來儲存日誌，並且能夠自訂輸出格式，滿足不同的日誌需求。

### Serilog 的特色

1. **結構化日誌**：使用結構化數據記錄（例如 JSON 格式），便於分析和篩選。
2. **靈活的接收器**：支援多種接收器，例如控制台、檔案、資料庫、Elasticsearch 等。
3. **支援多種日誌等級**：Trace、Debug、Information、Warning、Error、Fatal 等等。
4. **可擴充性**：可以通過自訂接收器和格式來滿足不同的日誌需求。

### 安裝 Serilog

在 .NET 中可以通過 NuGet 安裝 Serilog 及其常用接收器。以控制台和檔案接收器為例：

```shell
dotnet add package Serilog
dotnet add package Serilog.Sinks.Console
dotnet add package Serilog.Sinks.File
```

### 基本使用範例

以下是一個使用 Serilog 寫入日誌的範例程式碼。

#### 1. 基本設定與日誌寫入

這個範例會將日誌寫入控制台。

```csharp
using System;
using Serilog;

class Program
{
    static void Main()
    {
        // 基本設定，將日誌寫入控制台
        Log.Logger = new LoggerConfiguration()
            .MinimumLevel.Debug()
            .WriteTo.Console()
            .CreateLogger();

        // 寫入不同等級的日誌
        Log.Information("這是一則資訊日誌。");
        Log.Warning("這是一則警告日誌。");
        Log.Error("這是一則錯誤日誌。");

        // 結束前呼叫
        Log.CloseAndFlush();
    }
}
```

#### 2. 使用結構化日誌

Serilog 支援在日誌中插入結構化數據，便於日後分析。例如，可以傳入具名參數來添加資料。

```csharp
Log.Information("使用者 {User} 在 {Time} 登入系統", "Alice", DateTime.Now);
```

這樣的結構化日誌會顯示為：

```yaml
使用者 Alice 在 2024-11-04 10:30:00 登入系統
```

日誌框架可以識別 `{User}` 和 `{Time}` 作為鍵值，方便搜尋和篩選。

#### 3. 將日誌寫入檔案

要將日誌輸出到檔案，可以加入 `File` 接收器：

```csharp
using Serilog;

Log.Logger = new LoggerConfiguration()
    .WriteTo.File("logs/log.txt", rollingInterval: RollingInterval.Day)
    .CreateLogger();

Log.Information("這是一則記錄到檔案的日誌。");
Log.CloseAndFlush();
```

此設定會在 `logs` 資料夾下建立 `log.txt` 檔案，並依日期自動分檔。

### 配合 .NET ASP.NET Core 使用

在 ASP.NET Core 中，通常會在 `Program.cs` 或 `appsettings.json` 中設定 Serilog：

#### 1. `Program.cs` 中的設定範例

```csharp
using Serilog;

public class Program
{
    public static void Main(string[] args)
    {
        Log.Logger = new LoggerConfiguration()
            .ReadFrom.Configuration(configuration) // 讀取 appsettings.json 設定
            .Enrich.FromLogContext()
            .WriteTo.Console()
            .CreateLogger();

        try
        {
            Log.Information("啟動應用程式");
            CreateHostBuilder(args).Build().Run();
        }
        catch (Exception ex)
        {
            Log.Fatal(ex, "應用程式啟動失敗");
        }
        finally
        {
            Log.CloseAndFlush();
        }
    }

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .UseSerilog() // 使用 Serilog 作為日誌紀錄
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
            });
}
```

#### 2. 在 `appsettings.json` 中配置 Serilog

可以在 `appsettings.json` 中設置日誌紀錄的細節，例如輸出到控制台和檔案：

```json
{
  "Serilog": {
    "MinimumLevel": "Debug",
    "WriteTo": [
      { "Name": "Console" },
      {
        "Name": "File",
        "Args": {
          "path": "logs/log.txt",
          "rollingInterval": "Day"
        }
      }
    ]
  }
}
```

### 常見接收器

- **Console**：輸出到控制台。
- **File**：寫入到檔案，支援滾動檔案（如每天新建一個檔案）。
- **Seq**：支援寫入到 Seq 日誌伺服器。
- **Elasticsearch**：整合到 ELK 堆疊，用於日誌分析。
- **SQL Server**：將日誌寫入 SQL 資料庫。

### 結論

Serilog 是 .NET 開發中非常靈活且強大的日誌紀錄框架。透過結構化日誌和多樣化的接收器支援，開發者能更有效地管理和分析日誌，使得應用程式的維護和調試更加容易。