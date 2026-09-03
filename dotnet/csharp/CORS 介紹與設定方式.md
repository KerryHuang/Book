---
kind: original
---

# CORS 介紹與設定方式

### 什麼是 CORS？

**CORS（Cross-Origin Resource Sharing，跨來源資源共享）** 是一種瀏覽器的安全機制，用於控制網頁如何從不同的域名請求資源。當網頁發送 AJAX 請求（例如使用 `fetch()` 或 `XMLHttpRequest`）到與原始網頁不同的域（domain）、協議（protocol）或端口（port）時，會發生所謂的「跨來源請求」。CORS 機制允許服務器明確聲明哪些域名可以訪問它的資源，以及允許哪些 HTTP 方法和標頭。

預設情況下，瀏覽器會阻止這些跨來源請求，因為它們可能引起安全問題。為了解決這個問題，CORS 為合法的跨域請求提供了途徑。

### CORS 的作用

1. **允許的域**：通過 `Access-Control-Allow-Origin` 標頭，服務器可以指定允許的來源域。
2. **預檢請求（Preflight Request）**：對於一些非簡單請求（如使用 `PUT`, `DELETE`，或自訂標頭），瀏覽器會發送「預檢請求」，先詢問服務器是否允許該操作。
3. **允許的 HTTP 方法和標頭**：可以控制哪些 HTTP 方法（`GET`, `POST`, `PUT`, `DELETE`）和哪些自訂的標頭允許跨域使用。

### 在 .NET 中如何設定 CORS

#### 步驟 1：安裝 CORS 支援

在 .NET 6 或 .NET 8 中，CORS 已經內建，不需要額外安裝套件。您只需要在 `Program.cs` 或 `Startup.cs` 中進行配置即可。

#### 步驟 2：啟用和配置 CORS

在 `.NET 8` 中，您可以通過 `services.AddCors()` 來啟用 CORS，並使用 `UseCors` 來配置允許的來源、方法和標頭。

```csharp
var builder = WebApplication.CreateBuilder(args);

// 配置 CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowSpecificOrigins",
        builder =>
        {
            builder.WithOrigins("https://example.com") // 允許的來源
                   .AllowAnyHeader() // 允許所有標頭
                   .AllowAnyMethod(); // 允許所有方法
        });
});

var app = builder.Build();

// 啟用 CORS
app.UseCors("AllowSpecificOrigins");

app.MapControllers();

app.Run();
```

#### 步驟 3：允許所有來源（不推薦於生產環境使用）

在開發過程中，有時您可能想要暫時允許所有的來源進行跨域請求。這可以使用 `.AllowAnyOrigin()` 設定：

```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAllOrigins",
        builder =>
        {
            builder.AllowAnyOrigin()
                   .AllowAnyHeader()
                   .AllowAnyMethod();
        });
});

app.UseCors("AllowAllOrigins");
```

#### 步驟 4：設定預檢緩存時間（可選）

若您想要減少瀏覽器對服務器的預檢請求次數，可以設定預檢緩存時間：

```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowSpecificOrigins",
        builder =>
        {
            builder.WithOrigins("https://example.com")
                   .AllowAnyHeader()
                   .AllowAnyMethod()
                   .SetPreflightMaxAge(TimeSpan.FromMinutes(10)); // 設定預檢緩存時間
        });
});
```

#### 步驟 5：限制 HTTP 方法

您可以限制特定的 HTTP 方法來控制哪些操作允許跨域請求：

```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowSpecificOrigins",
        builder =>
        {
            builder.WithOrigins("https://example.com")
                   .WithMethods("GET", "POST") // 只允許 GET 和 POST 方法
                   .AllowAnyHeader();
        });
});
```

#### 步驟 6：在 Controller 中指定 CORS（可選）

如果只想在某些控制器或動作方法中啟用 CORS，可以使用 `[EnableCors]` 屬性來控制：

```csharp
[ApiController]
[Route("api/[controller]")]
public class SampleController : ControllerBase
{
    [HttpGet]
    [EnableCors("AllowSpecificOrigins")]
    public IActionResult Get()
    {
        return Ok("這是一個跨域的回應");
    }
}
```

#### 步驟 7：禁用 CORS（可選）

如果某些路由不需要跨域支援，可以用 `[DisableCors]` 禁用 CORS。

```csharp
[DisableCors]
[HttpGet]
public IActionResult NoCorsEndpoint()
{
    return Ok("CORS 被禁用");
}
```

### 總結

CORS 是一種安全機制，能有效防止瀏覽器發起不受控制的跨域請求。在 .NET 中，可以通過 `AddCors()` 和 `UseCors()` 配置並啟用 CORS，並根據需要設定允許的來源、方法、標頭等。配置正確的 CORS 能保護應用程式的安全，同時允許合法的跨域訪問。