---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/NLogExample_Advanced
author: CI-YU
---

# .NET 6 NLog進階範例

### 目的

- 在寫nlog.config檔案時覺得怎麼有點複雜，我只是需要簡單的設定檔就好了，最後決定透過appsetting來做設定
- 將log文件採用非同步寫入，可大幅提升效能

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/194093796-6556bde2-e061-4e23-8e1c-9f6313c44dbb.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 4.NuGet加入套件

- NLog
- NLog.Web.AspNetCore

![範例4-1](https://user-images.githubusercontent.com/19286751/194094083-38142c61-25c5-4a6b-9634-23bb8f8f0993.png)

### 編輯Program.cs檔

```C#
using NLog;
using NLog.Web;
//初始化NLog
var logger = LogManager.Setup()
  //載入Configuration並且讀取appsetting來使用
  .LoadConfigurationFromAppSettings()
  .GetCurrentClassLogger();
try {
  logger.Debug("init main");
  var builder = WebApplication.CreateBuilder(args);

  // Add services to the container.
  builder.Logging.ClearProviders();
  builder.Host.UseNLog();
  builder.Services.AddControllers();
  // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
  builder.Services.AddEndpointsApiExplorer();
  builder.Services.AddSwaggerGen();
  //以下省略
```

![範例5-1](https://user-images.githubusercontent.com/19286751/194096153-4bbb2f1a-77c1-4ca3-b0f3-e4e306547ca1.png)

### 編輯appsetting.json

設定NLog，包含

- throwConfigExceptions:設定檔錯誤時會跳exception
- 使用非同步方式寫入檔案
- targets:設定輸出的格式，例如txt檔案或是Console顯示
- rules:什麼情況要做什麼動作，例如log名稱為Microsoft.AspNetCore最小等級是warn時寫到Console

|         | ILogger     | NLog     |
| ------- | ----------- | -------- |
| Level 0 | Trace       | Trace    |
| Level 1 | Debug       | Debug    |
| Level 2 | Information | Info     |
| Level 3 | Warning     | Warn     |
| Level 4 | Error       | Error    |
| Level 5 | Critical    | Fatal    |
| Level 6 | None        | NLog沒有 |

```json
{
  "NLog": {
    "throwConfigExceptions": true,
    "targets": {
      "async": true,
      "logfile": {
        "type": "File",
        "fileName": "c:/temp/nlog-${shortdate}.txt"
      },
      "logconsole": {
        "type": "Console"
      }
    },
    "rules": [
      {
        "logger": "Microsoft.AspNetCore",
        "minLevel": "Warn",
        "writeTo": "logconsole"
      },
      {
        "logger": "*",
        "minLevel": "Info",
        "writeTo": "logfile"
      }
    ]
  }
}
```

![範例6-1](https://user-images.githubusercontent.com/19286751/194105847-3d9f6f9b-17ef-4f0b-b62b-dc1fc0aa9bb5.png)

### 編輯WeatherForecastController.cs類別檔

```C#
    [HttpGet(Name = "GetWeatherForecast")]
    public IEnumerable<WeatherForecast> Get() {
      //新增一個類型
      var StudentObject = new Student() { Id = 4, Name = "Bill", Age = 20 };
      //新增一個匿名類型
      var position = new { Latitude = 25, Longitude = 134 };
      //寫log等級為error的log，當需要紀錄物件時需要透過{@該物件}來表示
      _logger.LogError("Error Value: {@StudentObject}", StudentObject);
      _logger.LogError("Error Value: {@position}", position);
      return Enumerable.Range(1, 5).Select(index => new WeatherForecast {
        Date = DateTime.Now.AddDays(index),
        TemperatureC = Random.Shared.Next(-20, 55),
        Summary = Summaries[Random.Shared.Next(Summaries.Length)]
      })
      .ToArray();
    }
    public class Student {
      public int Id { get; set; }
      public string Name { get; set; }
      public int Age { get; set; }
    }
```

![範例7-1](https://user-images.githubusercontent.com/19286751/193857997-53a93aa7-ce6d-49da-b76b-c583ecb24772.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果
![範例8-1](https://user-images.githubusercontent.com/19286751/194106724-ad00b505-a21a-428c-9c69-992569d5af76.png)

![範例8-2](https://user-images.githubusercontent.com/19286751/194106895-19e08b46-04dc-47f8-a52b-871fceeabddd.png)

執行後查看log檔案，這次寫到C:\temp底下
![範例8-3](https://user-images.githubusercontent.com/19286751/194107246-342e213e-dbc3-4fca-8eb1-d6067907ef88.png)

- 第一個紅框處顯示物件內容
- 第二個紅框處顯示使用Get請求呼叫了WeatherForecast回傳狀態碼200用了54.3ms的時間
![範例8-4](https://user-images.githubusercontent.com/19286751/194107583-5e9a9d48-ee96-4b69-9b4f-a23abe82aeca.png)

### 結論

最後其實會發現Serilog相對來說比較容易使用，也建議使用serilog

### 參考

[黑暗執行緒](https://blog.darkthread.net/blog/high-capacity-dotnet-logging-survey/) [中文輸出為unicode問題](https://www.codeprj.com/zh/blog/a1a69f1.html) [target參數中文解說](https://www.codeprj.com/zh/blog/e597ce1.html) [非同步使用方式與縮寫](https://github.com/nlog/NLog/wiki/AsyncWrapper-target)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/NLogExample_Advanced)