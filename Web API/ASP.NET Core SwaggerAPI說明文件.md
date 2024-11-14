# [ASP.NET Core]如何使用SwaggerAPI說明文件


在開發API站台時，時常要與前端開發者做對接，Swagger提供了很完善的說明文件，也可以立即做測試
接下來介紹如何ASP.NET Core中使用Swagger產生說明文件



## 安裝套件

Swagger主要有三個套件

1. Swashbuckle.AspNetCore.Swagger: 公開 `SwaggerDocument` 物件作為 JSON 端點。
2. Swashbuckle.AspNetCore.SwaggerGen: 可以從Model、Controller、Router 等 建立 `SwaggerDocument`
3. Swashbuckle.AspNetCore.SwaggerUI: 可解析 `Swagger Json` 來產生畫面

從 Visual Studio 中可以在套件管理員中找到這三個套件
[![img](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-01.jpg)](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-01.jpg)

## 設定Swagger MiddleWare

在`ConfigureServices` 加入 Swagger產生器

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();
    /// 加入Swagger產生器到服務集合
    services.AddSwaggerGen(c =>
    {
        c.SwaggerDoc("v1", new OpenApiInfo
        {
            Title = "My API", Version = "V1"
        });
    });
}
```

在`Startup.Configure`方法中，啟用Swagger Middleware 用來產生json文件與Swagger UI

```csharp
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();

    /// 使用 Swagger 產生json端點文件
    app.UseSwagger()
    /// 啟用SwaggerUI 並根據Swagger.json產生畫面
    app.UseSwaggerUI(c => { c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1"); })
    app.UseHttpsRedirection()
    app.UseRouting()
    app.UseAuthorization()
    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllers();
    });
}
```

接著編譯一下並啟動 瀏覽`https://localhost:<port>/swagger` 就可以看到Swagger的API說明文件了

[![img](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-02.jpg)](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-02.jpg)

剛剛設定的Json端點文件會產生在 `https://localhost:<port>/swagger/v1/swagger.json`

## 自訂Swagger API 說明資訊

你也可以自行設定額外的Swagger API的說明資訊 在 `ConfigureServices` 設定

```csharp
services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "My API", 
        Version = "V1",
        Contact = new OpenApiContact { Name = "Bryan", Email = "d58526@gmail.com"},
        Description ="我的第一個測試API",
    });
});
```

[![img](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-03.jpg)](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-03.jpg)

## 在Swagger上加入Controller中或Model的註解

在程式當中所寫的註解，都可以透過Swagger產生說明文件，讓使用API的人更加了解API的意義及所需參數

我自訂了一個簡單的Controller

```csharp
/// <summary>
/// 使用者服務
/// </summary>
[ApiController]
[Route("api/[controller]")]
public class UserController : ControllerBase
{
    private List<UserInfo> _userInfos = new List<UserInfo>
    {
        new UserInfo {Id = 1, Account = "Test1", Name = "Test1Name", Phone = "123456"},
        new UserInfo {Id = 2, Account = "Test2", Name = "Test2Name", Phone = "789123"},
        new UserInfo {Id = 3, Account = "Test3", Name = "Test3Name", Phone = "012345"},
    };
    
    /// <summary>
    /// 取得使用者清單
    /// </summary>
    /// <returns></returns>
    [HttpGet]
    public IEnumerable<UserInfo> Get()
    {
        return this._userInfos;
    }
    /// <summary>
    /// 取得單一使用者
    /// </summary>
    /// <param name="id">編號</param>
    /// <returns></returns>
    [HttpGet("{id}")]
    public UserInfo Get(int id)
    {
        return this._userInfos.FirstOrDefault(item => item.Id == id);
    }
    /// <summary>
    /// 新增使用者
    /// </summary>
    /// <param name="userInfo">使用者資訊</param>
    [HttpPost]
    public void Post([FromBody]UserInfo userInfo)
    {
        this._userInfos.Add(userInfo);
    }
    /// <summary>
    /// 更新使用者名稱
    /// </summary>
    /// <param name="id">編號</param>
    /// <param name="name">名稱</param>
    [HttpPut("{id}")]
    public void Put(int id, [FromBody]string name)
    {
        var user = this._userInfos.FirstOrDefault(item => item.Id == id);
        user.Name = name;
    }
    /// <summary>
    /// 刪除使用者
    /// </summary>
    /// <param name="id">編號</param>
    [HttpDelete("{id}")]
    public void Delete(int id)
    {
        this._userInfos.RemoveAll(item => item.Id == id);
    }
}
```

自訂了一個簡單的類別 `UserInfo`

```csharp
/// <summary>
/// 使用者資訊
/// </summary>
public class UserInfo
{
    /// <summary>
    /// 編號
    /// </summary>
    public int Id { get; set; }
    /// <summary>
    /// 帳號
    /// </summary>
    public string Account { get; set; }
    /// <summary>
    /// 名稱
    /// </summary>
    public string Name { get; set; }
    /// <summary>
    /// 電話號碼
    /// </summary>
    public string Phone { get; set; }
}
```



接下來要讓專案產生註解的XML 並加入到Swagger中

打開專案檔 加入

```xml
<PropertyGroup>
  <GenerateDocumentationFile>true</GenerateDocumentationFile>
</PropertyGroup>
```



[![img](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-04.jpg)](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-04.jpg)

就會在編譯的時候 在組態的同名資料夾下會有檔名與專案同名的XML文件
這個XML文件的內容就是程式碼的註解

[![img](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-05.jpg)](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-05.jpg)

接下來要將這個註解XML檔案加入到Swagger中 在`ConfigureServices`加入設定

```csharp
services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "My API",
        Version = "V1",
        Contact = new OpenApiContact {Name = "Bryan", Email = "d58526@gmail.com"},
        Description = "我的第一個測試API",
    });
    
    /// 加入xml檔案到swagger
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
    c.IncludeXmlComments(xmlPath);
});
```

重新執行就會看到剛剛所寫的程式碼註解，也有完整的類別說明，提高API文件的可讀性

[![img](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-06.jpg)](https://bryanyu.github.io/2019/12/29/AspNetCoreSwagger/AspNetCoreSwagger-06.jpg)

[範例程式](https://github.com/BryanYu/AspNetCoreSwaggerSample)

## 結論

透過Swagger產生API說明文件的方式，可以節省開發人員撰寫額外的文檔時間，又可以解決文件與程式碼的同步問題，同時產生的文檔也可以立即進行測試，對於前後端開發者的對接可以增加開發效率。