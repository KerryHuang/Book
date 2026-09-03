---
kind: original
---

# Docker - 第九章 | 安裝 datalust seq

Seq 是一款使用現代化技術建置的結構化日誌儲存，查詢，分析工具。比起 ELK 這種組合要輕量級許多。只需要一個安裝套件就具有資料儲存，查詢，圖表分析功能。它對 windows 友好，直接提供了安裝套件。當然也可以使用 docker 來部署。Seq 對於單個使用者是免費的，這對於一些小團隊並沒有什麼問題。Seq 一個比較強大的功能是提供了類似 Sql 語句的資料查詢及處理能力，使得使用者可以直接寫 Select from 來得到自己想要的資料。

1. 收費
    * 免費的個人版，只能以一個使用者帳號連到網頁介面(沒有辦法做權限控管)，而且同時只有一個session可以使用(以cookie:Seq-Session為準)，可以在企業中使用這個版本
    * 如果裝app在seq站台，app的行為會視為另一個使用者
    * 在未啟用授權的狀況下，session數量不影響，但不能安裝app

2. 環境 docker
    * 啟動container，使用volume mount實體路徑: 

    ```
    docker run --name seq -d --restart unless-stopped -e ACCEPT_EULA=Y -v D:\docker\seqdata:/data -p 5341:80 datalust/seq:latest
    ```

3. 開發 (Microsoft.Extensions.Logging)

    1. 在專案中加入 [Seq.Extensions.Logging](https://www.nuget.org/packages/Seq.Extensions.Logging) NuGet 套件

    2. 在 `Program.cs` 加入 Seq 的 Log Provider

        ```
        builder.Logging.AddSeq();
        ```

    3. 如果要指定 Seq 伺服器位置與 API Key 的話，也可以這樣寫：

        ```
        builder.Logging.AddSeq(serverUrl: "http://localhost:5341", apiKey: "your-api-key");
        ```

    4. 如果要直接從組態進行設定，可以這樣寫：
        ```
        builder.Logging.AddSeq(builder.Configuration.GetSection("Seq"));
        ```

    5. 而 `appsettings.json` 的設定值如下：

        ```json
        {
          "Seq": {
            "ServerUrl": "http://localhost:5341",
            "ApiKey": "1234567890",
            "MinimumLevel": "Trace",
            "LevelOverride": {
              "Microsoft": "Warning"
            }
          }
        }
        ```

        

4. 開發 (Nlog)

    1. nuget套件 - NLog.Targets.Seq

    2. 在 `Program.cs` 加入 Seq 的 Log Provider

       ```c#
       #region 加入 NLog 相關資訊
       // 環境的相關資訊
       #if DEBUG
       NLogBuilder.ConfigureNLog($"nlog.config").GetCurrentClassLogger();
       #else
       NLogBuilder.ConfigureNLog($"nlog.{environmentName}.config").GetCurrentClassLogger();
       #endif
       // 將NLog註冊到此專案內
       builder.Logging.ClearProviders();
       // 設定log紀錄的最小等級
       builder.Logging.SetMinimumLevel(Microsoft.Extensions.Logging.LogLevel.Information);
       builder.Host.UseNLog();
       #endregion
       ```

       

    3. nlog.config
    ```xml
    <extensions>
        <!-- 引用seq type -->
        <add assembly="NLog.Targets.Seq"/>
    </extensions>
    
    <targets>
        <!-- 使用AsyncWrapper(nlog原生)可提升效能，且當寫入seq有問題時不會影響應用程式結果 -->
        <!-- 參考: https://github.com/NLog/NLog/wiki/AsyncWrapper-target -->
        <target name="seq" xsi:type="AsyncWrapper" overflowAction="Discard" queueLimit="10000" batchSize="200" timeToSleepBetweenBatches="1">
            <!-- 可以啟用apikey，只允許授權的key寫入log，也可做到群組統計的效果 -->
            <target xsi:type="Seq" serverUrl="http://localhost:5341" apiKey="" >
                <!-- property會一起帶到seq log裡，可作為filter欄位 -->
                  <property name="SourceContext" value="${logger}" />
                  <property name="ThreadId" value="${threadid}" as="number" />
                  <property name="MachineName" value="${machinename}" />
                  <property name="Environment" value="${windows-identity}" />
                  <property name="Application" value="KH.Lab.Seq" />
            </target>
        </target>
    </targets>
    ```
    3. 調整完後按重建才可吃到config的設定

    

5. 測試記錄到Seq

    1. 修改 `HomeController` 類別，加入不同 Log Level 的紀錄

        ```c#
        using Microsoft.AspNetCore.Mvc;
        
        namespace KH.Lab.Seq.Controllers
        {
            [ApiController]
            [Route("[controller]")]
            public class WeatherForecastController : ControllerBase
            {
                private static readonly string[] Summaries = new[]
                {
                "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
            };
        
                private readonly ILogger<WeatherForecastController> _logger;
        
                public WeatherForecastController(ILogger<WeatherForecastController> logger)
                {
                    _logger = logger;
                }
        
                [HttpGet(Name = "GetWeatherForecast")]
                public IEnumerable<WeatherForecast> Get()
                {
                    _logger.LogTrace("這是 Trace");
                    _logger.LogDebug("這是 Debug");
                    _logger.LogInformation("這是 Information");
                    _logger.LogWarning("這是 Warning");
                    _logger.LogError("這是 Error");
                    _logger.LogCritical("這是 Critical");
        
                    return Enumerable.Range(1, 5).Select(index => new WeatherForecast
                    {
                        Date = DateTime.Now.AddDays(index),
                        TemperatureC = Random.Shared.Next(-20, 55),
                        Summary = Summaries[Random.Shared.Next(Summaries.Length)]
                    })
                    .ToArray();
                }
            }
        }
        ```

    2. 進入 Seq 首頁 ( [http://localhost:5341](http://localhost:5341/) ) 即可看見 Log 已經被成功寫入！

6. 網頁介面

    1. 透過signals設定區分不同過濾條件(例如站台名稱)，等於建置索引，效能比較好
        https://docs.datalust.co/docs/signals
    2. Workspace只是影響進入時要顯示的幾個signals
    3. 從Settings->Retention設定清空events排程
    4. 可以設定占用記憶體跟硬碟最小剩餘空間多少後不再寫入

7. [部署總覽](https://docs.datalust.co/docs/production-deployment)

8. 參考資料

    1. [.Net Core with 微服務 - Seq 日誌聚合](https://kknews.cc/zh-tw/code/3ykpaoo.html)
    2. [C#：NLog接入配置與簡單使用](https://zhuanlan.zhihu.com/p/610461723)
    3. [Microsoft.Extensions.Logging](https://docs.datalust.co/docs/microsoft-extensions-logging)
    4. [NLog](https://docs.datalust.co/docs/using-nlog)
    5. [如何在現有 ASP.NET Core 專案加入 Seq 記錄提供者](https://blog.miniasp.com/post/2023/05/13/Add-Seq-Log-Provider-in-ASPNET-Core)
