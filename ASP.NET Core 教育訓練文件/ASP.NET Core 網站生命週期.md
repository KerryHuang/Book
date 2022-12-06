ASP.NET MVC 是一個網站服務，使用者輸入網址後，顯示網頁到使用者的瀏覽器上面，而生命週期就是在解釋當使用者輸入網址之後，背後運行的流程，中間經過哪些事件，最後把網頁呈現出來的過程。

理解 ASP.NET MVC 的生命週期就可以同時理解網站的運行機制，大多數的網站生命週期都是類似的，而 MVC 是一個適合專責分工的架構，從生命週期的角度更能了解 MVC 運行的過程。

在 ASP.NET MVC 上有兩個主要的生命週期：

應用程式生命週期
請求生命週期
我剛剛所講述的使用者輸入網址到呈現網頁，這是請求的生命週期，主要觸發點是使用者在瀏覽器上發出請求而啟動的。
另一個應用程式的生命週期，指的是網站服務的運作機制，從架設網站啟動服務開始，等待使用者請求，到最後結束應用程式，這是網站底層運作的生命週期。


##### 目錄  
[應用程式生命週期介紹](#Step1)
[請求生命週期介紹](#Step1)

<a name="Step1"/>
## 應用程式生命週期介紹

ASP.NET MVC 是運行在 .NET Framework 架構之上，在 .NET Framework 有一個 Web 基礎類別 HttpApplication 定義了共有的方法、屬性和事件，同時負責分發請求事件，而 HttpApplication 也是 WebForm 的基礎類別，可以說 HttpApplication 類別是整個 ASP.NET MVC 與 WebForm 架構的核心。

應用程式生命週期在啟動後會執行一個 Application_Start() 方法，然後就一直等待使用者請求，當請求來時會啟動對應的事件觸發，結束請求後就會繼續等待下一個請求到來，直到結束應用程式。

用一張圖來表達應用程式生命週期。
![Img](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-1.png)
在 MVC 專案內有一檔案 Global.asax 裡面有最初始的應用程式生命週期事件: `Application_Start()`
![Img2](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-2.png)

在 `Application_Start()` 事件內載入了 Area, Filter, Route 與 Boundle 這 4 種註冊表在 ASP.NET MVC 服務內。
除了 `Application_Start()` 之外，還有另外 19 個請求事件可以使用。
以下的事件名稱會依照請求發生時依此順序執行。

|事件名稱	|簡單描述|
|------------|:----------|
|BeginRequest|在 ASP.NET 響應請求時作為 HTTP 執行管線鏈中的第一個事件發生|
|PostAuthenticateRequest|當安全模組已建立使用者標識時發生。PostAuthenticateRequest 事件在 AuthenticateRequest 事件發生之後引發。預訂 PostAuthenticateRequest 事件的功能可以訪問由 PostAuthenticateRequest 處理的任何資料|
|AuthorizeRequest|當安全模組已驗證使用者授權時發生。AuthorizeRequest 事件發出訊號表示 ASP.NET 已對當前請求進行了授權。預訂 AuthorizeRequest 事件可確保在處理附加的模組或事件處理程式之前對請求進行身份驗證和授權|
|PostAuthorizeRequest|在當前請求的使用者已獲授權時發生。PostAuthorizeRequest 事件發出訊號表示 ASP.NET 已對當前請求進行了授權。預訂PostAuthorizeRequest 事件可確保在處理附加的模組或處理程式之前對請求進行身份驗證和授權|
|ResolveRequestCache|當 ASP.NET 完成授權事件以使快取模組從快取中為請求提供服務時發生，從而跳過事件處理程式（例如某個頁或 XML Web services）的執行|
|PostResolveRequestCache|在 ASP.NET 跳過當前事件處理程式的執行並允許快取模組滿足來自快取的請求時發生。）在 PostResolveRequestCache 事件之後、PostMapRequestHandler 事件之前建立一個事件處理程式|
|PostMapRequestHandler|在 ASP.NET 已將當前請求對映到相應的事件處理程式時發生。|
|AcquireRequestState|當 ASP.NET 獲取與當前請求關聯的當前狀態（如會話狀態）時發生。|
|PostAcquireRequestState|在已獲得與當前請求關聯的請求狀態（例如會話狀態）時發生。|
|PreRequestHandlerExecute|恰好在 ASP.NET 開始執行事件處理程式（例如，某頁或某個 XML Web services）前發生。|
|PostRequestHandlerExecute|在 ASP.NET 事件處理程式（例如，某頁或某個 XML Web service）執行完畢時發生。|
|ReleaseRequestState|在 ASP.NET 執行完所有請求事件處理程式後發生。該事件將使狀態模組儲存當前狀態資料。|
|PostReleaseRequestState|在 ASP.NET 已完成所有請求事件處理程式的執行並且請求狀態資料已儲存時發生。|
|UpdateRequestCache|當 ASP.NET 執行完事件處理程式以使快取模組儲存將用於從快取為後續請求提供服務的響應時發生。|
|PostUpdateRequestCache|在 ASP.NET 完成快取模組的更新並儲存了用於從快取中為後續請求提供服務的響應後，發生此事件。|
|LogRequest|在 ASP.NET 完成快取模組的更新並儲存了用於從快取中為後續請求提供服務的響應後，發生此事件。
僅在 IIS 7.0 處於整合模式並且 .NET Framework 至少為 3.0 版本的情況下才支援此事件|
|PostLogRequest|在 ASP.NET 處理完 LogRequest 事件的所有事件處理程式後發生。
僅在 IIS 7.0 處於整合模式並且 .NET Framework 至少為 3.0 版本的情況下才支援此事件。|
|EndRequest|在 ASP.NET 響應請求時作為 HTTP 執行管線鏈中的最後一個事件發生。
在呼叫 CompleteRequest 方法時始終引發 EndRequest 事件。|

使用事件的方式就是創建一方法，方法命名規則為 Application_{事件名稱}，例如：
![img3](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-3.png)
如果你有額外的邏輯要處理，就可以建立這些請求事件來執行額外的功能。

## 請求生命週期介紹
請求生命週期指的是 MVC 的運作機制，從使用者在瀏覽器上輸入網址發出請求開始，執行 Routing 解析網址，然後呼叫對應的 Controller 來處理請求，中間啟動 Action 服務到最後呈現網頁到瀏覽器的過程。

用一張圖來表達這樣的流程。
![img4](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-4.png)

MVC 指的是 Model – Controller – View 這三層架構，是一種權責分離的架構，不同層級處理不同的工作。
當請求發生時第一個會啟動 Routing 來解析請求，我們在 Application_Start() 裡面看到會載入 Route 註冊表 RouteConfig.RegisterRoutes(RouteTable.Routes);

![img5](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-5.png)
而 Route 註冊表預設放在 \App_Start\RouteConfig.cs 裡面。
這裡面寫了 Route 的規則，也就是解析網址的規則，第一個路徑指的是 Controller，第二個路徑是 Action ，第三個就是參數值。

![img6](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-6.png)
在 Route 內的目的就是解析要負責處理的 Controller 是那一個。

Controller 是 MVC 的起始入口，Action 是 Controller 內的方法，過程中從 Model 讀取資料，最後產生 View 頁面回傳到使用者的瀏覽器。

我用一張圖來描述 MVC 內會使用到的類別名稱。
![img7](https://blog.hungwin.com.tw/wp-content/uploads/2022/02/aspnet-mvc-life-cycle-7.png)

MVC 整體流程是照著箭頭在走的，圖片寫了各種在 MVC 架構內的類別名稱和事件名稱，大多可以在 MVC 的底層內找到對應的程式碼。

而我們在寫 MVC 程式時，主要的入口程式碼會寫在 Action 裡面。
我們建立 MVC 專案時，預設首頁的 Action 就在 HomeController 的 Index() ，在處理 Action 的過程中有必要時會載入 Model 物件，最後完成時 Return View() 也就是結束 Action 事件，轉交 Result 來處理呈現結果。

Result 依需求可能會載入 View 頁面也可能直接輸出文字就不載入 View 頁面。

在 Action Execution 裡面看到的 Filter 這是過濾器的機制，如果 Action 或 Controller 有啟用過濾器 (Filter) 就會依照箭頭的順序來執行。