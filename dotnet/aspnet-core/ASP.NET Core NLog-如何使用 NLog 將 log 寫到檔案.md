---
kind: reprint
source: site:blogspot.com
---

雖然有過對於專案設定 NLog 的經驗，但時間一久，每次面對新的專案只剩下印象，實作時還需要翻些文章，才能順利建立。這邊簡單做一下筆記，方便自己之後建立新專案時參考。本篇文章若有錯誤或任何建議，請各位先進不吝指教。

點選上方 工具 (Tools) > NuGet 套件管理員 (NuGet Package Manager) > 管理方案 NuGet 套件(Manage NuGet Packages for Solution)

![img1](https://1.bp.blogspot.com/-gEzyMtUT2TM/Xrj5r42d0QI/AAAAAAAAmoo/Uxra-SonwTgGxRdn32e-VaVsKIvf4W23wCK4BGAsYHg/w640-h292/302.png)

瀏覽頁簽內的搜尋框輸入 nlog，即可以找到相關套件。我們這次要安裝的套件有三個，分別是： NLog、NLog.Config 與 NLog.Web.AspNetCore
![img2](https://1.bp.blogspot.com/-Lgun9drVoFI/Xrj6oy5TlvI/AAAAAAAAmpE/ePMqDYla9Po2YjGhve0aW7ZxqdPPIPDywCK4BGAsYHg/w640-h414/301.png)

先開啟專案中的 Program.cs，如下方圖片加入 .UseNLog();
![img3](https://1.bp.blogspot.com/-vPFtzUDJCSY/Xrj720sZOPI/AAAAAAAAmpk/27zc-iYq07crgy6sH1SwRfnHVhIBYoncACK4BGAsYHg/w640-h356/303.png)

Main 內修改如下圖
![img4](https://1.bp.blogspot.com/-DGZcMupoaCk/XrkBfHAEBeI/AAAAAAAAmqc/wSfF8fYl5cM_7iXzmuEJZr-Pbd6PfBUvwCK4BGAsYHg/w640-h530/305.png)

完整程式碼如下：
```c#
public class Program
    {
        public static void Main(string[] args)
        {
            var logger = NLogBuilder.ConfigureNLog("nlog.config").GetCurrentClassLogger();
            try
            {
                logger.Debug("init main");
                CreateHostBuilder(args).Build().Run();
            }
            catch (Exception ex)
            {
                logger.Error(ex, "Stopped program because of exception");
                throw;
            }
            finally
            {
                NLog.LogManager.Shutdown();
            }
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                }).UseNLog();
    }
```
找到並右鍵點選 NLog.config，選擇屬性 (Properties) ，將 複製到輸出目錄 (Copy to Output Directory) 選擇 永遠複製  (Copy always)

![img5](https://1.bp.blogspot.com/-vl1EEYySxQ8/Xrj_uMje7NI/AAAAAAAAmqA/SxjbOwDVyzIdGDFVrCX5tal1X1w06rEKwCK4BGAsYHg/w640-h484/304.png)



接下來打開 NLog.config，你能看到許多註解，這些都是基本的設定範例。

首先我們先看一下 targets (目標) 設定：
**xsi:type**: 寫入log 格式，File 表示將log 寫入檔案
**fileName**: 為寫入檔案的位置， ${basedir} 為專案資料夾
layout: 為寫出的格式，這邊格視為時間、大寫 Log level與 log 內容 (meassage)
接下來我們看一下 rules (規則)設定
**logger name**: 可以設定寫出那些 logger，* 表示全部都寫
**minlevel**: 表示寫出log的層級
**writeTo**: 表示寫出位置，f 表示檔案 (對應上面 target name=f)
**我們將 NLog.config 內 targets 與 rules 註解拿掉**

![img6](https://1.bp.blogspot.com/-l6h4tUdtNlI/XroNAwjA3CI/AAAAAAAAmq8/AAFhHR3xs6k9V1uuWz-ewfSEbRF3RlGUgCK4BGAsYHg/w640-h448/306.png)

使用 nlog 有兩種方式：直接使用 與 注入使用，直接使用的方式在上面有提到 (加入到 Program.cs 內容) 只需要 var logger = NLogBuilder.ConfigureNLog("nlog.config").GetCurrentClassLogger(); 取得目前 Logger，再透過 logger.Debug("init main"); 寫入 log 即可

另一種方式是注入方式，無論在 controllers 或 services 於建構子注入後即可使用：
![img7](https://1.bp.blogspot.com/-t1Cn__9ywlY/XroP6raSfeI/AAAAAAAAmrY/HSDbUDR407YFHKr2qAaQcr1n3PoCt93iwCK4BGAsYHg/w640-h294/307.png)

完成設定後啟動專案，你能在專案目錄下 (\bin\Debug\netcoreapp3.1\logs) 下找到 log
![img8](https://1.bp.blogspot.com/-Rpd0MLutypg/XroRLMCUflI/AAAAAAAAmr0/GN5GnxSIJuQKbdoQAnSZ_o0SjoH2EK9ngCK4BGAsYHg/w640-h234/308.png)

幾乎所有 Log 機制都有所謂的 LogLevel，區分為 Trace、Debug、Information、Warn、Error、Critical... 等不同等級。借用微軟的[定義](https://learn.microsoft.com/zh-TW/dotnet/api/microsoft.extensions.logging.loglevel?view=dotnet-plat-ext-6.0&WT.mc_id=DOP-MVP-37580)說明各等級的適用場合：

- None/Off
  不記錄
- Trace
  包含最詳細訊息的記錄，訊息可能包含敏感性應用程式資料。預設停用，且永遠不應在生產環境中啟用。
- Debug
  開發期間用於互動式調查用，主要包含用於偵錯的資訊，不具備任何長期價值。
- Information/Info
  追蹤應用程式一般流程的記錄，應具備長期價值。
- Warning
  醒目提示應用程式異常或未預期事件，但這些異常或未預期事件不會造成應用程式執行停止。
- Error
  在目前執行流程因失敗而停止時進行醒目提示的記錄，記錄應著重目前活動的失敗資訊細節，而非整個應用程式的失敗。
- Critical/Fatal
  描述無法復原的應用程式或系統損毀，或需要立即注意重大失敗的記錄。

### 參考資料
1. [Nlog詳解](https://www.cnblogs.com/1175429393wljblog/p/16576726.html)
1. [C#：NLog接入配置與簡單使用]([https://zhuanlan.zhihu.com/p/610461723)