# ASP.NET Core Authentication系列（二）實現認證、登錄和註銷

# 前言

在[上一篇文章](https://www.cnblogs.com/liang24/p/13910368.html)介紹ASP.NET Core Authentication的三個重要概念，分別是Claim, ClaimsIdentity, ClaimsPrincipal，以及claims-base authentication是怎麼工作的。

這篇文章來介紹一下如何基於claims-base authentication來實現認證、登錄和註銷功能的。源代碼從[這裡](https://yxl-article.oss-cn-shenzhen.aliyuncs.com/files/CookieAuthenticationDemo.zip)下載。

# 認證票據

認證是一個確定發送請求的訪問者身份的過程，與認證相關的還有另外兩個基本操作：登錄和註銷。

ASP.NET Core應用的認證實現在一個名為`AuthenticationMiddleware`的中間件中，該中間件在處理分發給它的請求時會按照指定的**認證方案（Authentication Scheme）**從請求中提取能夠驗證用戶真實身份的數據，我們一般將該數據稱為**安全令牌（Security Token）**。ASP.NET Core應用下的安全令牌被稱為**認證票據（Authentication Ticket）**，所以ASP.NET Core應用採用基於票據的認證方式。

`AuthenticationMiddleware`中間件的整個認證過程涉及下圖的三種操作：認證票據的頒發、檢驗和撤銷。

![image](https://img2020.cnblogs.com/blog/19327/202003/19327-20200325083708342-258956203.png)

ASP.NET Core應用的認證系統旨在構建一個標準的模型來完成針對請求的認證以及與之相關的登錄和註銷操作。接下來我們就通過一個簡單的實例來演示如何在一個ASP.NET Core應用中實現認證、登錄和註銷的功能。

# 基於Cookie的認證

大多數Web應用採用的是Cookie來保存認證票據，因此我們採用基於Cookie的認證方案。

## 配置

在`Startup.ConfigureServices`方法裡，添加`AuthenticationMiddleware`中間件：

```scss
services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie();
```

然後在`Startup.Configure`方法裡，調用`UseAuthentication`和`UseAuthorization`來設置`HttpContext.User`屬性以及允許請求經過`AuthenticationMiddleware`，並且要在`UseEndpoints`之前調用：

```cpp
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...
    
    app.UseAuthentication();
    app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllerRoute(
            name: "default",
            pattern: "{controller=Home}/{action=Index}/{id?}");
    });
        
    // ...
}
    
```

## 登錄

接下來實現登錄方法，常見是使用“用戶名+密碼”，這裡使用一個靜態字典來模擬用戶表。

```csharp
public class AccountController : Controller
{
    // ....

    private static Dictionary<string, string> _accounts;

    static AccountController()
    {
        _accounts = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        _accounts.Add("Foo", "password");
        _accounts.Add("Bar", "password");
        _accounts.Add("Baz", "password");
    }

    [HttpGet]
    public IActionResult Login()
    {
        LoginModel model = new LoginModel();

        return View(model);
    }

    [HttpPost]
    public async Task<IActionResult> Login(LoginModel model)
    {
        if (_accounts.TryGetValue(model.UserName, out var pwd) && pwd == model.Password)
        {
            var claimsIdentity = new ClaimsIdentity(
                new Claim[] { new Claim(ClaimTypes.Name, model.UserName) }, "Basic");
            var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);                
            await HttpContext.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme, claimsPrincipal);

            return Redirect("/");
        }
        else
        {
            model.ErrorMessage = "Invalid user name or password!";

            return await Task.Run(() => View(model));
        }
    }

    // ....
}
```

這段代碼的關鍵在於下面三行代碼：

1. 創建ClaimType為Name，值為用戶名的Claim。
2. 創建ClaimsIdentity，注意AuthorizeType="Basic"。
3. 創建ClaimsPrincipal。
4. 調用HttpContext.SignInAsync登錄，其中認證方案為CookieAuthenticationDefaults.AuthenticationScheme，與配置時一致。

```csharp
var claimsIdentity = new ClaimsIdentity(
    new Claim[] { new Claim(ClaimTypes.Name, model.UserName) }, "Basic");
var claimsPrincipal = new ClaimsPrincipal(claimsIdentity); 
await HttpContext.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme, claimsPrincipal);
```

## 認證

需要授權訪問的功能要驗證登錄狀態，如果沒有登錄則不允許訪問，使用方法很簡單，只需要在`Action`上加上特性`[Authorize]`：

```csharp
[Authorize]
public IActionResult Index()
{
    return View();
}
```

未登錄會跳轉到/Account/Login（默認設置，可修改），避免未授權訪問。

## 註銷

用戶註釋，即將具有認證票據的Cookie設置為過期，直接調用`HttpContext.SignOutAsync`，注意認證方案要與配置和登錄的一致：`CookieAuthenticationDefaults.AuthenticationScheme`

```csharp
public class AccountController : Controller
{
    // ....

    public async Task<IActionResult> Logout()
    {
        _logger.LogInformation("User {Name} logged out at {Time}.",
                User.Identity.Name, DateTime.UtcNow);

        await HttpContext.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);

        return Redirect("/");
    }
    
    // ....
}
```

# 參考資料

- [Exploring the cookie authentication middleware in ASP.NET Core](https://andrewlock.net/exploring-the-cookieauthenticationmiddleware-in-asp-net-core/)
- [用最簡單的方式在ASP.NET Core應用中實現認證、登錄和註銷](https://www.cnblogs.com/artech/p/authentication-sign-in-out.html)
- [Use cookie authentication without ASP.NET Core Identity](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/cookie?view=aspnetcore-3.1#)
