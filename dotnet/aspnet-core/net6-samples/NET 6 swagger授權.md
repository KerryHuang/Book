---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/SwaggerExample_Advanced_Authorization
author: CI-YU
---

# .NET 6 swagger授權

### 目的

在swagger內使用jwt token測試API

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1-1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2-1](https://user-images.githubusercontent.com/19286751/187078108-8415cab0-dd09-4bde-93fa-9ab69a1e36dd.png)

### 其他資訊

選擇.net6版本，支援OpenAPI支援一定要勾選，此選項.net5以後才會有，.net core 3.1並沒有此選項，需要從NuGet安裝，並點建立
![步驟3-1](https://user-images.githubusercontent.com/19286751/143257352-79b0ced0-fdba-4846-8275-f35ce5bffc7f.png)

### 專案基本設定

右邊紅框處專案檔點兩下，會開啟專案的xml檔案，額外加入兩行xml資料，目的是要透過編譯器產生文件檔案

```xml
<GenerateDocumentationFile>true</GenerateDocumentationFile>
<NoWarn>$(NoWarn);1591</NoWarn>
```

- 加入前
![步驟4-1](https://user-images.githubusercontent.com/19286751/143259132-6b80a83f-88c0-4e5e-91f1-aedcae09f747.png)

- 加入後
![步驟4-2](https://user-images.githubusercontent.com/19286751/143258393-ee01f7e3-42e2-44b9-b9cc-2ba3dca463f9.png)

### 編輯Program.cs檔案

修改program檔案內容，調整AddSwaggerGen的內容，目的是為了可以讀取我們所寫的註解

```csharp
builder.Services.AddSwaggerGen(options => {
  // using System.Reflection;
  var xmlFilename = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
  options.IncludeXmlComments(Path.Combine(AppContext.BaseDirectory, xmlFilename));
});
```

- 加入前
![步驟5-1](https://user-images.githubusercontent.com/19286751/143260711-19f5d30d-97e9-4ef2-a003-e0aae1b71bbb.png)

- 加入後
![步驟5-2](https://user-images.githubusercontent.com/19286751/143260140-bed85f76-44d3-4a33-aaa2-e4778c7b8e9d.png)

### NuGet加入套件

透過NuGet安裝

- JWT
- Microsoft.AspNetCore.Authentication.JwtBearer
- Microsoft.IdentityModel.Tokens
- System.IdentityModel.Tokens.Jwt

![範例6-1](https://user-images.githubusercontent.com/19286751/190917165-eba77970-c4d8-4835-b312-41e3449fcd8c.png)

### 新增Helpers資料夾並在裡面新增JwtHelpers.cs類別檔案

jwt範例使用保哥範例來做修改，目的只是為了取得jwt token

```c#
  public class JwtHelper {
    private readonly JwtSettingsOptions _settings;

    public JwtHelper(IOptionsMonitor<JwtSettingsOptions> settings) {
      //注入appsetting的json
      _settings = settings.CurrentValue;
    }

    public string GenerateToken(string userName, int expireMinutes = 120) {
      //發行人
      var issuer = _settings.Issuer;
      //加密的key，拿來比對jwt-token沒有
      var signKey = _settings.SignKey;
      //建立JWT-Token
      var token = JwtBuilder.Create()
                      //所採用的雜湊演算法
                      .WithAlgorithm(new HMACSHA256Algorithm()) // symmetric
                      //加密key
                      .WithSecret(signKey)
                      //角色
                      .AddClaim("roles", "admin")
                      //JWT ID
                      .AddClaim("jti", Guid.NewGuid().ToString())
                      //發行人
                      .AddClaim("iss", issuer)
                      //使用對象名稱
                      .AddClaim("sub", userName) // User.Identity.Name
                      //過期時間
                      .AddClaim("exp", DateTimeOffset.UtcNow.AddMinutes(expireMinutes).ToUnixTimeSeconds())
                      //此時間以前是不可以使用
                      .AddClaim("nbf", DateTimeOffset.UtcNow.ToUnixTimeSeconds())
                      //發行時間
                      .AddClaim("iat", DateTimeOffset.UtcNow.ToUnixTimeSeconds())
                      //使用者全名
                      .AddClaim(ClaimTypes.Name, userName)
                      //進行編碼
                      .Encode();
      return token;
    }
  }
  //將appsetting轉為強型別所使用
  public class JwtSettingsOptions {
    public string Issuer { get; set; } = "";
    public string SignKey { get; set; } = "";
  }
```

因篇幅過長，只擷取JwtHelpers.cs部分內容，記得要using下列命名空間

```c#
using JWT.Algorithms;
using JWT.Builder;
using Microsoft.Extensions.Options;
using System.Security.Claims;
```

![範例7-1](https://user-images.githubusercontent.com/19286751/190916369-882f1da2-b777-471d-8728-bdca97546274.png)

### 新增Filters資料夾並在裡面新增AuthorizeCheckOperationFilter.cs類別檔案

因為在使用swagger做認證測試時，會遇到一個很惱人的問題，就是當我的某些api並不需要做認證，卻還是會在畫面上顯示鎖頭

- 第一支並沒有attribute，無須認證
- 第二支為AllowAnonymous，無須認證
- 第三支為Authorize，需要認證

![範例8-1](https://user-images.githubusercontent.com/19286751/190920825-f49060d7-681f-4ec8-a890-efedde67306e.png)

```c#
      public class AuthorizeCheckOperationFilter : IOperationFilter {
    private readonly EndpointDataSource _endpointDataSource;

    public AuthorizeCheckOperationFilter(EndpointDataSource endpointDataSource) {
      _endpointDataSource = endpointDataSource;
    }
    public void Apply(OpenApiOperation operation, OperationFilterContext context) {
      //取得所有controller內的action
      var Descriptor = _endpointDataSource.Endpoints.FirstOrDefault(x =>
          x.Metadata.GetMetadata<ControllerActionDescriptor>() == context.ApiDescription.ActionDescriptor);
      //取得包含Authorize的Attribute
      var Authorize = Descriptor.Metadata.GetMetadata<AuthorizeAttribute>() != null;
      //取得包含AllowAnonymous的Attribute
      var AllowAnonymous = Descriptor.Metadata.GetMetadata<AllowAnonymousAttribute>() != null;
      //如果不需要鎖頭則return回去
      if (!Authorize || AllowAnonymous)
        return;
      //需要鎖頭則在swagger-UI中定義出來
      operation.Security = new List<OpenApiSecurityRequirement>
      {
                new()
                {
                    [
                        new OpenApiSecurityScheme {Reference = new OpenApiReference
                            {
                                Type = ReferenceType.SecurityScheme,
                                Id = "Bearer"}
                        }
                    ] = new List<string>()
                }
            };
    }
  }
```

### 編輯WeatherForecastController檔案

注入JwtHelper
![範例9-1](https://user-images.githubusercontent.com/19286751/190922072-93b7cf19-52a7-4a7b-a17a-bb1ce544b8a2.png)

- 第一支為預設沒有attribute的方法
- 第二支為登入方法，attribute是AllowAnonymous，任何人都可以使用
- 第三支為登入後才可以取得的資料，attribute是Authorize(Roles = “admin”)，role需要是admin才可以使用

```c#
    [HttpGet("Login"), AllowAnonymous]
    public ActionResult<string> Login(string username , string password) {
      var token = _jwtHelpers.GenerateToken(username);
      return Ok(token);
    }
    [HttpGet("username"), Authorize(Roles = "admin")]
    public ActionResult<string> Username() {
      return Ok(User.Identity?.Name);
    }
```

![範例9-2](https://user-images.githubusercontent.com/19286751/190922108-2676ae07-fcd2-4846-9991-e060756b998e.png)

### 再次編輯Program.cs檔案

分兩個區塊說明

1. JWT設定

```c#
//清除預設映射
JwtSecurityTokenHandler.DefaultInboundClaimTypeMap.Clear();
//註冊JwtHelper
builder.Services.AddSingleton<JwtHelper>();
//使用選項模式註冊
builder.Services.Configure<JwtSettingsOptions>(
    builder.Configuration.GetSection("JwtSettings"));
//設定認證方式
builder.Services
  //使用bearer token方式認證並且token用jwt格式
  .AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
  .AddJwtBearer(options => {
    options.TokenValidationParameters = new TokenValidationParameters {
      // 可以讓[Authorize]判斷角色
      RoleClaimType = "roles",
      // 預設會認證發行人
      ValidateIssuer = true,
      ValidIssuer = builder.Configuration.GetValue<string>("JwtSettings:Issuer"),
      // 不認證使用者
      ValidateAudience = false,
      // 如果 Token 中包含 key 才需要驗證，一般都只有簽章而已
      ValidateIssuerSigningKey = true,
      // 簽章所使用的key
      IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(builder.Configuration.GetValue<string>("JwtSettings:SignKey")))
    };
  }); 
```

![範例10-1](https://user-images.githubusercontent.com/19286751/190919465-fb4da107-0770-4df5-905a-1a69982cb786.png)

2. Swagger-UI調整

```C#
  //說明api如何受到保護
  options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme {
    Name = "Authorization",
    //選擇類型，type選擇http時，透過swagger畫面做認證時可以省略Bearer前綴詞(如下圖)
    Type = SecuritySchemeType.Http,
    //採用Bearer token
    Scheme = "Bearer",
    //bearer格式使用jwt
    BearerFormat = "JWT",
    //認證放在http request的header上
    In = ParameterLocation.Header,
    //描述
    Description = "JWT驗證描述"
  });
  //製作額外的過濾器，過濾Authorize、AllowAnonymous，甚至是沒有打attribute
  options.OperationFilter<AuthorizeCheckOperationFilter>();
```

- Type使用`SecuritySchemeType.Http`，不用打Bearer![範例10-2](https://user-images.githubusercontent.com/19286751/190922426-373cd97c-f214-4ebe-9e7e-e89cd9169bd3.png)

- Type使用`SecuritySchemeType.ApiKey`，需要打Bearer與空白以及文字描述會包含Name、In、Description![範例10-3](https://user-images.githubusercontent.com/19286751/190922475-342ba0df-a95d-4bc3-b565-eca6d1ac8414.png)![範例10-4](https://user-images.githubusercontent.com/19286751/190922385-30e93c23-ad12-4eca-bd45-572f27d36bb2.png)在下方別忘了使用認證的中介層![範例10-5](https://user-images.githubusercontent.com/19286751/190922539-a297e36d-05e0-48fc-84e9-e5c91a76f4c8.png)

### 執行結果

在登入的api輸入帳號密碼
![範例11-1](https://user-images.githubusercontent.com/19286751/190922633-a6c9c7e6-4bf2-4731-82db-202f7eac9877.png)

會回傳一組jwt token
![範例11-2](https://user-images.githubusercontent.com/19286751/190922662-ab8550be-2d17-4f39-b717-eafbdc3e4cfa.png)

點擊認證按鈕，將token輸入
![範例11-3](https://user-images.githubusercontent.com/19286751/190922742-a757734a-9795-43b6-bbf5-dbcd95f97a8b.png)

![範例11-4](https://user-images.githubusercontent.com/19286751/190922687-fda2c7b2-18d1-400f-80d1-96458517c519.png)

使用有鎖頭的API
![範例11-5](https://user-images.githubusercontent.com/19286751/190922772-ac0d9e89-2ae3-47a2-b10e-cda412aa77dc.png)

最後可以正確取得回傳值就是成功了
![範例11-6](https://user-images.githubusercontent.com/19286751/190922793-20fa6719-8d24-4b22-80f2-6e2adb16d83c.png)

如果不輸入token直接使用有鎖頭的API，就會跳出401錯誤
![範例11-7](https://user-images.githubusercontent.com/19286751/190922917-f882cd9f-c2ee-48c5-98e9-197272a4b125.png)

### 參考

[保哥](https://blog.miniasp.com/post/2019/12/16/How-to-use-JWT-token-based-auth-in-aspnet-core-31) [伊果的沒人看筆記本](https://igouist.github.io/post/2021/10/swagger-enable-authorize/) [實作Filter](https://stackoverflow.com/questions/62432556/requireauthorization-and-swashbuckle-ioperationfilter) [JWT規範](https://www.iana.org/assignments/jwt/jwt.xhtml)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/SwaggerExample_Advanced_Authorization)