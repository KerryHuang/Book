---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/HangfireExample
author: CI-YU
---

# .NET 6 Hangfire範例

### 目的

在windows系統上想執行排程有兩個選擇

1. 使用windows工作排程器執行exe檔
2. 透過Hangfire進行排程管理

此次教學說明如何使用Hangfire執行排程

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![範例2-1](https://user-images.githubusercontent.com/19286751/194689500-5b5c96ec-2b84-4612-9a2d-ec329a039981.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Hangfire
- Hangfire.InMemory

![範例4-1](https://user-images.githubusercontent.com/19286751/194689748-3481e5a1-e8c5-46e8-b012-80aacf1a398b.png)

### 編輯Program.cs檔

```C#
using Hangfire;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
//註冊hangfire並且使用記憶體保存排程，
//預設所下載的HangFire套件可以使用sqlserver，可透過config.UseSqlServerStorage();，但需要設定
builder.Services.AddHangfire(config => {
  config.UseInMemoryStorage();
});
//註冊hangfire要使用的伺服器，伺服器就是上面所寫的使用記憶體當伺服器
builder.Services.AddHangfireServer();
var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment()) {
  app.UseSwagger();
  app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();
//使用hangfire內建的儀表板
app.UseHangfireDashboard();
app.MapControllers();

app.Run();
```

![範例5-1](https://user-images.githubusercontent.com/19286751/194691360-f7ce1a6c-a5bf-4a8d-a1bd-071979c455fc.png)

### 編輯WeatherForecastController.cs類別檔

```C#
    //記得using Hangfire;
    [HttpGet(Name = "GetWeatherForecast")]
    public IEnumerable<WeatherForecast> Get() {
      //單次立即執行
      BackgroundJob.Enqueue(() => Console.WriteLine("單次!"));
      //單次10秒後執行
      BackgroundJob.Schedule(() => Console.WriteLine("10秒後執行!"), TimeSpan.FromSeconds(10));
      //重複執行，預設為每天00:00啟動
      RecurringJob.AddOrUpdate(() => Console.WriteLine("重複執行！"), Cron.Daily);
      return Enumerable.Range(1, 5).Select(index => new WeatherForecast {
        Date = DateTime.Now.AddDays(index),
        TemperatureC = Random.Shared.Next(-20, 55),
        Summary = Summaries[Random.Shared.Next(Summaries.Length)]
      })
      .ToArray();
    }
```

![範例6-1](https://user-images.githubusercontent.com/19286751/194691871-92f50f80-7e55-4b1a-bb48-c66dccffc56b.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果
![範例7-1](https://user-images.githubusercontent.com/19286751/194691970-01c31af8-7980-4ce7-9467-fbf6dc70a388.png)

![範例7-2](https://user-images.githubusercontent.com/19286751/194691986-aa08ea36-23a1-4f4e-a416-49ac6f52edd3.png)

接下來到hangfire儀表板查看執行狀態

> 預設的網址為https://domain/hangfire 我的swagger網址為 https://localhost:7198/swagger/index.html 所以下方為hangfire預設路徑 https://localhost:7198/hangfire

就可以看到Hangfire的畫面了，接著點擊上方`工作`就可以看到所執行的排程，如需看重複作業則點選`定期工作`
![範例7-3](https://user-images.githubusercontent.com/19286751/194692189-289a1af5-7427-4bb8-b37c-1abaf58ef85a.png)

![範例7-4](https://user-images.githubusercontent.com/19286751/194692230-e67345a8-501b-47a3-a621-1ab5150c8bbc.png)

![範例7-5](https://user-images.githubusercontent.com/19286751/194692393-b626fa0b-7943-4bf7-928d-0ff0b275d135.png)

### 後記

任務排程的套件還有另外兩個[Coravel](https://docs.coravel.net/)與[Quart.Net](https://www.quartz-scheduler.net/)都可以參考看看

### 參考

[Hangfire官網](https://github.com/HangfireIO/Hangfire)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/HangfireExample)