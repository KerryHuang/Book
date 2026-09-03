---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/SerilogExample
author: CI-YU
---

# .NET 6 Serilog範例

### 目的

在webapi專案下使用serilog套件

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/193309315-47457982-a726-42cf-bf0b-4b2b2b8902a3.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Serilog.AspNetCore

![步驟4](https://user-images.githubusercontent.com/19286751/193309762-1a22fc5f-eff8-4418-9622-0eb28e48bee6.png)

### 編輯Program.cs檔

在最外層包一個try catch目的是為了捕捉啟動階段的錯誤

```C#
using Serilog;
using Serilog.Events;

Log.Logger = new LoggerConfiguration()
    //Serilog要寫入的最低等級為Information
    .MinimumLevel.Information()
    //Microsoft.AspNetCore開頭的類別等級為warning
    .MinimumLevel.Override("Microsoft.AspNetCore", LogEventLevel.Warning)
    //寫log到Logs資料夾的log.txt檔案中，並且以天為單位做檔案分割
    .WriteTo.File("./Logs/log.txt", rollingInterval: RollingInterval.Day)
    .CreateLogger();
try {
  Log.Information("Starting web host");
  var builder = WebApplication.CreateBuilder(args);
  builder.Services.AddControllers();
  builder.Services.AddEndpointsApiExplorer();
  builder.Services.AddSwaggerGen();
  //controller可以使用ILogger介面來寫入log紀錄
  builder.Host.UseSerilog();
  var app = builder.Build();
  // Configure the HTTP request pipeline.
  if (app.Environment.IsDevelopment()) {
    app.UseSwagger();
    app.UseSwaggerUI();
  }
  app.UseHttpsRedirection();
  app.UseAuthorization();
  app.MapControllers();
  app.Run();
  return 0;
} catch (Exception ex) {
  Log.Fatal(ex, "Host terminated unexpectedly");
  return 1;
} finally { Log.CloseAndFlush(); }
```

![範例5-1](https://user-images.githubusercontent.com/19286751/193331027-d349cec3-361a-4cbd-be87-787aab6c1a2f.png)

### 編輯WeatherForecastController.cs類別檔

因預設就有注入ILogger，故可以直接使用

> 因微軟內建的介面ILogger等級區分與Serilog不一樣，故提供對照表格

|         | ILogger     | Serilog     |
| ------- | ----------- | ----------- |
| Level 0 | Trace       | Verbose     |
| Level 1 | Debug       | Debug       |
| Level 2 | Information | Information |
| Level 3 | Warning     | Warning     |
| Level 4 | Error       | Error       |
| Level 5 | Critical    | Fatal       |
| Level 6 | None        | Serilog沒有 |

```C#
    private readonly ILogger<WeatherForecastController> _logger;

    public WeatherForecastController(ILogger<WeatherForecastController> logger) {
      _logger = logger;
    }

    [HttpGet(Name = "GetWeatherForecast")]
    public IEnumerable<WeatherForecast> Get() {
      //輸出log
      _logger.LogInformation("This is Controller");
      _logger.LogError("Test Error");
      return Enumerable.Range(1, 5).Select(index => new WeatherForecast {
        Date = DateTime.Now.AddDays(index),
        TemperatureC = Random.Shared.Next(-20, 55),
        Summary = Summaries[Random.Shared.Next(Summaries.Length)]
      })
      .ToArray();
    }
```

![範例6-1](https://user-images.githubusercontent.com/19286751/193327535-dd2753cd-1487-41a7-938e-f6fc0ef760d1.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果
![範例7-1](https://user-images.githubusercontent.com/19286751/193330270-05dfbb9d-6e2b-4546-b439-1bbe1b65c331.png)

![範例7-2](https://user-images.githubusercontent.com/19286751/193330370-b147c0bc-80d5-4114-9e94-b02ab84afa7c.png)

執行後就可以到我們的專案檔路徑下查看Logs資料夾

![範例7-3](https://user-images.githubusercontent.com/19286751/193330529-e67d51d5-1e4b-45e0-a3eb-f87121356439.png)

點進去資料夾後就可以看到以日期為單位的txt檔案

![範例7-4](https://user-images.githubusercontent.com/19286751/193331247-2a517601-18d8-460a-b4fe-83dd85206f3d.png)

### 參考

[余小章](https://dotblogs.com.tw/yc421206/2022/09/04/serilog_config_in_asp_net_core) [Will保哥](https://blog.miniasp.com/post/2021/11/29/How-to-use-Serilog-with-NET-6) [官方文件](https://github.com/serilog/serilog-sinks-file)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/SerilogExample)