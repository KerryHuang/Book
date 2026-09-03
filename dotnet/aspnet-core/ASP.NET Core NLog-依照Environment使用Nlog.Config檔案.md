---
kind: original
---

# ASP.NET Core NLog-依照Environment使用Nlog.Config檔案

前情提要
筆者公司使用NLog當作Log工具，相當簡單易用，但用到現在會有一個困擾，畢竟為方便測試，到處埋Info等級的Log於程式中，為方便偵錯及追蹤，可能連傳入的資料都會記錄於文字檔中，變成正式環境也會有同樣的效果，因為這個Nlog.Config又加入於版控中，要嘛就是在release分支那邊將Nlog.config調整成正式環境符合的設定，也是頗麻煩。

筆者這篇主要是解決上述問題，解決方式也頗簡單，將Nlog.config製作多個帶有Environment的檔名，NLogBuilder註冊時套用不同的NLog.Config檔案即可解決。基本上若為預設的NLog.config則不需特別註冊也有效，因要針對不同環境，套用不同的config檔案，必須宣告NLogBuilder註冊。

內容
筆者這邊使用dotnet core版本為6.0.100，已經是套用minimal api形式，還真不習慣。

Demo專案建立
首先簡單建立一下webapi專案
```
dotnet new webapi -o NLog.Demo.API
```

加入NLog相關套件
筆者這邊會使用到三個NLog相關套件

NLog
NLog.Config
NLog.Web.AspNetCore
```
dotnet add package NLog
dotnet add package NLog.Config
dotnet add package NLog.Web.AspNetCore
```
製作不同環境使用的NLog.Config檔案
就直接用手動方式建立不同環境使用的NLog.Config檔案
```
touch nlog.development.config
touch nlog.production.config
```
直接從NLog.Config預設的設定，調整成不同環境所要的rules及target，筆者這邊為演示，直接使用文字檔案紀錄，並且於不同環境下設定不一樣的minlevel，以示有效套用。

```xml
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.nlog-project.org/schemas/NLog.xsd NLog.xsd" autoReload="true" throwExceptions="false" internalLogLevel="Off" internalLogFile="c:\temp\nlog-internal.log">

  <!-- optional, add some variables
  https://github.com/nlog/NLog/wiki/Configuration-file#variables
  -->
  <variable name="myvar" value="myvalue" />

  <!--
  See https://github.com/nlog/nlog/wiki/Configuration-file
  for information on customizing logging rules and outputs.
   -->
  <targets>

    <!--
    add your targets here
    See https://github.com/nlog/NLog/wiki/Targets for possible targets.
    See https://github.com/nlog/NLog/wiki/Layout-Renderers for the possible layout renderers.
    -->

    <!--
    Write events to a file with the date in the filename.
    <target xsi:type="File" name="f" fileName="${basedir}/logs/${shortdate}.log"
            layout="${longdate} ${uppercase:${level}} ${message}" />
    -->

    <target xsi:type="File" name="f" fileName="${basedir}/logs/${shortdate}.log" layout="${longdate} ${uppercase:${level}} ${message}" />
  </targets>

  <rules>
    <logger name="*" minlevel="Info" writeTo="f" />
  </rules>
</nlog>
```

```xml
<!--以上省略-->
<rules>
  <logger name="*" minlevel="Error" writeTo="f" />
</rules>
<!--以下省略-->
```
套用不同的NLog.Config
於Program.cs中宣告NLogBuilder註冊
```c#
// 以上省略
// Nlog config
var env = builder.Environment.EnvironmentName;
NLogBuilder.ConfigureNLog($"nlog.{env}.config").GetCurrentClassLogger();
//以下省略
builder.Logging.ClearProviders();
builder.Host.UseNLog();
```

一樣是在Program.cs中，寫一個簡單的API入口以準備測試
```c#
// 以上省略
app.MapControllers();
app.MapGet("/logtest", () =>
{
    app.Logger.LogTrace("LogTrace");
    app.Logger.LogDebug("LogDebug");
    app.Logger.LogInformation("LogInformation");
    app.Logger.LogWarning("LogWarning");
    app.Logger.LogError("LogError");
    app.Logger.LogCritical(new Exception("eLogCritical"), "LogCritical");
    return "logtest";
});
app.Run();
```

Demo效果
筆者透過launchsettings.json中的設定來模擬不同執行環境
```c#
// 以上省略
"profiles": {
    "NLog.Demo.API": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
      "applicationUrl": "http://localhost:5187",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development" // 設定值要切換成development/production做測試
      }
    },
    // 以下省略
  }
```

為方便直接透過swagger api說明頁面點擊其API，調整一下Program.cs中的設定

```c#
// Production環境也先保有swagger api說明頁面
//if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
```

先看一下swagger api說明頁面，直接點上面的/logtest API

Development環境
執行完成後會在文字檔案中可看到minlevel為info的效果，從info等級開始印
```
2022-05-17 14:51:52.9377 INFO LogInformation
2022-05-17 14:51:52.9377 WARN LogWarning
2022-05-17 14:51:52.9377 ERROR LogError
2022-05-17 14:51:52.9377 FATAL LogCritical
```
Production環境
執行完成後會在文字檔案中可看到minlevel為error的效果，從error等級開始印
```
2022-05-17 14:52:35.3299 ERROR LogError
2022-05-17 14:52:35.3434 FATAL LogCritical
```
---
結論
落落等寫了這麼多，基本上就是只有兩步驟

製作不同環境使用的NLog.Config檔案
宣告NLogBuilder.ConfigureNLog的方式不同環境下套用不同的NLog.Config檔案
以上解決方案，確實解決筆者困擾的問題，這篇就到這邊了，下篇見。