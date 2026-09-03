---
kind: reprint
source: https://www.faciletechnolab.com/blog/2021/4/13/how-to-implement-azure-ad-authentication-in-aspnet-core-50-web-application
---

## [如何在 ASP.NET CORE 5.0 WEB 應用程序中實現 AZURE AD 身份驗證](https://www.faciletechnolab.com/blog/2021/4/13/how-to-implement-azure-ad-authentication-in-aspnet-core-50-web-application#)


在本文中，我將向您展示如何在 ASP.NET Core 5.0 Web 應用程序中實現 Azure AD 身份驗證。我將創建 ASP.NET Core 5.0 項目，並逐步向您展示如何使用它來針對 Azure AD 身份驗證進行身份驗證和授權。


### 先決條件


在開始執行本文中給出的步驟之前，您需要一個 Azure 帳戶，以及帶有 .NET 5.0 開發環境的 Visual Studio 2019 步驟。

### 創建 ASP.NET Core 5.0 Web 應用程序

打開visual studio，點擊右側的新建項目，選擇“Asp.net core web app”，如下圖所示，點擊下一步。

![在 Visual Studio 中創建新項目](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/a1d03cc3-1984-4764-a43e-63f51e15ac95.png)

在配置您的新項目部分中，輸入項目的名稱和位置，如下圖所示，然後單擊下一步

![在 Visual Studio 中配置您的新項目](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/85d81323-e681-46f8-a223-c38f14ffab4d.png)

在附加信息步驟中，在目標框架中選擇 .NET 5.0，Authentication Type 為 none，選中 Configure HTTPS 複選框，然後單擊 create。

![在 Visual Studio 中為新項目配置附加信息](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/ade34eae-2bc0-4415-8eb5-591164decac1.png)

創建項目後，運行項目並從瀏覽器複製項目的 url。我們將在 Azure AD 應用註冊和設置中需要此 url。

 

### 在 Azure AD 中設置應用

使用具有管理員權限的帳戶登錄 Azure 門戶。登錄後，單擊 Azure Active Directory，如下圖所示。

![img](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/b9af224c-1a38-4db4-a6de-25dff6eaf81a.png)

從左側導航中，選擇應用註冊。

![img](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/f9abba72-bc43-4e0e-bfc5-1595c1de9f0e.png)

然後單擊頂部工具欄中的新註冊。這將打開一個對話框“註冊和應用程序”。

![img](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/1550626c-bfc5-496f-adf2-12d10605da0e.png)

在名稱輸入字段中，輸入您要用於應用程序的名稱。當用戶將被重定向到 Azure Active Directory 進行登錄時，此名稱將顯示在登錄頁面中。

在支持的帳戶類型中，選擇第一個選項。這將允許您自己組織的用戶使用此應用程序登錄。

現在，將重定向 URI 留空，然後單擊註冊。

創建應用程序後，通過單擊其名稱打開應用程序並複制 ClientID 和 TenantID 並隨身攜帶。

![img](https://www.faciletechnolab.com/Areas/Blog/blogcontent/blogimages/cb8794e7-d40f-4a2e-a8b7-a0023bdb2748.png)

接下來，單擊 API 權限。單擊工具欄中的添加權限，然後單擊 Microsoft graph，然後單擊委派權限。這將顯示您選擇的權限列表。`profile`從列表中選擇和添加`opendid`權限。

接下來，單擊左側導航中的身份驗證，並在平台部分中，添加 Web（如果不存在）。在網頁部分，轉到重定向 URL，然後單擊底部的添加 URI。輸入`{your-app-url}/signin-oidc`。例如，輸入`https://localhost:44332/signin-oidc`您的本地項目是否在端口 44332 上運行。

 

### 為 Azure AD 身份驗證配置 ASP.NET Core 5.0 應用程序

打開您的 Web 應用程序的 appsettings.json 並添加以下代碼行。

```json
 "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "ClientId": "your-client-id",
    "TenantId": "your-tenant-id"
  },
```

將`your-client-id`和替換`your-tenant-id`為您在 azure ad 中進行應用註冊時復制的實際值

接下來，添加包管理器控制台並將以下兩個包引用添加到您的 Web 應用程序。



```
Install-package Microsoft.AspNetCore.Authentication.OpenIdConnect
install-package Microsoft.Identity.Web
```



接下來，在您的項目中打開 startup.cs 並將以下代碼粘貼到行`ConfigureServices`前的方法中`services.AddRazorPages();`。

```c#
services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)
          .AddMicrosoftIdentityWebApp(Configuration.GetSection("AzureAd"));


services.AddControllersWithViews(options =>
{
    var policy = new AuthorizationPolicyBuilder()
        .RequireAuthenticatedUser()
        .Build();
    options.Filters.Add(new AuthorizeFilter(policy));
});
```

接下來，在 中`Startup.cs`，轉到`Configure`方法並`app.UseAuthentication();`在行前添加`app.UseAuthorization();`行。

接下來，在 views 文件夾中打開 index.cshtml 並輸入以下代碼行

```html-razor
@if(User.Identity.IsAuthenticated)
{
    <p>
        @User.Identity.Name
    </p>
}
```

保存所有文件並運行您的項目。

您會注意到，一旦您運行該項目，瀏覽器將重定向到 Microsoft 登錄頁面，返回後，您將在頁面上看到您的電子郵件地址。

 

### 結論

我們剛剛學習瞭如何在 ASP.NET 5.0 Web 應用程序中實現 Azure AD 身份驗證。

### 參考



- https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-aspnet-core-webapp
- https://www.c-sharpcorner.com/article/authentication-and-authorization-in-asp-net-5-with-jwt-and-swagger/