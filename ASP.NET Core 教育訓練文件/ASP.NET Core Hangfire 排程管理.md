Hangfire 是一款個人認為相當不錯的非同部步服務器，它脫離 Windows 工作排程，在 Web 檢視、重送任務，在 Hangfire 操作 UI 介面可以知道你指派給它的任務狀態，何時成功？為什麼失敗？(例外捕捉)下一次任務觸發時間？訊息可說是相當的完整。不過有點可惜的是，預設 Hangfire 操作介面沒有手動觸發任務的介面，幸好 Hangfire.Dashboard.Management 彌補了這個不足...

延伸閱讀

[[Hangfire\] 使用 Hangfire OWIN 建立非同步任務](https://dotblogs.com.tw/yc421206/2019/12/25/desktop_app_async_task_via_hangfire)

## 開發環境

- ASP.NET Core 3.1
- VS 2019

範例內包含了 .NET Framework 4.8 的專案

## 實作

開一個 ASP.NET Core Web Application 專案 → 空白樣板

### 安裝套件

```
Install-Package HangfireInstall-Package Hangfire.MemoryStorageInstall-Package Hangfire.ConsoleInstall-Package Hangfire.Dashboard.Management
```

 

### 配置 Configure

`app.UseHangfireServer()`：設定 Queue、服務逾時、WorkCount 等等...

`app.UseHangfireDashboard`：設定權限、URL 等等..

```c#
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
 
    app.UseHangfireServer();
    app.UseHangfireDashboard("/hangfire",
                             new DashboardOptions
                             {
                                 //預設授權無法在線上環境使用 Hangfire.Dashboard.LocalRequestsOnlyAuthorizationFilter
                                 Authorization = new[] {new DashboardAuthorizationFilter()}
 
                                 //AppPath = System.Web.VirtualPathUtility.ToAbsolute("~/"),
                                 //DisplayStorageConnectionString = false,
                                 //IsReadOnlyFunc = f => true
                             }
                            );
 
    app.UseRouting();
 
    app.UseEndpoints(endpoints =>
                     {
                         endpoints.MapGet("/",
                                          async context =>
                                          {
                                              await context.Response.WriteAsync("Hello World!");
                                          });
                     });
}
```

 

### 配置 ConfigureServices

接著在這裡設定 Hangfire 要有那些功能，

`config.UseDashboardMetric()`：小報表，可根據需求決定，Hangfire angfire 內建許多的報表

`config.UseConsole()` ：來自 Hangfire.Console，輸出 Console.Log 到onsole.Log 到 Hangfire 頁面。

`config.UseSqlServerStorage()` ：來自 Hangfire.SqlServer，排程資料放在 SQL Server。

`config.UseManagementPages()` ：來自 Hangfire.Dashboard.Management，本篇主要的重點，任務管理工具，可以在 /hangfire 操作介面直接新增任務

```c#
public void ConfigureServices(IServiceCollection services)
{
    services.AddHangfire(config => config
                                   .UseSimpleAssemblyNameTypeSerializer()
                                   .UseRecommendedSerializerSettings()
                                   .UseColouredConsoleLogProvider()
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.ServerCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.RecurringJobCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.RetriesCount)
 
                                   //.UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.EnqueuedCountOrNull)
                                   //.UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.FailedCountOrNull)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics
                                                               .EnqueuedAndQueueCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics
                                                               .ScheduledCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics
                                                               .ProcessingCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics
                                                               .SucceededCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.FailedCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics.DeletedCount)
                                   .UseDashboardMetric(Hangfire.Dashboard.DashboardMetrics
                                                               .AwaitingCount)
                                   .UseConsole()                                                                                                                //from Hangfire.Console
                                   .UseSqlServerStorage(@"Data Source=(localdb)\mssqllocaldb;Initial Catalog=Hangfire;Encrypt=False;Integrated Security=True;") //from Hangfire.SqlServer
                                   .UseManagementPages(p => p.AddJobs(() => GetModuleTypes())) //from Hangfire.Dashboard.Management
                        );
}
```

 

GetModuleType 取出 Assembly 裡面所有的 ManagementPage 的物件

```c#
public static Type[] GetModuleTypes()
{
    var assemblies = new[] {typeof(DemoJob).Assembly};
    var moduleTypes = assemblies.SelectMany(f =>
                                            {
                                                try
                                                {
                                                    return f.GetTypes();
                                                }
                                                catch (Exception)
                                                {
                                                    return new Type[] { };
                                                }
                                            }
                                           ) 
                                .ToArray();
 
    return moduleTypes;
}
```

 

效果如下，DemoJob 是我這次演練的物件

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582805198.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582805198.png)

 

### ManagementPage

config.UseManagementPages 裡面放 ManagementPage 物件，設計要點如下，

1. 在類別加上 Hangfire.Dashboard.Management.Metadata.ManagementPageAttribute。
2. 方法加上 Hangfire.Dashboard.Management.Support.JobAttribute、System.ComponentModel.DisplayNameAttribute，這樣可以輕易地完成一個管理介面。
3. PerformContext 來自 Hangfire.Console，會在 Hangfire Hangfire 介面的 Log 主控台呈現。
4. IJobCancellationToken，當任務在執行過程當成被刪除，IsCancellationRequested = true

```c#
[ManagementPage("演示")]
public class DemoJob
{
    [Hangfire.Dashboard.Management.Support.Job]
    [DisplayName("呼叫內部方法")]
    public void Action(PerformContext context = null, IJobCancellationToken cancellationToken = null)
    {
        if (cancellationToken.ShutdownToken.IsCancellationRequested)
        {
            return;
        }
 
        context.WriteLine($"測試用，Now:{DateTime.Now}");
        Thread.Sleep(30000);
    }
}
```

 

執行結果如下：

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582959327.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582959327.png)

 

#### Task type Queue execution

原本要自己寫扣決定非同步類型，可以不需要寫了，交由給這個管理介面幫忙建立任務類型

Queue execution => BackgroundJob.Enqueue();

Timely execution => BackgroundJob.Schedule();

Delayed execution => BackgroundJob.ContinueWith();

Repeated execution => RecurringJob.AddOrUpdate();

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582959395.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582959395.png)

 

PerformContext 呈現效果如下：

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990661.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990661.png)

 

#### DisplayData

自訂輸入參數介面，只要在參數加上 DisplayDataAttribute，就能根據型別長出對應的 UI 介面，enum 對應下拉選單，還能自訂下拉選單的內容，例如 EncodingsInputDataList class

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582988781.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582988781.png)

 

執行結果下圖：

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582988889.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582988889.png)

 

完整設定如下

```c#
[ManagementPage("演示")]
public class DemoJob
{
    [Hangfire.Dashboard.Management.Support.Job]
    [DisplayName("呼叫內部方法")]
    [Description("呼叫內部方法")]
    [AutomaticRetry(Attempts = 3)]   //自動重試
    [DisableConcurrentExecution(90)] //禁止使用並行
    public void Action(PerformContext context = null, IJobCancellationToken cancellationToken = null)
    {
        if (cancellationToken.ShutdownToken.IsCancellationRequested)
        {
            return;
        }
 
        context.WriteLine($"測試用，Now:{DateTime.Now}");
        Thread.Sleep(30000);
    }
 
    [Queue("WebAPI")]
    [Hangfire.Dashboard.Management.Support.Job]
    [DisplayName("呼叫外部服務")]
    [Description("呼叫外部服務")]
    [AutomaticRetry(Attempts = 3)]   //自動重試
    [DisableConcurrentExecution(90)] //禁止使用並行
    public string CallWebApi(
        [DisplayData("服務端點",
                     "http://localhost:8080/test.html?name=youname",
                     "請求位置必須為 http or https")]
        Uri url,
        [DisplayData("請求方式",
                     "POST",
                     "常用的請求方式 GET、POST、PUT、DELETE ")]
        HttpMethod method = HttpMethod.POST,
        [DisplayData("請求內容", IsMultiLine = true)]
        string content = null,
        [DisplayData("內容類型",
                     "application/x-www-form-urlencoded",
                     "常見的有 application/x-www-form-urlencoded、multipart/form-data、text/plain、application/json 等",
                     "application/x-www-form-urlencoded")]
        string contentType = "application/x-www-form-urlencoded",
        [DisplayData("內容編碼方式",
                     "utf-8",
                     "常見的有 UTF-8、Unicode、ASCII，錯誤的編碼會導致內容無法正確呈現",
                     "utf-8",
                     ConvertType = typeof(EncodingsInputDataList))]
        string contentEncoding = "UTF-8",
        [DisplayData("回應結果內容編碼",
                     "utf-8",
                     "常見的有 UTF-8、Unicode、ASCII，錯誤的編碼會導致內容無法正確呈現",
                     "utf-8",
                     ConvertType = typeof(EncodingsInputDataList))]
        string responseEncoding = "UTF-8",
        PerformContext context = null)
    {
        var defaultContentEncoding  = Encoding.GetEncoding(contentEncoding)  ?? Encoding.UTF8;
        var defaultResponseEncoding = Encoding.GetEncoding(responseEncoding) ?? Encoding.UTF8;
 
        context.WriteLine($"測試用，Now:{DateTime.Now}");
 
        //Thread.Sleep(30000);
        return $"模擬呼叫Web API返回結果，目前時間：{DateTime.Now}，內容編碼：{defaultContentEncoding}，回傳編碼：{defaultResponseEncoding}";
    }
}
```

 

EncodingsInputDataList.GetData 回傳 Dictionary<string, string> 型別，就可以在任務管理介面看到下拉選單

```c#
public class EncodingsInputDataList : IInputDataList
{
	public Dictionary<string, string> GetData()
	{
		return Encoding.GetEncodings()
					   .GroupBy(f => f.Name, (f1, f2) => f2.FirstOrDefault())
					   .ToDictionary(f => f.Name, f => f.DisplayName);
	}

	public string GetDefaultValue()
	{
		return null;
	}
}
```

 

### 任務執行配置

可以替任務方法加上 Hangfire 執行這些任務的設定，比如重試次數(AutomaticRetryAttribute)、停用並行(DisableConcurrentExecutionAttribute)，詳情參考 https://docs.hangfire.io/en/latest/background-processing/throttling.html

 

### CRON Expression

RecurringJob 排程工作可以根據 CRON 依照年、月、週、日來定義比較複雜的定期排程，Hangfire.Dashboard.Management 的 Repeated execution 則整合 https://github.com/bradymholt/cron-expression-descriptor

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582989199.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582989199.png)

 

#### Cron Expression Analysis

紅框處，彼此互相 analysis

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582989727.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582989727.png)

 

#### Cron Expression Builder

說明頁面描述可以支援到秒的單位，但是 Analysis 沒有支援到秒

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990118.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990118.png)

 

#### Verified address

除了用 CRON Expression 幫我們產生語法之外，還能驗證這個語法是不是我們期望的，他的位置為 /hangfire/cron?cron=*+*+*+*+* ，不同的時間單位用 + 號隔開

每分鐘

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990420.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990420.png)

每兩分鐘

[![img](https://dotblogsfile.blob.core.windows.net/user/%E4%BD%99%E5%B0%8F%E7%AB%A0/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990505.png)](https://dotblogsfile.blob.core.windows.net/user/余小章/9ad2147f-18a0-41ad-b4de-5c61259d0cd7/1582990505.png)

 

## 參考來源

https://github.com/mccj/Hangfire.Dashboard.Management/tree/master/Samples

 

## 範例位置

https://github.com/yaochangyu/sample.dotblog/tree/master/Hangfire/Lab.HangfireManager