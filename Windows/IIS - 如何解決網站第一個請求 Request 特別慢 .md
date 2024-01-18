## [[IIS\] 如何解決網站第一個請求 Request 特別慢 ?](https://marcus116.blogspot.com/2018/12/why-iis-application-so-slow-on-first-request.html)

[12月 18, 2018](https://marcus116.blogspot.com/2018/12/why-iis-application-so-slow-on-first-request.html)[.NET](https://marcus116.blogspot.com/search/label/.NET), [IIS](https://marcus116.blogspot.com/search/label/IIS)[No comments](https://marcus116.blogspot.com/2018/12/why-iis-application-so-slow-on-first-request.html#comment-form)

**問題**
相信大家都有類似的經驗，在寫完的 Code 佈署到 IIS 開好網頁要準備要進入網站要測試時，網站的第一個請求總是特別慢，尤其是開發已久的程式要在 Production 驗證時心情總是特別緊張，這等待的時間更是讓人很煎熬(不知道會不會爆炸 XD)，如何加速網站第一個 Request 呢 ? 過去待過的公司會在佈署完後透過 Jenkins 去打 Server 來 "喚醒" 它，在此簡單記錄一下如何透過 IIS 設定加速網站第一個 Request 的過程

**處理方式** 
IIS 8.0 開始提供 **網站預先啟動功能 (Preload)**，主要是透過 Application Initialization模組改善了網站第一位使用者等待網站初始化動作過久的問題，讓 IIS 啟動網站時先進行 Application 的初始化動作，加快 Response 回應時間，設定方式如下

**安裝 Application Initialization feature**
如果要啟用的話需要先檢查是否有安裝 Application Initialization feature，檢查方式如下 

1. 開啟控制台 > 程式集 > 開啟或關閉 Windows 功能 
2. Internal Information Service > WWW 服務 > 應用程式開發功能 
3. 應用程式初始化選項打勾



[![img](https://3.bp.blogspot.com/-dB27J4d-t9I/XBj3RPhZpjI/AAAAAAAAFYE/gpU1Ozy24mM2VQcF_3LqhkKtHiaHnSwOwCLcBGAs/s400/IIS.png)](https://3.bp.blogspot.com/-dB27J4d-t9I/XBj3RPhZpjI/AAAAAAAAFYE/gpU1Ozy24mM2VQcF_3LqhkKtHiaHnSwOwCLcBGAs/s1600/IIS.png)


**設定 IIS**

1. 開啟要設定的 Application 應用程式，點選 **進階設定**



2. 可以看到 **預先載入已啟用** 功能 設定為 True 

Note : 下方說明可以看到，preloadEnable 為 True 時，就會啟用應用程式的預先載入功能

[![img](https://2.bp.blogspot.com/-8-e-qFSTGRk/XBj6OqRwqII/AAAAAAAAFYQ/K6m1F1CFKegqdSK5qif5SE3hjDdyWgw9ACLcBGAs/s400/IIS2.png)](https://2.bp.blogspot.com/-8-e-qFSTGRk/XBj6OqRwqII/AAAAAAAAFYQ/K6m1F1CFKegqdSK5qif5SE3hjDdyWgw9ACLcBGAs/s1600/IIS2.png)

3. 接下來到應用程式集區
4. 點選要設定的 Application Pool，選擇 **進階設定**



5. 啟用模式原本是 OnDemand，選擇 **AlwaysRunning**，按下確定

Note : 下方說明可以看到，[startMode] 設定應用程式集區要以 隨選 或是 永遠執行 模式執行

[![img](https://4.bp.blogspot.com/-3V9Imjl7Aqo/XBj8GEfjlHI/AAAAAAAAFYc/Hq541B1OWwMW95mi2lRb3-E2SHblDnpKgCLcBGAs/s400/iis3.jpg)](https://4.bp.blogspot.com/-3V9Imjl7Aqo/XBj8GEfjlHI/AAAAAAAAFYc/Hq541B1OWwMW95mi2lRb3-E2SHblDnpKgCLcBGAs/s1600/iis3.jpg)

如果是IIS 7.5的話，需要另外下載 [Application W](https://www.iis.net/downloads/microsoft/application-initialization)[arming up](https://www.iis.net/downloads/microsoft/application-initialization) 模組
設定方式也是類似上述步驟，詳細可以參考 Michelle哥 Blog 詳細說明 
[ASP.NET 程式中的背景工作 (1)](https://www.huanlintalk.com/2014/03/writing-aspnet-background-tasks.html)

打完收工，大功告成 !

**參考**
[IIS 8.0 Application Initialization](https://docs.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/iis-80-application-initialization)
[ASP.NET開發人員不可不知的 IIS](https://docs.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/iis-80-application-initialization)
[iis8-preloaded](https://blog.ite2.com/iis8-preloaded/)