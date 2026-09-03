---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/NLogExample
author: CI-YU
---

# .NET 6 NLog範例

### 目的

在webapi專案下使用NLog套件

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/158062716-eff12417-b1a4-42c6-a379-53940b79d07f.png)

### 其他資訊

直接進行下一步

### NuGet加入套件

- NLog
- NLog.Web.AspNetCore

![步驟4](https://user-images.githubusercontent.com/19286751/158211424-474efe49-67b0-4190-8d47-0c598cb19900.png)

### 新增nlog.config檔案

在根目錄新增nlog.config檔案
![步驟5-1](https://user-images.githubusercontent.com/19286751/158211819-ad11ff2a-50b7-4a6a-9eea-6751eba2a54a.png)

![步驟5-2](https://user-images.githubusercontent.com/19286751/158212071-64974dcd-13d9-4a86-8a9f-fbf500d0346e.png)

### nlog.config寫入程式

在nlog.config寫入官方範例

```xml
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      autoReload="true"
      internalLogLevel="Info"
      internalLogFile="c:\temp\internal-nlog-AspNetCore.txt">

	<!-- enable asp.net core layout renderers -->
	<extensions>
		<add assembly="NLog.Web.AspNetCore"/>
	</extensions>

	<!-- the targets to write to -->
	<targets>
		<!-- File Target for all log messages with basic details -->
		<target xsi:type="File" name="allfile" fileName="c:\temp\nlog-AspNetCore-all-${shortdate}.log"
				layout="${longdate}|${event-properties:item=EventId_Id:whenEmpty=0}|${level:uppercase=true}|${logger}|${message} ${exception:format=tostring}" />

		<!-- File Target for own log messages with extra web details using some ASP.NET core renderers -->
		<target xsi:type="File" name="ownFile-web" fileName="c:\temp\nlog-AspNetCore-own-${shortdate}.log"
				layout="${longdate}|${event-properties:item=EventId_Id:whenEmpty=0}|${level:uppercase=true}|${logger}|${message} ${exception:format=tostring}|url: ${aspnet-request-url}|action: ${aspnet-mvc-action}|${callsite}" />

		<!--Console Target for hosting lifetime messages to improve Docker / Visual Studio startup detection -->
		<target xsi:type="Console" name="lifetimeConsole" layout="${MicrosoftConsoleLayout}" />
	</targets>

	<!-- rules to map from logger name to target -->
	<rules>
		<!--All logs, including from Microsoft-->
		<logger name="*" minlevel="Trace" writeTo="allfile" />

		<!--Output hosting lifetime messages to console target for faster startup detection -->
		<logger name="Microsoft.Hosting.Lifetime" minlevel="Info" writeTo="lifetimeConsole, ownFile-web" final="true" />

		<!--Skip non-critical Microsoft logs and so log only own logs (BlackHole) -->
		<logger name="Microsoft.*" maxlevel="Info" final="true" />
		<logger name="System.Net.Http.*" maxlevel="Info" final="true" />

		<logger name="*" minlevel="Trace" writeTo="ownFile-web" />
	</rules>
</nlog>
```

只擷取部分畫面
![範例6](https://user-images.githubusercontent.com/19286751/158213049-00f980ea-501d-4fd7-b4d0-5f81a58aad4a.png)

### Program寫入程式

在Program寫入官方範例

```c#
using NLog;
using NLog.Web;
var logger = LogManager.Setup().LoadConfigurationFromAppSettings().GetCurrentClassLogger();
logger.Debug("init main");
try {
  var builder = WebApplication.CreateBuilder(args);

  //將NLog註冊到此專案內
  builder.Logging.ClearProviders();
  //設定log紀錄的最小等級
  builder.Logging.SetMinimumLevel(Microsoft.Extensions.Logging.LogLevel.Information);
  builder.Host.UseNLog();
  builder.Services.AddControllers();
  // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
  builder.Services.AddEndpointsApiExplorer();
  builder.Services.AddSwaggerGen();

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
} catch (Exception ex) {
  // 捕獲設定錯誤的錯誤紀錄
  logger.Error(ex, "Stopped program because of exception");
  throw;
} finally {
  //須確定在關閉時，把nlog關閉
  LogManager.Shutdown();
}
```

只擷取部分畫面
![範例7](https://user-images.githubusercontent.com/19286751/194465911-dd0c7785-3282-434f-a153-90372bbd2e15.png)

### 設定appsetting.json

將原先存在的default移除

```json
{
  "Logging": {
    "LogLevel": {
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

![範例8](https://user-images.githubusercontent.com/19286751/158407049-fcaba46c-f6af-404d-a977-fe62c64e3376.png)

### controller寫入log

在預設的controller裡面寫入Log，如下圖紅框處

```c#
//寫在建構子內
_logger.LogDebug(1, "NLog injected into HomeController");
//寫在action內
_logger.LogInformation("這是範例程式預設的controller!!");
```

![範例9](https://user-images.githubusercontent.com/19286751/158409422-ac21aeb0-4f94-443c-b5c1-837b1e9eaa0a.png)

### 執行結果

點try it out後點execute，確定執行完成查看console檔案(執行專案會啟動一個terminal)
![步驟10-1](https://user-images.githubusercontent.com/19286751/158414836-4796d115-292c-4249-ac3e-5c3ce21fefc6.png)

![步驟10-2](https://user-images.githubusercontent.com/19286751/158415050-62bcb17d-a406-4b76-8013-ac0285b0501d.png)

![步驟10-3](https://user-images.githubusercontent.com/19286751/158415452-71160939-0981-4fec-95ba-b0a07aecd7ee.png)

> 步驟六有在設定檔內設定log存放路徑，c:\temp\internal-nlog-AspNetCore.txt
![步驟10-4](https://user-images.githubusercontent.com/19286751/158416314-54965424-04b3-4b8a-9b00-321fbaf368dc.png)

### 結論

完成範例說明後建議使用Serilog，因為相對來說單純一點，對於設定上來說nlog真的比較複雜。

### 參考

[官方範例](https://github.com/NLog/NLog/wiki/Getting-started-with-ASP.NET-Core-6)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/NLogExample)