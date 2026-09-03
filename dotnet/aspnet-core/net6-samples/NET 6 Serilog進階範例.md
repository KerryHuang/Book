---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/SerilogExample_Advanced
author: CI-YU
---

# .NET 6 Serilog進階範例

### 目的

- 讀取appsetting設定檔
- 二階段初始化
- 為了簡單化故將Log存入SQLite

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/193637579-767f7e66-af55-4f0a-b1c5-593609fe4424.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Serilog.AspNetCore
- Serilog.Sinks.SQLite

![步驟4](https://user-images.githubusercontent.com/19286751/193637871-2beac67d-a315-4bb3-a793-a55b736b1159.png)

### 編輯Program.cs檔

```C#
using Serilog;
 //第一階段初始化
 // var builder = WebApplication.CreateBuilder(args);未使用二階段參數化，builder會跑到try外面
Log.Logger = new LoggerConfiguration()
  //.ReadFrom.Configuration(builder.Configuration)
  .CreateBootstrapLogger();
try {
  var builder = WebApplication.CreateBuilder(args);
  // Add services to the container.

  builder.Services.AddControllers();
  // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
  builder.Services.AddEndpointsApiExplorer();
  builder.Services.AddSwaggerGen();
  //第二階段初始化可以取得appsetting的內容，如不使用第二階段初始化，
  //會需要將 var builder宣告式會移出try(如上方註解處)，就會有風險未捕獲builder的錯誤
  builder.Host.UseSerilog(
      (hostingContext, services, loggerConfiguration) => {
        //使用appsetting
        loggerConfiguration.ReadFrom.Configuration(builder.Configuration);
      });
  var app = builder.Build();

  // Configure the HTTP request pipeline.
  if (app.Environment.IsDevelopment()) {
    app.UseSwagger();
    app.UseSwaggerUI();
  }

  app.UseHttpsRedirection();
  //紀錄每個Request的資料，須注意要放在讀取靜態檔案(app.UseStaticFiles())後面，因為靜態檔案的狀態通常不需要紀錄資訊
  app.UseSerilogRequestLogging();
  //以下省略
```

![範例5-1](https://user-images.githubusercontent.com/19286751/193849408-d444f650-dcee-4a68-a624-e91192e7b044.png)

### 編輯appsetting.json

設定Serilog，包含

- 最低紀錄標準為Information
- Microsoft.AspNetCore開頭類別紀錄標準為Warning
- 寫Log檔到console
- 寫Log檔到File，並請用日期分割檔案
- 寫Log檔到SQLite，資料表名稱為Logs，限制DB最大為1M，預設還有一個參數rollOver為true，當達到限制，就會分割DB

```json
{
  "Serilog": {
    "MinimumLevel": {
      "Default": "Information",
      "Override": {
        "Microsoft.AspNetCore": "Warning"
      }
    },
    "WriteTo": [
      { "Name": "Console" },
      {
        "Name": "File",
        "Args": {
          "path": "./logs/log-.txt",
          "rollingInterval": "Day"
        }
      },
      {
        "Name": "SQLite",
        "Args": {
          "sqliteDbPath": "../../../logs/log.sqlite",
          "tableName": "Logs",
          "maxDatabaseSize": 1
        }
      }
    ]
  },
  "AllowedHosts": "*"
}
```

![範例6-1](https://user-images.githubusercontent.com/19286751/193850407-55454218-ea65-46ed-8831-c7f8cc8196f5.png)

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
![範例8-1](https://user-images.githubusercontent.com/19286751/193861408-b6a6bdc5-f981-4b65-9383-5253fc0134c2.png)

![範例8-2](https://user-images.githubusercontent.com/19286751/193861542-eb3f655c-f4d1-42e3-a1c5-99d386019263.png)

執行後查看Log檔
![範例8-3](https://user-images.githubusercontent.com/19286751/193861723-8bdd7d6b-31a5-42b7-bc3c-d14416b1101c.png)

![範例8-4](https://user-images.githubusercontent.com/19286751/193861910-905e6de0-1778-40f9-acea-b3e53da797c2.png)

點擊txt檔案後會看到我們所寫的Log檔案，會發現

- 第一個紅框處非匿名類型多一個$type跟你說明是什麼類型
- 第二個紅框處是由於在Program.cs加入了app.UseSerilogRequestLogging();會記錄使用Get請求呼叫了WeatherForecast回傳狀態碼200用了31ms的時間
![範例8-5](https://user-images.githubusercontent.com/19286751/193861061-d25cee45-412a-4f66-bc3d-c4d0952615e4.png)

### 參考

[Serilog](https://github.com/serilog/serilog-settings-configuration) [m@rcus 學習筆記](https://marcus116.blogspot.com/2019/05/about-netcore-serilog-config-settings.html)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/SerilogExample_Advanced)