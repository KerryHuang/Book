---
kind: original
---

# `ASP.NET Core` Web Api實作JWT驗證筆記

此為紀錄筆者實作JWT驗證過程筆記。
專案使用`.Net 5`，並使用`.Net Core CLI`進行建置
使用`Visual Code`作為開發工具

有關`.Net Core CLI` 可參考
https://docs.microsoft.com/zh-tw/dotnet/core/tools/

> GitHub
> https://github.com/s123600g/jyu.lab.jwt

# 環境建置

下載`.Net Core SDK`選擇`.Net 5`版本並安裝
https://dotnet.microsoft.com/download

透過下方指令確認是否安裝無誤，正常會出現版本號

```
dotnet --version
```

# 專案建置

## 建立方案檔(sln)

```
dotnet new sln -n jyu.lab.jwt
```

> `-n` 為方案檔名稱

## 建立`.gitignore`

```
dotnet new gitignore
```

> 這裡可以視需要再做

## 建立WebApi專案

```
dotnet new webapi -n Lab_JWT
```

> `-n` 為設置專案名稱

透過下方指令將專案加入至方案內

```
dotnet sln add .\Lab_JWT\Lab_JWT.csproj
```

設置信任`ASP.NET Core HTTPS` 開發憑證

```
dotnet dev-certs https --trust
```

> 可以參考
> https://docs.microsoft.com/zh-tw/aspnet/core/security/enforcing-ssl?view=aspnetcore-5.0&tabs=visual-studio#trust-the-aspnet-core-https-development-certificate-on-windows-and-macos

建立好了之後，請在終端機透過`cd`指令進入專案目錄內，下方步驟需要再專案目錄內進行。

## 安裝Nuget套件

- `Microsoft.AspNetCore.Authentication.JwtBearer`
  https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.JwtBearer

```
dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer --version 5.0.6
```

- `NLog`
  https://www.nuget.org/packages/NLog/

```
dotnet add package NLog --version 4.7.10
```

- `NLog.Web.AspNetCore`
  https://www.nuget.org/packages/NLog.Web.AspNetCore/4.13.0-readme-preview

```
dotnet add package NLog.Web.AspNetCore --version 4.12.0
```

## 配置NLog

關於配置可以參考**Getting started with `ASP.NET Core 5`**
https://github.com/NLog/NLog/wiki/Getting-started-with-ASP.NET-Core-5

在配置之前要先完成安裝必要的Nuget套件，在上方步驟有安裝指令。

在專案目錄內建立一個`nlog.config`檔案，並在方案檔加入必要設置，請透過`Visual Code`進行操作。

開啟`Lab_JWT.csproj`在裡面加入下方配置

```
<ItemGroup>    
    <Content Update="nlog.config">
      <CopyToOutputDirectory>Always</CopyToOutputDirectory>
      <CopyToPublishDirectory>Always</CopyToPublishDirectory>
    </Content>
 </ItemGroup>
```

> 這裡用意是在**建置**/**發佈**階段時，指定將`nlog.config`複製一份到`bin/`底下對應的各階段目錄內去。
> 如果沒設置的話在執行的時候NLog不會正常運作起來。
> 複製條件為`Always`代表無論有沒有更動內容都複製更新。

將以下內容複製到`nlog.config`

```
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	  internalLogLevel="Trace"
      internalLogFile="${basedir}\Log\internal_nlog\internal-nlog.txt">

  <!-- enable asp.net core layout renderers -->
  <extensions>
    <add assembly="NLog.Web.AspNetCore"/>
  </extensions>

  <!-- the targets to write to -->
  <targets>
    <!-- write logs to file  -->
    <target xsi:type="File" name="allfile" fileName="${basedir}\Log\web\nlog-all-${shortdate}.log"
            layout="${longdate} [${uppercase:${level}}] ${message} ${newline}${exception:format=tostring}" />

    <!-- another file log, only own logs. Uses some ASP.NET core renderers -->
    <target xsi:type="File" name="ownFile-web" fileName="${basedir}\Log\coreown\nlog-own-${shortdate}.log"
            layout="${longdate} [${uppercase:${level}}] ${logger} | ${message} ${newline}${exception:format=tostring} | url: ${aspnet-request-url} action: ${aspnet-mvc-action}" />

    <target xsi:type="Console" name="lifetimeConsole"
            layout="${date} [${uppercase:${level}}] ${message} ${newline}${exception}" />
  </targets>

  <!-- rules to map from logger name to target -->
  <rules>
    <!--All logs, including from Microsoft-->
    <logger name="*" minlevel="Info" writeTo="allfile" />

    <!--Output hosting lifetime messages to make Docker / Visual Studio happy -->
    <logger name="Microsoft.Hosting.Lifetime" level="Info" writeTo="lifetimeConsole, ownFile-web" final="true" /> 
    <!--Skip non-critical Microsoft logs and so log only own logs-->
    <logger name="Microsoft.*" maxlevel="Info" final="true" /> <!-- BlackHole without writeTo -->
    <logger name="*" minlevel="Trace" writeTo="ownFile-web" />
  </rules>
</nlog>
```

> 在專案啟動時會在專案目錄下自動建置`Log/`，裡面會放置NLog產生的紀錄檔案
> 通常會看的是在`coreown/`與`web/`底下的紀錄檔
> 關於配置內容設定可以參考
> https://github.com/NLog/NLog/wiki/Configuration-file

### 註冊NLog為Log提供者

開啟專案內`Program.cs`，並引入以下套件

```
using NLog.Web;
```

在`Main`區塊將原始內容更改為以下

```
public static void Main(string[] args)
{
    NLog.Logger logger = NLogBuilder.ConfigureNLog("nlog.config").GetCurrentClassLogger();

    try
    {
        logger.Debug("The app init main");
        CreateHostBuilder(args).Build().Run();
    }
    catch (Exception exception)
    {
        //NLog: catch setup errors
        logger.Error(exception, "Stopped program because of exception");
        throw;
    }
    finally
    {
        // 確保當App結束時，NLog正常結束釋放掉
        // Ensure to flush and stop internal timers/threads before application-exit (Avoid segmentation fault on Linux)
        NLog.LogManager.Shutdown();
    }
}
```

> 在第一行為最重要，他會載入`nlog.config`依據裡面的內容進行配置NLog。
> 可以看到原始只有一行`CreateHostBuilder(args).Build().Run();`，經過配置NLog變成包覆在`try-catch-finally`裡面結構。
> 確保app啟動過程中如果發生意外而導致啟動失敗，可以啟動失敗錯誤紀錄，前提是NLog有先被正常載入。
> 在`finally`區塊內`NLog.LogManager.Shutdown();`是為了當app被關掉後，讓NLog程序正常關閉。

在`CreateHostBuilder`區塊將原始內容更改為以下

```
 public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                })
                // 重新設置app Log配置
                .ConfigureLogging(logging =>
                {
                    // 清除app預設Log Provider
                    logging.ClearProviders();
                    // 設定Log輸出最小層級
                    logging.SetMinimumLevel(LogLevel.Trace);
                })
                .UseNLog();  // NLog: Setup NLog for Dependency injection);
```

> 這裡透過`ConfigureLogging`來進行app預設Log提供者解除，並設定要輸出的最低Log層級。
> 最後透過`UseNLog()`來注入NLog服務成為app預設Log提供者。

# JWT服務

實作一個專門處理JWT處理的服務，並透過DI(Dependency Injection)注入方式供app使用。

> 使用擴充方法來註冊服務群組
> https://docs.microsoft.com/zh-tw/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-5.0#register-groups-of-services-with-extension-methods

建立`JWTCliam.cs`，並放置在專案`Models/`

```
namespace Lab_JWT.Models
{
    public class JWTCliam
    {
        /// <summary>
        /// 聲明資訊-發行者
        /// </summary>
        /// <value></value>
        public string iss { set; get; }

        /// <summary>
        /// 聲明資訊-User內容
        /// </summary>
        /// <value></value>
        public string sub { set; get; }

        /// <summary>
        /// 聲明資訊-接收者
        /// </summary>
        /// <value></value>
        public string aud { set; get; }

        /// <summary>
        /// 聲明資訊-有效期限
        /// </summary>
        /// <value></value>
        public string exp { set; get; }

        /// <summary>
        /// 聲明資訊-起始時間
        /// </summary>
        /// <value></value>
        public string nbf { set; get; }

        /// <summary>
        /// 聲明資訊-發行時間
        /// </summary>
        /// <value></value>
        public string iat { set; get; }

        /// <summary>
        /// 聲明資訊-獨立識別ID
        /// </summary>
        /// <value></value>
        public string jti { set; get; }
    }
}
```

> 放置聲明資訊(Claim)內容各項預設參數內容Data Model。
> 在api接收到請求後，內部處理會先封裝好聲明資訊內容，再呼叫JWT處理服務內功能時會帶此Data Model。
> 有關於聲明資訊(Claim)可以參考
> https://auth0.com/docs/tokens/json-web-tokens/json-web-token-claims#reserved-claims

建立`JWTConfig.cs`，並放置在專案`Models/`

```
namespace Lab_JWT.Models
{
    public class JWTConfig
    {
        /// <summary>
        /// 發行者
        /// </summary>
        /// <value></value>
        public string Issuer { set; get; }

        /// <summary>
        /// 加密金鑰
        /// </summary>
        /// <value></value>
        public string SignKey { set; get; }

        /// <summary>
        /// 設置Token存活多久(分鐘)
        /// </summary>
        /// <value></value>
        public int ExpireDateTime { set; get; }
    }
}
```

> 放置有關Token相關設定項目內容Data Model。
> 這裡設定項目跟Token本身有關，會跟`appsettings.json`內`JWTConfig`配置相對應
> 在api接收到請求後，內部處理會先封裝Token本身設定內容，再呼叫JWT處理服務內功能時會帶此Data Model。

建立`JWTServices.cs`，並放置在專案`Services/`

```
using Microsoft.Extensions.Logging;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Collections.Generic;
using System.Security.Claims;
using System.Text;
using System.IdentityModel.Tokens.Jwt;
using Lab_JWT.Models;

namespace Lab_JWT.Services
{
    public interface JWTBase
    {
        /// <summary>
        ///  產生JWT Token
        /// </summary>
        /// <param name="jWTCliam">Token 資訊聲明內容物件</param>
        /// <param name="secretKey">加密金鑰，用來做加密簽章用</param>
        /// <param name="issur">Token 發行者資訊</param>
        /// <param name="expireMinutes">Token 有效期限(分鐘)</param>
        /// <returns>回應內容物件，內容屬性jwt放置Token字串</returns>
        RunStatus GetJWT(
            JWTCliam jWTCliam,
            string secretKey,
            string issuer,
            int expireMinutes = 30
        );
    }

    public class JWTServices : JWTBase
    {
        private readonly ILogger<JWTServices> log;

        public JWTServices(ILogger<JWTServices> logger)
        {
            log = logger;
        }

        public RunStatus GetJWT(
            JWTCliam jWTCliam,
            string secretKey,
            string issuer,
            int expireMinutes = 30
        )
        {
            RunStatus response = new RunStatus();

            try
            {
                #region Step 1. 取得資訊聲明(claims)集合

                List<Claim> claims = GenCliams(jWTCliam);

                #endregion

                #region  Step 2. 建置資訊聲明(claims)物件實體，依據上面步驟產生Data來做

                ClaimsIdentity userClaimsIdentity = new ClaimsIdentity(claims);

                #endregion

                #region Step 3. 建立Token加密用金鑰

                SymmetricSecurityKey securityKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(secretKey));

                #endregion

                #region Step 4. 建立簽章，依據金鑰

                // 使用HmacSha256進行加密
                SigningCredentials signingCredentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256Signature);

                #endregion

                #region  Step 5. 建立Token內容實體

                SecurityTokenDescriptor tokenDescriptor = new SecurityTokenDescriptor
                {
                    Issuer = issuer, // 設置發行者資訊
                    Audience = issuer, // 設置驗證發行者對象，如果需要驗證Token發行者，需要設定此項目
                    NotBefore = DateTime.Now, // 設置可用時間， 預設值就是 DateTime.Now
                    IssuedAt = DateTime.Now, // 設置發行時間，預設值就是 DateTime.Now
                    Subject = userClaimsIdentity, // Token 針對User資訊內容物件
                    Expires = DateTime.Now.AddMinutes(expireMinutes), // 建立Token有效期限
                    SigningCredentials = signingCredentials // Token簽章
                };

                #endregion

                #region Step 6. 產生JWT Token並轉換成字串

                JwtSecurityTokenHandler tokenHandler = new JwtSecurityTokenHandler(); // 建立一個JWT Token處理容器
                SecurityToken securityToken = tokenHandler.CreateToken(tokenDescriptor);  // 將Token內容實體放入JWT Token處理容器
                string serializeToken = tokenHandler.WriteToken(securityToken); // 最後將JWT Token處理容器序列化，這一個就是最後會需要的Token 字串

                #endregion

                response.isSuccess = true; // 告訴使用此請求一方Token成功產生
                response.jwt = serializeToken; // 放置產生的Token字串
                response.msg = "Done.";
            }
            catch (Exception ex)
            {
                log.LogError($"{ex.Message}\n{ex.StackTrace}");
                response.isSuccess = false;
                response.jwt = string.Empty;
                response.msg = "產生Token 過程發生錯誤.";
            }

            return response;
        }

        // https://auth0.com/docs/tokens/json-web-tokens/json-web-token-claims#custom-claims
        /// <summary>
        /// 建置資訊聲明集合
        /// </summary>
        /// <param name="jWTCliam">Token資訊聲明內容物件</param>
        /// <returns>一組收集資訊聲明集合</returns>
        private List<Claim> GenCliams(JWTCliam jWTCliam)
        {
            List<Claim> claims = new List<Claim>();

            // (audience)
            // 設定Token接受者，用在驗證接收者驗證是否相符
            if (jWTCliam.aud != null && jWTCliam.aud != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Aud, jWTCliam.aud));
            }

            // (expiration time)
            // Token過期時間，一但超過這時間此Token就失效
            if (jWTCliam.exp != null && jWTCliam.exp != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Exp, jWTCliam.exp));
            }

            //  (issued at time)
            // Token發行時間，用在後面檢查Token發行多久
            if (jWTCliam.iat != null && jWTCliam.iat != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Iat, jWTCliam.iat));
            }

            // (issuer)
            // 發行者資訊
            if (jWTCliam.iss != null && jWTCliam.iss != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Iss, jWTCliam.iss));
            }

            // (JWT ID)
            // Token ID，避免Token重複在被套用
            if (jWTCliam.jti != null && jWTCliam.jti != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Jti, jWTCliam.jti));
            }

            // (not before time)
            // Token有效起始時間，用來驗證Token可用時間
            if (jWTCliam.nbf != null && jWTCliam.nbf != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Nbf, jWTCliam.nbf));
            }

            // (subject)
            // Token 主題，放置該User內容
            if (jWTCliam.sub != null && jWTCliam.sub != string.Empty)
            {
                claims.Add(new Claim(JwtRegisteredClaimNames.Sub, jWTCliam.sub));
            }

            return claims;
        }
    }

    public class RunStatus
    {
        /// <summary>
        /// Token是否有成功產生狀態
        /// </summary>
        /// <value>布林值</value>
        public bool isSuccess { set; get; }

        /// <summary>
        /// Token
        /// </summary>
        /// <value>字串</value>
        public string jwt { set; get; }

        /// <summary>
        /// 處理訊息
        /// </summary>
        /// <value>字串</value>
        public string msg { set; get; }
    }
}
```

> 在此服務架構中
> 透過介面(JWTBase)去定義有什麼功能和需要帶什麼參數，作為一個Service Base。
> 介面功能定義好後，將此Service Base去實作出來，完成介面定義功能內處理邏輯。

## 註冊服務與設置驗證方法

### 註冊服務

在`Startup.cs`內`ConfigureServices`進行配置

```
services.AddSingleton<JWTBase, JWTServices>();
```

> 透過相依性注入(Dependency Injection)
> 泛型結構<介面,實作類別>
> 可以參考使用擴充方法來註冊服務群組
> https://docs.microsoft.com/zh-tw/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-5.0#register-groups-of-services-with-extension-methods
> 關於注入的服務留存期可參考，在這是使用`單一`
> https://docs.microsoft.com/zh-tw/dotnet/core/extensions/dependency-injection#service-lifetimes

### 設置驗證

在`Startup.cs`內進行配置，在以下兩個區塊進行

#### ConfigureServices

引入套件

```
using Microsoft.AspNetCore.Authentication.JwtBearer;
```

在這裡驗證邏輯流程如下

- 設置驗證方式

```
services.AddAuthentication(
    JwtBearerDefaults.AuthenticationScheme
)
```

> 這裡作用為告訴app驗證方式為JWT Token驗證
> 有關驗證可以參考
> https://docs.microsoft.com/zh-tw/aspnet/core/security/authentication/?view=aspnetcore-5.0

- 驗證項目設置

```
AddJwtBearer(options =>
    {
        // You need to import package as follow
        // using Microsoft.IdentityModel.Tokens;
        options.TokenValidationParameters = new TokenValidationParameters
        {
            #region  配置驗證發行者

            ValidateIssuer = true, // 是否要啟用驗證發行者
            ValidIssuer = Configuration.GetSection("JWTConfig").GetValue<string>("Issuer"),

            #endregion

            #region 配置驗證接收方

            ValidateAudience = false, // 是否要啟用驗證接收者
            // ValidAudience = "" // 如果不需要驗證接收者可以註解

            #endregion

            #region 配置驗證Token有效期間

            ValidateLifetime = true, // 是否要啟用驗證有效時間

            #endregion

            #region 配置驗證金鑰

            ValidateIssuerSigningKey = false, // 是否要啟用驗證金鑰，一般不需要去驗證，因為通常Token內只會有簽章

            #endregion

            #region 配置簽章驗證用金鑰

            // 這裡配置是用來解Http Request內Token加密
            // 如果Secret Key跟當初建立Token所使用的Secret Key不一樣的話會導致驗證失敗
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(
                    Configuration.GetSection("JWTConfig").GetValue<string>("SignKey")
                )
            )

            #endregion
    };
});
```

> 接續在`services.AddAuthentication()`後面，透過`.`來進行串接。
> 這裡主要用來設置Token驗證的項目設定。

#### Configure

加入驗證

```
app.UseAuthentication();
```

加入授權

```
app.UseAuthorization();
```

> 需要注意的是，這個要包在`app.UseRouting()`跟`app.UseEndpoints`中間
> 否則會再請求進來時，發生錯誤產生。
> 這個會跟Action上方Tag`[Authorize]`與`[AllowAnonymous]`有關

## 服務功能

### 產生JWT Token

`GetJWT()` 用來產生取得JWT Token字串。

功能所需要的參數

- `secretKey`、`issuer`、`expireMinutes`
  都會跟`appsettings.json`內`JWTConfig`配置相對應。
- `jWTCliam`
  在呼叫此功能上一端會將聲明資訊內容透過`JWTCliam`Data Model封裝，並帶入給此功能參數。

最後會回傳一組Token字串，這組字串內容是經過加密後的字串。

# 測試

透過`Controllers/LoginController.cs` Api進行測試

## 模擬登入取得Token

```
https://localhost:5001/api/signin
```

對應**Action** --> `SignIn()`

關於User資訊聲明(Cliam)產生，會在此自動做一個簡單內容，使用上方`JWTCliam`進行資訊內容封裝Data Model，在呼叫JWT處理服務內產生JWT Token功能時，會將此封裝好Data Model帶入參數給予。

最後會回傳一組JSON

- `JwtToken` --> 產生的JWT Token 字串。
- `Status` --> 請求處理結果是否正常狀態，型態為一個布林值。
- `Msg` --> 如果有錯誤發生，這裡會放置錯誤訊息。

![img](https://i.imgur.com/kJj29V3.png)

## 模擬呼叫需驗證Token Api

```
https://localhost:5001/api/get/info
```

對應**Action** --> `GetTokenInfo()`

模擬一個發送請求途中，在**Header**內帶有驗證Token，格式如下

```
Authorization: Bearer + Token
```

> `Bearer`跟Token之間記得要加上一個空白符號隔開

這支Api只是單純模擬需要帶有Token驗證Htpp請求，根據在`Starup.cs`內設置的驗證配置來進行，最後會簡單的分析讀取Token發行者(Issuer)資訊。

最後會回傳一組JSON

- `JwtToken` --> 因為不是請求登入取得Token，所以這裡會是字串空值。
- `Status` --> 請求處理結果是否正常狀態，型態為一個布林值。
- `Msg` --> 如果有錯誤發生，這裡會放置錯誤訊息，反之則會是Token發行者(Issuer)資訊。

![img](https://i.imgur.com/ONB42q2.png)

# 參考連結

- https://blog.miniasp.com/post/2019/12/16/How-to-use-JWT-token-based-auth-in-aspnet-core-31
- https://blog.poychang.net/authenticating-jwt-tokens-in-asp-net-core-webapi/
- https://mgleon08.github.io/blog/2018/07/16/jwt/
- https://medium.com/麥克的半路出家筆記/筆記-透過-jwt-實作驗證機制-2e64d72594f8
- https://auth0.com/docs/tokens/json-web-tokens/json-web-token-claims#custom-claims