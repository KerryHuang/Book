# ASP.NET Core 呼叫 API 發生 CORS 錯誤

假設使用 ASP.NET Core 6 建立了一個 API ， 連結為 http://localhost:8080/user ，使用 Post 方法，需要在 Body 中帶入資料，在 Postman 中可以正常呼叫和取得回應，但是在別的網站上無法呼叫，在瀏覽器的開發人員工具的主控台中出現了下面的錯誤:

Firefox 錯誤訊息:

```log
已封鎖跨來源請求: 同源政策不允許讀取 http://localhost:8080/user 的遠端資源。（原因: 缺少 CORS 'Access-Control-Allow-Origin' 檔頭）。狀態代碼: 302。

已封鎖跨來源請求: 同源政策不允許讀取 http://localhost:8080/user 的遠端資源。（原因: CORS 請求未成功）。狀態代碼: (null)。
```

Log file

Copy

Chrome 錯誤訊息:

```log
POSThttp://localhost:8080/user net::ERR_FAILED

Access to XMLHttpRequest at 'http://localhost:8080/user' from origin 'http://localhost:5173' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: Redirect is not allowed for a preflight request.
```

Log file

Copy

## CORS 是什麼?

依據 mdn 上的說法， CORS(Cross-Origin Resource Sharing) 是跨來源資源共用，只要網域(domain)、通訊協定(protocol)或通訊埠(port) 不同時，就會產生跨來源 HTTP 請求(cross-origin HTTP request)。

CORS 是一個 Web 標準，用來限制瀏覽器從不同來源請求資源，只要瀏覽器檢查到不同來源的資源請求，就會進行檢查，確保使用者的資料安全。若該請求不為[簡單請求](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS#簡單請求)（simple requests），則會觸發 CORS 預檢，發送一個 OPTIONS 請求，稱為預檢請求(Preflight Request)，驗證**伺服器回應**的訊息中是否包含 Access-Control-Allow-Origin (所以瀏覽器中才會有兩個錯誤)，由此確認伺服器是否允許本網頁跨來源請求資源。如果預檢請求沒有通過，確認目標伺服器拒絕本網頁跨來源請求資源，則不會發送原本請求。

而 Postman 不是瀏覽器，不受 CORS 策略的限制，所以使用 Postman 沒有 CORS 問題，不代表就沒有 CORS 問題，因為這個問題是瀏覽器為了安全而限制的。

所以通常遇到 CORS 問題時，不是呼叫 API 的客戶端(如網頁)的問題，而是伺服器端的問題(如 ASP.NET Core)，前端工程師可以鬆一口氣，直接把問題甩到後端工程師身上(誤)。

## ASP.NET Core 6 解決 CORS 的方式

- **WithOrigins**
  設定允許跨域的來源，有多個的話可以用 `,` 隔開。
  若要同意所有跨域來源都能呼叫的話，可以把 `WithOrigins()` 改為 `AllowAnyOrigin()`。
- **AllowAnyHeader**
  允許任何的 Request Header。若要限制 Header，可以改用 `WithHeaders`，有多個的話可以用 `,` 隔開。
- **AllowAnyMethod**
  允許任何的 HTTP Method。若要限制 Method，可以改用 `WithMethods`，有多個的話可以用 `,` 隔開。
- **AllowCredentials**
  預設瀏覽器不會發送 CORS 的憑證(如：Cookies)，如果 JavaScript 使用 `withCredentials = true` 把 CORS 的憑證帶入，ASP.NET Core 這邊也要允取，才可以正常使用。

在 var app = builder.Build(); 前加入下面的程式碼:

```csharp
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(builder =>
    {
        builder
        	.AllowAnyOrigin() // 允許任何來源
            .AllowAnyMethod()
            .AllowAnyHeader();
    });
});
```

Program.cs

或是要設定只能允許幾個來源，可以將第六行替換，就可以以白名單的形式設定

```csharp
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(builder =>
    {
        builder
        	.WithOrigins("http://localhost:5173", "https://localhost:44300") // 只允許這兩個來源
            .AllowAnyMethod()
            .AllowAnyHeader();
    });
});
```

Program.cs

## 套用 Policy

套用 Policy 有兩種方式：

1. 全域套用
2. 區域套用

### 全域套用

最後在 UseRouting 後面和 UseEndpoints 前面加入 UseCors 即可，程式碼如下:

```csharp
var app = builder.Build();
app.UseRouting();

app.UseCors();

app.UseEndpoints();
```

Program.cs

若沒有 UseEndpoints 則可以忽略。

### 區域套用

可以在 Controller 或 Action 掛上 `[EnableCors("Policy 名稱")]`，套用 Policy 到 Controller 或 Action 上。

- **Controller**

```cs
// ...
[EnableCors("CorsPolicy")]
public class HomeController : Controller
{
    // ...
}
```

- **Action**

```cs
// ...
public class HomeController : Controller
{
    [EnableCors("CorsPolicy")]
    [Route("cors-sample")]
    public ResultModel Test()
    {
        // ...
    }
}
```

在 ASP.NET Core 允取 CROS 後，完整的情境如下：

![[鐵人賽 Day26] ASP.NET Core 2 系列 - 跨域請求 (Cross-Origin Requests) - 情境 2](https://blog.johnwu.cc/images/i26-2.png)

再次重新發送請求時就不會再出現 CORS 錯誤了！