---
kind: reprint
source: site:dotblogs.com.tw
author: chris
---

本文實作 IHostedService 介面將 Quartz.Net 排程作業託管於 ASP.NET Core 網站中，並以 SignalR 實現 real-time 排程狀態管理 Dashboard 頁面

## 前言

------

當應用網站有一些外部資料需要定時獲得，或是有些內部耗時作業需要批次逐筆消化時，都會需要排程作業來處理，而比較精簡的方式就是將排程作業 Host 在 .NET Core 應用程式上運行，本文會將 Quartz.NET 排程作業託管於 ASP.NET Core 網站中作為範例；解決了運行問題後所面臨到的就是維運，要如何讓維運人員可以清楚明瞭的掌握目前各個排程作業的執行狀況，這就必須提供一個即時性的 Dashboard 頁面來呈現相關資訊，這部分可透過 SignalR 技術讓 Dashboard 跟後端程式保持一個即時相互主動的溝通渠道，以此避免以往前端定期向後端 Pulling 資料所造成的網路資訊消耗。

 

 

## Quartz.NET 套件

------

本文使用的 Quartz.NET 是一款開源的排程作業框架，透過 Scheduler、Trigger 及 Job 組合出所需要的作業執行策略，另外透過其 cron expression 來描述作業被觸發的時機，從秒、分、時、日、月、星期、年都可以進行操作，滿足各項排程執行頻率需求。

先於專案中透過 Nuget 下載安裝 Quartz.NET 套件 (目前版本為 3.2.3)。

![img](https://dotblogsfile.blob.core.windows.net/user/chris/899f2ad6-7bb1-4ba2-a4f8-e78609455bbf/1607932358.png)

 

 

## 建立 Job

------

首先定義作業內容為何，依據 Quartz.NET 定義的 IJob 介面來實作出一個 ReportJob 來，接著在 Execute方法中執行主要工作。其中有幾個需要注意的地方如下：

- 標記 [DisallowConcurrentExecution] 標籤來禁止同一個 Job 被同時併發執行。
- 透過 IJobExecutionContext 的 context.JobDetail.JobDataMap 取得在建立 JobDetail 時加入的自定義資訊，因此 Job 就可以依據傳入的參數不同而執行不同的任務。
- 由於 Job 在 DI 容器中註冊為 singleton 實體，因此於 Job 內無法注入比 singleton 生命週期範圍還小物件實體 (e.g. scope)，此時可注入 IServiceProvider 透過 CreateScope 來產生 scope ，並藉此手動建立出生命週期為 scope 的實體 (e.g. dbContext)。
- 由於 Job 是可以被中斷，因此可以使用 IJobExecutionContext的 CancellationToken.IsCancellationRequested 作為作業被中斷的判斷條件，自行定義安全中斷工作的時機。

```cs
[DisallowConcurrentExecution]
public class ReportJob : IJob
{
    private readonly ILogger<ReportJob> _logger;

    private readonly IServiceProvider _provider;


    public ReportJob(ILogger<ReportJob> logger, IServiceProvider provider)
    {
        _provider = provider ?? throw new ArgumentNullException(nameof(provider));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }


    public Task Execute(IJobExecutionContext context)
    {

        // 可取得自定義的 JobSchedule 資料, 可根據 JobSchedule 提供的內容建立不同 report 資料
        var schedule = context.JobDetail.JobDataMap.Get("Payload") as JobSchedule;
        var jobName = schedule.JobName;

        using (var scope = _provider.CreateScope())
        {
            // 如果要使用到 DI 容器中定義為 Scope 的物件實體時，由於 Job 定義為 singleton
            // 因此無法直接取得 Scope 的實體，此時就需要於 CreateScope 在 scope 中產生該實體
            // ex. var dbContext = scope.ServiceProvider.GetService<AppDbContext>();
        }


        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - start");
        for (int i = 0; i < 5; i++)
        {

            // 自己定義當 job 要被迫被被中斷時，哪邊適合結束
            // 如果沒有設定，當作業被中斷時，並不會真的中斷，而會整個跑完
            if (context.CancellationToken.IsCancellationRequested)
            {
                break;
            }

            System.Threading.Thread.Sleep(1000);
            _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - working{i}");

        }


        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - done");
        return Task.CompletedTask;
    }
}
```

 

 

## 建立 JobFactory

------

由於排程中的 Job 實體希望由 DI 容器中取得，因此依據 Quartz.NET 定義的 IJobFactory 介面來實作 JobFactory ，在 NewJob 方法中從 DI 容器取出指定 JobType 的實體。

```cs
public class JobFactory : IJobFactory
{
    private readonly IServiceProvider _serviceProvider;


    public JobFactory(IServiceProvider serviceProvider)
    {
        _serviceProvider = serviceProvider ?? throw new ArgumentNullException(nameof(serviceProvider));
    }


    public IJob NewJob(TriggerFiredBundle bundle, IScheduler scheduler)
    {
        var jobType = bundle.JobDetail.JobType;

        // 從 DI 容器取出指定 Job Type 實體
        return _serviceProvider.GetRequiredService(jobType) as IJob;
    }

    public void ReturnJob(IJob job)
    {
        var disposable = job as IDisposable;
        disposable?.Dispose();
    }
}
```

 

 

## 定義 JobSchedule 

------

剛已經定義了 ReportJob ，後續可能又會建立其他種 Job 如 SyncDataJob，因此我們希望透過一個通用性的 JobSchedule 類別來描述排程作業項目，後續將以 List<JobSchedule> 來呈現須執行的所有作業清單，例如 2 種 ReportJob 的工作再加上 1 種 SyncDataJob 工作，因此就會建立 3 筆 JobSchedule 資料，其中或許內含兩種不同 ReportJob 需要的識別碼 (自行增加屬性) 讓 ReportJob 被排程執行時可以區分 2 種要產出的報表；另外最重要的就是要提供觸發的時機，因此需要給予 cronExpression 來描述作業被觸發時機，以下是一個最精簡的示意結構。

```cs
public class JobSchedule
{
    public JobSchedule(Type jobType, string cronExpression, string jobName)
    {
        JobType = jobType ?? throw new ArgumentNullException(nameof(jobType));
        CronExpression = cronExpression ?? throw new ArgumentNullException(nameof(cronExpression));
        JobName = jobName ?? throw new ArgumentNullException(nameof(jobName));
    }

    /// <summary>
    /// Job識別名稱
    /// </summary>
    public string JobName { get; private set; }

    /// <summary>
    /// Job型別
    /// </summary>
    public Type JobType { get; private set; }

    /// <summary>
    /// Cron表示式
    /// </summary>
    public string CronExpression { get; private set; }

    /// <summary>
    /// Job狀態
    /// </summary>
    public JobStatus JobStatus { get; set; } = JobStatus.Init;
}


public enum JobStatus : byte
{
    [Description("初始化")]
    Init = 0,
    [Description("已排程")]
    Scheduled = 1,
    [Description("執行中")]
    Running = 2,
    [Description("已停止")]
    Stopped = 3,
}
```

 

 

## 建立 QuartzHostedService 

------

我們的 Quartz.NET 排程器最終要 Host 在 .NET Core 應用程式上，因此要依據 IHostedService 介面來實作 QuartzHostedService 服務，而主要就是定義服務啟動時 StartAsync 及停止時 StopAsync 需要做什麼；本例都是針對排程器 Scheduler 的建置，另外也定義了許多作業層面的操作，例如取得各項作業的執行狀態 GetJobSchedules 、手動觸發作業 TriggerJobAsync 或手動終止作業 InterruptJobAsync 等相關的操作。

在 StartAsync 啟動服務中，加入了 2 筆工作來模擬來自 DB 控制的動態報表工作項目，應用情境會是針對 ReportJob 這個通用的報表作業，但透過 DB 來設置數個不同報表的查詢條件及觸發時機，將這些所有資訊都存放在 JobSchedule 物件中；一來排程器可以依照 JobSchedule 中的 JobType 與 cronExpression 建立作業，另外透過 jobDetail.JobDataMap.Put("Payload", jobSchedule) 將 JobSchedule 額外資訊放入 ReportJob 中後，又可以幫助 ReportJob 執行時判斷需要進行的工作細節，為作業執行保留了許多彈性。

new JobSchedule(jobName: "333", jobType: typeof(ReportJob), cronExpression: $"0/13 * * * * ?");
new JobSchedule(jobName: "444", jobType: typeof(ReportJob), cronExpression: $"0/20 * * * * ?");
 

```cs
public class QuartzHostedService : IHostedService
{

    private readonly ISchedulerFactory _schedulerFactory;

    private readonly IJobFactory _jobFactory;

    private readonly ILogger<QuartzHostedService> _logger;

    private readonly IEnumerable<JobSchedule> _injectJobSchedules;

    private List<JobSchedule> _allJobSchedules;



    public IScheduler Scheduler { get; set; }

    public CancellationToken CancellationToken { get; private set; }



    public QuartzHostedService(ILogger<QuartzHostedService> logger, ISchedulerFactory schedulerFactory, IJobFactory jobFactory, IEnumerable<JobSchedule> jobSchedules)
    {
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        _schedulerFactory = schedulerFactory ?? throw new ArgumentNullException(nameof(schedulerFactory));
        _jobFactory = jobFactory ?? throw new ArgumentNullException(nameof(jobFactory));
        _injectJobSchedules = jobSchedules ?? throw new ArgumentNullException(nameof(jobSchedules));
    }



    /// <summary>
    /// 啟動排程器
    /// </summary>
    /// <param name="cancellationToken"></param>
    /// <returns></returns>
    public async Task StartAsync(CancellationToken cancellationToken)
    {
        if (Scheduler == null || Scheduler.IsShutdown)
        {
            // 存下 cancellation token 
            CancellationToken = cancellationToken;

            // 先加入在 startup 註冊注入的 Job 工作
            _allJobSchedules = new List<JobSchedule>();
            _allJobSchedules.AddRange(_injectJobSchedules);

            // 再模擬動態加入新 Job 項目 (e.g. 從 DB 來的，針對不同報表能動態決定產出時機)
            _allJobSchedules.Add(new JobSchedule(jobName: "333", jobType: typeof(ReportJob), cronExpression: "0/13 * * * * ?"));
            _allJobSchedules.Add(new JobSchedule(jobName: "444", jobType: typeof(ReportJob), cronExpression: "0/20 * * * * ?"));

            // 初始排程器 Scheduler
            Scheduler = await _schedulerFactory.GetScheduler(cancellationToken);
            Scheduler.JobFactory = _jobFactory;


            // 逐一將工作項目加入排程器中 
            foreach (var jobSchedule in _allJobSchedules)
            {
                var jobDetail = CreateJobDetail(jobSchedule);
                var trigger = CreateTrigger(jobSchedule);
                await Scheduler.ScheduleJob(jobDetail, trigger, cancellationToken);
                jobSchedule.JobStatus = JobStatus.Scheduled;
            }

            // 啟動排程
            await Scheduler.Start(cancellationToken);
        }
    }

    /// <summary>
    /// 停止排程器
    /// </summary>
    /// <returns></returns>
    public async Task StopAsync(CancellationToken cancellationToken)
    {
        if (Scheduler != null && !Scheduler.IsShutdown)
        {
            _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - Scheduler StopAsync");
            await Scheduler.Shutdown(cancellationToken);
        }
    }

    /// <summary>
    /// 取得所有作業的最新狀態
    /// </summary>
    public async Task<IEnumerable<JobSchedule>> GetJobSchedules()
    {
        if (Scheduler.IsShutdown)
        {
            // 排程器停止時更新各工作狀態為停止
            foreach (var jobSchedule in _allJobSchedules)
            {
                jobSchedule.JobStatus = JobStatus.Stopped;
            }
        }
        else
        {
            // 取得目前正在執行的 Job 來更新各 Job 狀態
            var executingJobs = await Scheduler.GetCurrentlyExecutingJobs();
            foreach (var jobSchedule in _allJobSchedules)
            {
                var isRunning = executingJobs.FirstOrDefault(j => j.JobDetail.Key.Name == jobSchedule.JobName) != null;
                jobSchedule.JobStatus = isRunning ? JobStatus.Running : JobStatus.Scheduled;
            }

        }

        return _allJobSchedules;
    }

    /// <summary>
    /// 手動觸發作業
    /// </summary>
    public async Task TriggerJobAsync(string jobName)
    {
        if (Scheduler != null && !Scheduler.IsShutdown)
        {
            _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - TriggerJobAsync");
            await Scheduler.TriggerJob(new JobKey(jobName), CancellationToken);
        }
    }

    /// <summary>
    /// 手動中斷作業
    /// </summary>
    public async Task InterruptJobAsync(string jobName)
    {
        if (Scheduler != null && !Scheduler.IsShutdown)
        {
            var targetExecutingJob = await GetExecutingJob(jobName);
            if (targetExecutingJob != null)
            {
                _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - InterruptJobAsync");
                await Scheduler.Interrupt(new JobKey(jobName));
            }

        }
    }

    /// <summary>
    /// 取得特定執行中的作業
    /// </summary>
    private async Task<IJobExecutionContext> GetExecutingJob(string jobName)
    {
        if (Scheduler != null)
        {
            var executingJobs = await Scheduler.GetCurrentlyExecutingJobs();
            return executingJobs.FirstOrDefault(j => j.JobDetail.Key.Name == jobName);
        }

        return null;
    }

    /// <summary>
    /// 建立作業細節 (後續會透過 JobFactory 依此資訊從 DI 容器取出 Job 實體)
    /// </summary>
    private IJobDetail CreateJobDetail(JobSchedule jobSchedule)
    {
        var jobType = jobSchedule.JobType;
        var jobDetail = JobBuilder
            .Create(jobType)
            .WithIdentity(jobSchedule.JobName)  
            .WithDescription(jobType.Name)
            .Build();

        // 可以在建立 job 時傳入資料給 job 使用
        jobDetail.JobDataMap.Put("Payload", jobSchedule);

        return jobDetail;
    }

    /// <summary>
    /// 產生觸發器
    /// </summary>
    /// <param name="schedule"></param>
    /// <returns></returns>
    private ITrigger CreateTrigger(JobSchedule schedule)
    {
        return TriggerBuilder
            .Create()
            .WithIdentity($"{schedule.JobName}.trigger") 
            .WithCronSchedule(schedule.CronExpression)
            .WithDescription(schedule.CronExpression)
            .Build();
    }
}
```

 

 

## 託管 QuartzHostedService

------

先在 Startup 的 ConfigureServices 方法中向 DI 容器註冊先前建立的所有類別，最後透過 AddHostedService 加入需要 Host 的 QuartzHostedService 服務後，只要 .NET Core 應用網站一執行後就會自動地啟動該服務了，所以無需再去執行 StartAsync 方法啟動服務。

筆者在向 DI 容器註冊類別時，又加入了 2 筆測試工作項目，這種操作情境為「固定不變」的作業，只要是固定「作業內容」及「觸發時機」就可以透過這種方式注入 QuartzHostedService 中。

new JobSchedule(jobName: "111", jobType: typeof(ReportJob), cronExpression: "0/30 * * * * ?");
new JobSchedule(jobName: "222", jobType: typeof(ReportJob), cronExpression: "0/52 * * * * ?");

 

```cs
public class Startup
{
  
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllersWithViews();


        //向DI容器註冊Quartz服務
        services.AddSingleton<IJobFactory, JobFactory>();
        services.AddSingleton<ISchedulerFactory, StdSchedulerFactory>();

        //向DI容器註冊Job
        services.AddSingleton<ReportJob>();

        //向DI容器註冊JobSchedule
        services.AddSingleton(new JobSchedule(jobName: "111", jobType: typeof(ReportJob), cronExpression: "0/30 * * * * ?"));
        services.AddSingleton(new JobSchedule(jobName: "222", jobType: typeof(ReportJob), cronExpression: "0/52 * * * * ?"));

        //向DI容器註冊Host服務
        services.AddSingleton<QuartzHostedService>();
        services.AddHostedService(provider => provider.GetService<QuartzHostedService>());

    }

}
```

 

 

## 啟動 .NET Core 網站

------

啟動 .NET Core 網站後 QuartzHostedService 會自動被啟動，而我們先前總共加了四個 ReportJob 類型的工作排程，可以從 log 中看到這些工作執行的狀況。

new JobSchedule(jobName: "111", jobType: typeof(ReportJob), cronExpression: "0/30 * * * * ?");
new JobSchedule(jobName: "222", jobType: typeof(ReportJob), cronExpression: "0/52 * * * * ?");
new JobSchedule(jobName: "333", jobType: typeof(ReportJob), cronExpression: "0/13 * * * * ?");
new JobSchedule(jobName: "444", jobType: typeof(ReportJob), cronExpression: "0/20 * * * * ?");

 

以 Job333 為例，當 cron expression 設定為 0/13 * * * * ? 表示從 0 秒開始，每 13 秒會執行一次，搭配分鐘設定為 * 表示執行的時機會是每分鐘的 0, 13, 26, 39, 52 秒時觸發，而我們從輸出可以驗證 Job333 確實如我們預期的時間點執行。

![img](https://dotblogsfile.blob.core.windows.net/user/chris/899f2ad6-7bb1-4ba2-a4f8-e78609455bbf/1608012575.png)

 

 

## 確保網站永遠處於執行狀態

------

由於我們的排程器是附屬於在主要的 ASP.NET Core 應用網站上，所以如果要讓這個排程器永續經營就必須確保該應用網站永遠處於執行的狀態，若該應用網站是部署在 IIS 上就必須特別注意它的回收機制，有可能會造成應用程式中斷的情況產生，這部分許多前輩已經用血淚整理出應對之道，細節請參考黑暗執行緒 [執行定期排程](https://blog.darkthread.net/blog/hangfire-recurringjob-notes/) 文章說明，本文僅簡單列出可設定補強之處。

- 應用程式集區 - 進階設定 - 啟動模式 (Start Mode) = AlwaysRunning
- 站台設定 - 進階設定 - 啟用預載 (Preload Enabled) = True

 

 

## 視覺化管理

------

在排程作業都可以順利運作後，對於維運人員最重要的是可以管理這些作業運行的狀態，因此設計視覺化的介面來了解目前狀態，簡單列一下需求吧。

- 能夠即時看到各作業執行的狀態 (排程中、執行中、停止)。
- 可以針對特定作業手動執行觸發及終止。
- 可以針對整個排程器執行啟動及停止。

 

初步構想就是在 .NET Core 應用網站上加上 Dashboard 頁面來顯示各作業的執行狀態，並且提供一些控制功能。

![img](https://dotblogsfile.blob.core.windows.net/user/chris/899f2ad6-7bb1-4ba2-a4f8-e78609455bbf/1607940383.png)

 

先定義出畫面上顯示資訊用的 JobScheduleSummary 物件類別。

```cs
public class JobScheduleSummary
{

    /// <summary>
    /// Job識別名稱
    /// </summary>
    public string JobName { get; set; }

    /// <summary>
    /// Job類型
    /// </summary>
    /// 
    public string JobType { get; set; }

    /// <summary>
    /// Cron表示式
    /// </summary>
    /// 
    public string CronExpression { get; set; }

    /// <summary>
    /// Job狀態名
    /// </summary>
    /// 
    public string JobStatusName { get; set; }

    /// <summary>
    /// Job狀態碼
    /// </summary>
    /// 
    public JobStatus JobStatusId { get; set; }

}
```

 

 

## 使用 SignalR 即時更新狀態

------

針對排程作業狀態的更新頻率來說，當作業被啟動或結束時會希望立即反映在畫面上，而在排程作業漫長的等待期又是長時間的狀態停滯，因此使用 Timer 一直去 Pulling 資料絕對不會是件好事，而 SignalR 絕對是這類需求的最佳解。

首先建立 SchedulerHub 作為 SignalR 伺服端控管前後端溝通的渠道，能夠接收 client 端的請求，並且也能主動通知 client 狀態異動。由於需要取得排程器的資訊並進行操作，因此注入 QuartzHostedService 服務，藉由此服務對排程器或作業進行操控。

```cs
public class SchedulerHub : Hub
{
    private QuartzHostedService _quartzHostedService;

    /// <summary>
    /// 建構子
    /// </summary>
    /// <param name="quartzHostedService">Quartz排程服務</param>
    public SchedulerHub (QuartzHostedService quartzHostedService)
    {
        _quartzHostedService = quartzHostedService;
    }

    /// <summary>
    /// 要求取得Job狀態
    /// </summary>
    public async Task RequestJobStatus()
    {
        if (Clients != null)
        {
            var jobs = await _quartzHostedService.GetJobSchedules();
            var jobSummary = jobs.Select(e => 
                    new JobScheduleSummary { 
                        JobName = e.JobName, 
                        CronExpression = e.CronExpression, 
                        JobStatusName = e.JobStatus.GetDescription(), 
                        JobStatusId = e.JobStatus, 
                        JobType = e.JobType.FullName 
                    }
                );

            await Clients.Caller.SendAsync("ReceiveJobStatus", jobSummary);
        }
    }

    /// <summary>
    /// 通知Job狀態改變
    /// </summary>
    public async Task NotifyJobStatusChange()
    {
        if (Clients != null)
        {
            await Clients.All.SendAsync("JobStatusChange");
        }
    }

    /// <summary>
    /// 手動觸發Job執行
    /// </summary>
    public async Task TriggerJob(string jobName)
    {
        await _quartzHostedService.TriggerJobAsync(jobName);
    }

    /// <summary>
    /// 手動中斷Job執行
    /// </summary>
    public async Task InterruptJob(string jobName)
    {
        await _quartzHostedService.InterruptJobAsync(jobName);
    }

        
    /// <summary>
    /// 開啟排程器
    /// </summary>
    public async Task StartScheduler()
    {
        await _quartzHostedService.StartAsync(_quartzHostedService.CancellationToken);
    }

    /// <summary>
    /// 關閉排程器
    /// </summary>
    public async Task StopScheduler()
    {
        await _quartzHostedService.StopAsync(_quartzHostedService.CancellationToken);
    }


    /// <summary>
    /// 用戶連線事件
    /// </summary>
    public override async Task OnConnectedAsync()
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, "SignalR Users");
        await NotifyJobStatusChange();
        await base.OnConnectedAsync();
    }


    /// <summary>
    /// 用戶斷線事件
    /// </summary>
    public override async Task OnDisconnectedAsync(Exception exception)
    {
        await Groups.RemoveFromGroupAsync(Context.ConnectionId, "SignalR Users");
        await base.OnDisconnectedAsync(exception);
    }
}
```

 

 

## 監聽器

------

溝通渠道搞定了，接著就是誰能主動通知 Job 及 Scheduler 的變化，好讓排程作業狀態有變動時主動通知 client 端更新顯示的作業狀態；我們可依據 Quartz.NET 定義的 IJobListener 介面來實作 JobListener物件，透過 Job 監聽器來統一提供這些事件，這樣就可以精準掌握各 Job 狀態變化了。以下是實作細節說明。

- 我們在 Job 發生變化時需要操作 SchedulerHub 來通知 client 更新狀態，如果直接注入 SchedulerHub 會造成循環參考 ( JobListener -> SchedulerHub -> QuartzHostedService -> JobListener ... )，所以只能使用 IServiceProvider 透過 GetRequiredService 方法手動從 DI 容器取出物件實體。
- 於本例中只使用到 JobToBeExecuted 及 JobWasExecuted 兩個事件，分別表示 Job 開始執行及結束，這邊要特別注意我們無法在這兩個事件中主動使用 schedulerHub.RequestJobStatus() 發送狀態資訊給前端用戶，因為 Job 會在這兩個事件結束後才會正式進入預期的狀態，所以僅能以 schedulerHub.NotifyJobStatusChange() 通知方式告知 client 狀態已經改變，然後再經由 client 主動向後端取得更新後的狀態。
- JobToBeExecuted：工作將被執行 (當下 Job 狀態尚未進入 Executing 清單)，所以不能直接「主動」傳送當下狀態給 SchedulerHub 送出，因取得的 Job 狀態都還在排程中，非預期的執行中狀態。
- JobWasExecuted：工作執行完畢 (當下 Job 狀態尚未移出 Executing 清單)，所以不能直接「主動」傳送當下狀態給 SchedulerHub 送出，因取得的 Job 狀態都還在執行中，非預期的排程中狀態。

```cs
public class JobListener : IJobListener
{

    private readonly ILogger<JobListener> _logger;

    private readonly IServiceProvider _serviceProvider = null;  // 要用這個來產生 schedulerHub 實體，避免直接注入造成循環參考



    string IJobListener.Name => "Jobs Listener";



    public JobListener(ILogger<JobListener> logger, IServiceProvider serviceProvider)
    {
        _logger = logger;
        _serviceProvider = serviceProvider;
    }



    public async Task JobToBeExecuted(IJobExecutionContext context, CancellationToken cancellationToken = default)
    {
        // 工作將被執行 (目前Job狀態尚未進入Executing清單)

        var jobName = context.JobDetail.Key.Name;
        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - JobToBeExecuted");

        var schedulerHub = _serviceProvider.GetRequiredService<SchedulerHub>();
        await schedulerHub.NotifyJobStatusChange();
         
    }

    public async Task JobWasExecuted(IJobExecutionContext context, JobExecutionException jobException, CancellationToken cancellationToken = default)
    {
        // 工作執行完畢 (目前Job狀態尚未移出Executing清單)

        var jobName = context.JobDetail.Key.Name;
        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - job{jobName} - JobWasExecuted");

        var schedulerHub = _serviceProvider.GetRequiredService<SchedulerHub>();
        await schedulerHub.NotifyJobStatusChange();

    }

    public Task JobExecutionVetoed(IJobExecutionContext context, CancellationToken cancellationToken = default)
    {
        return Task.CompletedTask;
    }

}
```

 

另外，我們也想知道排程器 Scheduler 被啟動或結束的狀態，因此可依據 ISchedulerListener 介面來實作 SchedulerListener 物件。在此我們只關注 Scheduler 啟動或結束相關的事件，因此只需在這些事件中如同 JobListener 處理方式來以 schedulerHub.NotifyJobStatusChange() 通知方式告知 client 狀態已經改變，然後再經由 client 主動向後端取得更新後的狀態。

```cs
public class SchedulerListener : ISchedulerListener
{
    private readonly ILogger<SchedulerListener> _logger;

    private readonly IServiceProvider _serviceProvider = null;  // 要用這個來產生 schedulerHub 實體，避免直接注入造成循環參考



    public SchedulerListener(ILogger<SchedulerListener> logger, IServiceProvider serviceProvider)
    {
        _logger = logger;
        _serviceProvider = serviceProvider;
    }



    public async Task SchedulerShutdown(CancellationToken cancellationToken = default)
    {
        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - SchedulerShutdown");
        var schedulerHub = _serviceProvider.GetRequiredService<SchedulerHub>();
        await schedulerHub.NotifyJobStatusChange();
    }

    public async Task SchedulerShuttingdown(CancellationToken cancellationToken = default)
    {
        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - SchedulerShuttingdown");
        var schedulerHub = _serviceProvider.GetRequiredService<SchedulerHub>();
        await schedulerHub.NotifyJobStatusChange();
    }

    public async Task SchedulerStarted(CancellationToken cancellationToken = default)
    {
        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - SchedulerStarted");
        var schedulerHub = _serviceProvider.GetRequiredService<SchedulerHub>();
        await schedulerHub.NotifyJobStatusChange();
    }

    public async Task SchedulerStarting(CancellationToken cancellationToken = default)
    {
        _logger.LogInformation($"@{DateTime.Now:HH:mm:ss} - SchedulerStarting");
        var schedulerHub = _serviceProvider.GetRequiredService<SchedulerHub>();
        await schedulerHub.NotifyJobStatusChange();
    }

  
    /* ...略... */
}
```

 

接著於 DI 容器中註冊 JobListener、SchedulerListener 及 SchedulerHub 後，加入 SignalR 服務及設定 SignalR Router 就大功告成了。

```cs
public class Startup
{

    public void ConfigureServices(IServiceCollection services)
    {

        //向DI容器註冊Quartz服務
        services.AddSingleton<IJobFactory, JobFactory>();
        services.AddSingleton<ISchedulerFactory, StdSchedulerFactory>();
        services.AddSingleton<IJobListener, JobListener>();  // 註冊 JobListener
        services.AddSingleton<ISchedulerListener, SchedulerListener>();  // 註冊 SchedulerListener


        /* ... 略 ... */

       
        // 註冊DI容器schedulerHub實體
        services.AddSingleton<SchedulerHub>();

        // 設定 SignalR 服務
        services.AddSignalR();
    }

    
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        /* ... 略 ... */

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");

            // 設定 signalR 的 router
            endpoints.MapHub<SchedulerHub>("/schedulerHub");
        });


         
    }
}
```

 

對了，最後最重要的別忘了在 Scheduler 中加入 JobListener 及 SchedulerListener 監聽器。至此 SignalR 伺服端設置已經完成了。

```cs
public class QuartzHostedService : IHostedService
{

    private readonly IJobListener _jobListener;

    private readonly ISchedulerListener _schedulerListener;

    /* ... 略 ... */


    public QuartzHostedService(ILogger<QuartzHostedService> logger, ISchedulerFactory schedulerFactory, IJobFactory jobFactory, IEnumerable<JobSchedule> jobSchedules, IJobListener jobListener, ISchedulerListener schedulerListener)
    {
         _jobListener = jobListener ?? throw new ArgumentNullException(nameof(jobListener));
         _schedulerListener = schedulerListener ?? throw new ArgumentNullException(nameof(schedulerListener));

          /* ... 略 ... */

    }

 
    public async Task StartAsync(CancellationToken cancellationToken)
    {
        // 啟動排程器

        if (Scheduler == null || Scheduler.IsShutdown)
        {
            
            /* ... 略 ... */


            // 初始 scheduler
            Scheduler = await _schedulerFactory.GetScheduler(cancellationToken);
            Scheduler.JobFactory = _jobFactory;
            Scheduler.ListenerManager.AddJobListener(_jobListener);  // 加入 Job 監聽器
            Scheduler.ListenerManager.AddSchedulerListener(_schedulerListener); // 加入 Scheduler 監聽器

            
            /* ... 略 ... */

        }

    }

  /* ... 略 ... */

}
```

 

 

## 前端設置

------

至於前端就只要依照 SignalR 開發方式進行即可，首先在 _Layout.cshtml 中載入所需要的 js 檔案。

[![img](https://dotblogsfile.blob.core.windows.net/user/chris/899f2ad6-7bb1-4ba2-a4f8-e78609455bbf/1608003331.png)](https://dotblogsfile.blob.core.windows.net/user/chris/899f2ad6-7bb1-4ba2-a4f8-e78609455bbf/1608003331.png)

```html
@*加入 signalr.js + vue.js *@
<script src="https://cdnjs.cloudflare.com/ajax/libs/microsoft-signalr/3.1.7/signalr.min.js"></script>
<script src="https://unpkg.com/vue"></script>
<script src="https://unpkg.com/http-vue-loader"></script>
```

 

筆者已經習慣使用 vue / react 進行前端開發，因此本例使用 vue 來完成前端 Home/index.cshtml 的互動。主要就是使用 signalR.HubConnectionBuilder 建立起與後端的連線，接著定義可被後端觸發的事件，以及可以直接呼叫後端 SchedulerHub 方法的動作，程式邏輯約略如下。

```html
@{
    ViewData["Title"] = "Home Page";
}

<div class="text-center">

    <div id="app">
        <h1 class="display-4">System Scheduler</h1>
        <div class="scheduler-actions">
            <button v-on:click="startScheduler" :disabled="!isSchedulerStop">Start Scheduler</button>
            <button v-on:click="stopScheduler" :disabled="isSchedulerStop">Stop Scheduler</button>
            <button v-on:click="refresh">Refresh {{counter}}</button>
        </div>

        <table class="schedule-table">
            <thead class="schedule-table__header">
                <tr>
                    <td align="center">
                        Job Name
                    </td>
                    <td align="center">
                        Job Type
                    </td>
                    <td align="center">
                        CRON
                    </td>
                    <td align="center">
                        Status
                    </td>
                    <td>
                        Actions
                    </td>
                </tr>
            </thead>
            <tr v-for="(job,index) in jobs" :key="index">
                <td align="center">
                    {{job.jobName}}
                </td>
                <td align="center">
                    {{job.jobType}}
                </td>
                <td align="center">
                    {{job.cronExpression}}
                </td>
                <td align="center" :class="isExecuting(job.jobStatusId) ? 'schedule-table--active' : ''">
                    {{job.jobStatusName}}
                </td>
                <td>
                    <button v-on:click="()=>trigger(job.jobName)" :disabled="!isStandby(job.jobStatusId)">Trigger</button>
                    <button v-on:click="()=>Interrupt(job.jobName)" :disabled="!isExecuting(job.jobStatusId)">Interrupt</button>
                </td>
            </tr>
        </table>

        <div class="scheduler-actions">
             {{time}}
        </div>
    </div>
</div>


<script>


    var app = new Vue({
        el: '#app',
        data: {
            connection: null,
            jobs: [],
            counter: 0,
            time: '',
            timeInterval: null
        },
        async mounted() {

            this.connection = new signalR.HubConnectionBuilder()
                .withUrl("/schedulerHub")
                .build();

            // 被後端呼叫接收 Job 目前狀態
            this.connection.on("ReceiveJobStatus", (jobs) => {
                this.jobs = jobs;
                this.counter += 1;
            });

            // 被後端呼叫接收 Job 狀態改變的通知
            this.connection.on("JobStatusChange", () => {
                this.connection.invoke("RequestJobStatus").catch(err => console.error(err));
            });

            this.connection.start().catch(err => console.error(err));

            this.time = this.getTime();
            this.timeInterval = window.setInterval(() => this.time = this.getTime(), 300);
        },
        destroyed() {
            window.clearInterval(this.timeInterval);
        },
        computed: {
            isSchedulerStop() {
                return this.jobs.findIndex(j => j.jobStatusId === 3) > -1
            }
        },
        methods: {
            isExecuting(status) {
                return status === 2;
            },
            isStandby(status) {
                return status === 1;
            },
            refresh() {
                // 呼叫後端提供所有 Job 的狀態
                this.connection.invoke("RequestJobStatus").catch(err => console.error(err));
            },
            trigger(jobName) {
                // 呼叫後端觸發特定Job
                this.connection.invoke("TriggerJob", jobName).catch(err => console.error(err));
            },
            Interrupt(jobName) {
                // 呼叫後端終止特定Job
                this.connection.invoke("InterruptJob", jobName).catch(err => console.error(err));
            },
            startScheduler() {
                // 呼叫後端啟動排程
                this.connection.invoke("StartScheduler").catch(err => console.error(err));
            },
            stopScheduler() {
                // 呼叫後端終止排程
                this.connection.invoke("StopScheduler").catch(err => console.error(err));
            },
            getTime() {
                var dt = new Date();
                var DD = ("0" + dt.getDate()).slice(-2);
                var MM = ("0" + (dt.getMonth() + 1)).slice(-2);
                var YYYY = dt.getFullYear();
                var hh = ("0" + dt.getHours()).slice(-2);
                var mm = ("0" + dt.getMinutes()).slice(-2);
                var ss = ("0" + dt.getSeconds()).slice(-2);
                return YYYY + "-" + MM + "-" + DD + " " + hh + ":" + mm + ":" + ss;
            }
        }
    });


</script>
```

 

 

## 成果發表

------

先回憶一下各工作的執行時機，驗證一下是否能如實呈現各個 Job 工作的狀態。

| **Job Name** | **cron expression** | **remark**                        |
| ------------ | ------------------- | --------------------------------- |
| 111          | 0/30 * * * * ?      | 每分鐘的 0, 30 秒觸發             |
| 222          | 0/52 * * * * ?      | 每分鐘的 0, 52 秒觸發             |
| 333          | 0/13 * * * * ?      | 每分鐘的 0, 13, 26, 39, 52 秒觸發 |
| 444          | 0/20 * * * * ?      | 每分鐘的 0, 20, 40 秒觸發         |

 

各 Job 確實依 cron 設定觸發，並如實地將狀態呈現在頁面上，表示 Listener 及 SignalR 通訊皆正常。

![img](https://i.imgur.com/KOeWthp.gif)

 

可點下 Interrupt 強制中斷作業。

![img](https://i.imgur.com/caz6j4t.gif)

 

可點下 Trigger 觸發作業執行。

![img](https://i.imgur.com/c7tv9he.gif)

 

最後測試關閉排程器及啟動排程器也正常。太棒了，我們終於手把手完成了一個排程器啦！

![img](https://i.imgur.com/0yoPaMq.gif)

 

想要實際體驗同步狀態更新效果的朋友，可開啟多個 [DEMO](https://scheduler20201217142248.azurewebsites.net/) 頁玩玩；完整程式碼請參考筆者 [Github](https://github.com/wasichris/Scheduler) 專案。

 

 

## 後記

------

本文實現了一個 Host 在 .NET Core 應用程式上的排程器，然後又使用 SignalR 技術讓 Dashboard 保持前後端雙向溝通，在初步的使用情境應該是可以滿足了；另外，如果還要延伸處理當然除了一些訪問權限上的管控外，也需要讓 Dashboard 可呈現各個作業相關的 log 紀錄，讓維護人員知道這個排程的過去及未來，是否有確實執行、是否有發生錯誤，甚至也可以考慮在捕捉到 Job Exception 時自動 Mail 通知相關維運人員等，都是可以再延伸應用的部分。

 

 

## 參考資訊

------

[Quartz.NET](https://www.quartz-scheduler.net/)

[在ASP.NET Core中創建基於Quartz.NET託管服務輕鬆實現作業調度](https://www.cnblogs.com/yilezhu/p/12644208.html)

[Hangfire 筆記2 - 執行定期排程](https://blog.darkthread.net/blog/hangfire-recurringjob-notes/)

[Quartz.net 3.x使用總結(一)——簡單使用](https://www.cnblogs.com/wyy1234/p/10278521.html)

 