---
kind: reprint
source: https://www.cnblogs.com/liang24/p/13919397.html
author: liang24 (91suke)
---

# ASP.NET Core Authentication系列（三）Cookie選項

# 前言

在本系列[第一篇文章](https://www.cnblogs.com/liang24/p/13910368.html)介紹了ASP.NET時代如何認證，並且介紹瞭如何通過web.config文件來配置Auth Cookie的選項。

[第二篇文章](https://www.cnblogs.com/liang24/p/13912695.html)介紹瞭如何使用Cookie認證，本文介紹幾個常見的Cookie選項及其用法。

# CookieBuilder

Cookie選項設置主要在`AddCookie`的`CookieAuthenticationOptions.Cookie`：

```javascript
services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(options =>
    {
        options.Cookie.Name = "Name"; // 设置Cookie名称
        options.Cookie.Expiration = new TimeSpan(1, 0, 0); // 有效期1小时
        options.Cookie.Domain = ".91suke.com"; // 设置Cookie域名
    });
```

下面我們具體看一下`CookieAuthenticationOptions.Cookie`的結構：

```csharp
namespace Microsoft.AspNetCore.Http
{
    public class CookieBuilder
    {
        public CookieBuilder();

        public virtual string Domain { get; set; }
        
        public virtual TimeSpan? Expiration { get; set; }
        
        public virtual bool HttpOnly { get; set; }
        
        public virtual bool IsEssential { get; set; }
        
        public virtual TimeSpan? MaxAge { get; set; }
        
        public virtual string Name { get; set; }
        
        public virtual string Path { get; set; }
        
        public virtual SameSiteMode SameSite { get; set; }
        
        public virtual CookieSecurePolicy SecurePolicy { get; set; }

        public CookieOptions Build(HttpContext context);
        
        public virtual CookieOptions Build(HttpContext context, DateTimeOffset expiresFrom);
    }
}
```

常用的幾個選項：

- Domain：Cookie域名，只有相同域名（或子域名）才會攜帶Cookie
- Expiration：Cookie有效期
- Name：Cookie名稱
- Path：Cookie路徑，只有訪問路徑下的子路徑才會攜帶Cookie
- HttpOnly：此屬性為true，則只有在http請求頭中會帶有此cookie的信息，而不能通過document.cookie來訪問此cookie。

# 通過Configuration來設置Cookie選項

在實際開發中，一般不會對選項或配置項硬編碼，因為開發環境與生產環境會有差異。這時候一般會通過配置文件來管理配置項，這樣不需要重新編譯。

在`appsettings.json`裡添加配置項：

```json
{
  // other configuration
  
  "Cookie":{
    "Name" : "TestCookie",
    "Path": "/"
  }
  
  // other configuration
}
```

然後在`Startup`裡設置：

```csharp
services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(options =>
    {
        Configuration.GetSection("Cookie").Bind(options.Cookie);
    });
```

效果圖：

![image](https://yxl-article.oss-cn-shenzhen.aliyuncs.com/images/cookiebuilder-configuration.png)
