---
kind: reprint
source: site:www.cnblogs.com
author: liang24 (91suke)
---

# ASP.NET Core Authentication系列（四）基於Cookie實現多應用間單點登錄（SSO）

# 前言

本系列前三篇文章分別從ASP.NET Core認證的三個重要概念，到如何實現最簡單的登錄、註銷和認證，再到如何配置Cookie 選項，來介紹如何使用ASP.NET Core認證。感興趣的可以了解一下。

- [ASP.NET Core Authentication系列（一）理解Claim, ClaimsIdentity, ClaimsPrincipal](https://www.cnblogs.com/liang24/p/13910368.html)
- [ASP.NET Core Authentication系列（二）實現認證、登錄和註銷](https://www.cnblogs.com/liang24/p/13912695.html)
- [ASP.NET Core Authentication系列（三）Cookie選項](https://www.cnblogs.com/liang24/p/13919397.html)

這三篇文章都是從單應用角度來介紹如何使用ASP.NET Core認證，但是在實際開發中，往往都是多應用、分佈式部署的，僅通過上面的內容沒辦法直接應用到多應用上。例如有3個應用，分別對應PC端、移動端和服務端，假設它們的域名分別為www.91suke.com，m.91suke.com以及service.91suke.com，如何讓這三個應用都共享認證。

本文將介紹如何通過共享授權Cookie來實現多應用間單點登錄（SSO）。

源碼下載地址：https://github.com/liang24/SSO

# 如何實現

前面我們已經解決瞭如何使用Cookie來實現認證功能，要實現共享授權Cookie還需要解決以下兩個問題：

1. Cookie共享
2. Cookie的認證票據的解析

第一個問題比較簡單，只要設置Cookie的域為根域，其他子域都能獲得這個Cookie。

```csharp
services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(options =>
    {
        options.Cookie.Name = "TestCookie"; //设置统一的Cookie名称
        options.Cookie.Domain = ".91suke.com"; //设置Cookie的域为根域，这样所有子域都可以发现这个Cookie
    });
```

第二個問題主要是讓多個應用共用解析算法，在ASP.NET Core裡是通過`services.AddDataProtection`配置數據加密保存方式。數據加密配置保存方式現階段ASP.NET Core支持：

- 保存到文件：PersistKeysToFileSystem
- 保存到數據庫：PersistKeysToDbContext
- 保存到Redis：PersistKeysToStackExchangeRedis
- 保存到Azure：PersistKeysToAzureBlobStorage

```csharp
services.AddDataProtection()
    //.PersistKeysToDbContext<SSOContext>()  //把加密数据保存在数据库
    .PersistKeysToFileSystem(new DirectoryInfo(@"C:\server\share\directory\"))  //把加密信息保存大文件夹
    //.PersistKeysToStackExchangeRedis(redis, "DataProtection-Keys")
    .SetApplicationName("SSO"); //把所有子系统都设置为统一的应用名称
```

## 使用PersistKeysToFileSystem

這個方法最簡單，就是把生成的票據保存到磁盤目錄上，多個應用同時訪問這個目錄，達到共享效果。

- 優點：實現簡單，只要應用有目錄權限即可，不需要再配置其他東西。
- 缺點：必須部署在同一台服務器上，無法分佈式部署。

## 使用PersistKeysToDbContext

這個方法是把票據持久化到數據庫，應用只要有訪問數據庫的權限，就能達到共享效果。

- 優點：支持分佈式部署。
- 缺點：在高並發場景下，數據庫IO將會是瓶頸；三種方式裡實現的代碼量是最多的；

## 使用PersistKeysToStackExchangeRedis

這個方法是把票據保存到Redis緩存裡，應用只要有訪問Redis的權限，就能達到共享效果。

- 優點：支持分佈部署，高並發場景。
- 缺點：需要配置額外的緩存服務器。

# 參考資料

- [Share authentication cookies among ASP.NET apps](https://docs.microsoft.com/en-us/aspnet/core/security/cookie-sharing?view=aspnetcore-3.1)
- [Sharing cookies between applications](https://jakeydocs.readthedocs.io/en/latest/security/data-protection/compatibility/cookie-sharing.html)
- [Asp.Net Core基於Cookie實現同域單點登錄(SSO)](https://www.cnblogs.com/liuju150/p/10114778.html)
- [集群環境下，你不得不注意的ASP.NET Core Data Protection 機制](https://www.cnblogs.com/sheng-jie/p/11653196.html)
- [.NET跨平台之旅：ASP.NET Core從傳統ASP.NET的Cookie中讀取用戶登錄信息](https://www.cnblogs.com/cmt/p/5940796.html)
