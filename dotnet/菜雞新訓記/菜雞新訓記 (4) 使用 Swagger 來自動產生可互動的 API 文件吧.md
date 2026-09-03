---
kind: reprint
source: https://igouist.github.io/post/2021/05/newbie-4-swagger
author: igouist
---

# 菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧



![img](https://i.imgur.com/lzjNys4.png)

這是俺整理公司新訓內容的第四篇文章，目標是簡單地使用 Swagger 工具來自動產生可互動的 API 文件。

## API 文件與 Swagger

在 [上一篇](https://igouist.github.io/post/2021/05/newbie-3-dapper) 我們建立了一個有簡單的 CRUD 的 Web API 服務，這篇我們就接續著 API 服務往下看吧！

之前我們介紹 API 的時候有提過：API 是為了讓兩個服務之間可以溝通、互動所產生的接口。而所有的溝通要有效，都一定要先有共識，隨著溝通的人數越來越多，或是內容的理解要越來越細，就會用文件或契約的方式來達成共識。

回到我們的 API 服務開發來說，就是你除了把服務生出來了，可以跑了以外，還有一個重要的點是：必須讓所有的使用者（包含幾個月後的你自己）知道怎麼使用這組 API 服務。

也就來說，就是要寫 API 規格文件 啦！

為了能讓服務對接順利，以及省下大部份口沫橫飛解釋的時間，甚至是讓自己和使用者好幾個月之後能夠順利回想起來，我們在開發 API 的時候一定會列出 API 接口的規格和用法。

通常一份文件的內容包括但不限於：用途、路由、參數、回傳值等等，更細部的會有例如參數放在 Route, QueryString 還是 Body、參數是否必填、回傳的 JSON 範例等等。例如：

```markdown
## GET /card/{id}
**查詢指定編號的卡片**

### Parameter

- Route
    - `id (int, required)` 卡片編號

example: https://exampleProjN.com/api/card/1

### Response

200: 回傳對應的卡片
{
  "id": 0,
  "name": "string",
  "description": "string",
  "attack": 0,
  "health": 0,
  "cost": 0
}

404: 找不到
```

當然這邊已經把例子簡化很多了，實際上的 API 文件格式會隨著各地的團隊習慣而改變，用表格和 PDF 等等的狀況也很常見。

對 API 規格都長怎樣有興趣的朋友，也可以直接在網路上找找一些公開的文件：

- [痞客幫 API 文件](https://developer.pixnet.pro/#!/doc/pixnetApi/glossaryArea)
- [91 APP 的開發文件](https://www.91app.com/developers#api-doc)
- [農業資料開放平台](https://agridata.coa.gov.tw/apidocs.aspx)
- [司法院資料開放平台](https://opendata.judicial.gov.tw/news/detail?newsId=3032)

不過寫文件畢竟是能登上靠北榜的工作內容之一（靠北榜還包括其他人不寫文件、寫註解、其他人不寫註解等），同時，每次 API 有變動還要一直去維護文件真的很麻煩，所以…

我們工程師的美德，就是懶惰！ API 文件什麼的，當然是要用自動產生的啦～

今天要介紹的 Swagger 工具就是幫助我們來自動產生 API 規格文件的好幫手，接下來就先讓我們稍微認識一下 Swagger 吧！

Swagger 是一套 API 互動文件產生器，主要是讓人跟電腦都能夠理解 API 的功能和內容，而不需要閱讀程式碼。因為 Swagger 已經在 2015 捐贈給 OpenAPI，所以也會看到有人用 OpenAPI 來稱呼它。更精準的說，OpenAPI 是一種規格、一種表達方式，Swagger 則是使用 OpenAPI 的工具。

想知道 Swagger 工具的 API 文件長怎樣的朋友，可以到這些地方逛逛按按：

- [Swagger 提供的 Demo 網頁（petstore.swagger.io）](http://petstore.swagger.io/)
- [公共運輸旅運資料服務（MOTC Transport API）](https://ptx.transportdata.tw/MOTC)

操作上挺直覺的，而且我們前面提到的「用途、路由、參數、回傳」等等 API 資訊都清楚明瞭的顯示，甚至還可以戳一戳，直接呼叫 API 來動手試試。更重要的是：這些都是自動產生的！所以說，Swagger，好！

也因為 Swagger 是一種工具，所以大多主流語言都會有支援 Swagger 的工具包，例如 Golang 的 swag 和 go-swagger。

在 Dotnet 陣營裡面，作為代表的則是 [Swashbuckle](https://github.com/domaindrivendev/Swashbuckle.AspNetCore) 和 [NSwag](https://github.com/RicoSuter/NSwag)。由於工作團隊採用前者，故本篇將會以 Swashbuckle 來逐步實作。

> 對 NSwag 有興趣，或是工作要求採用的朋友。可以參閱以下資料：
>
> - [使用Swagger自動建立清晰明瞭的REST API文件 - 我與 ASP.NET Core 的 30天](https://ithelp.ithome.com.tw/articles/10242295)
> - 微軟文件的 [NSwag 與 ASP.NET Core 使用者入門](https://docs.microsoft.com/zh-tw/aspnet/core/tutorials/getting-started-with-nswag?view=aspnetcore-5.0&tabs=visual-studio)

## 安裝 Swashbuckle 及啟用 Swagger

現在讓我們把鏡頭回到我們在[上一篇](https://igouist.github.io/post/2021/05/newbie-3-dapper)裡使用 .net Core 預設的 Web API 範本建立的簡易 CRUD 服務。

首先，直奔 Nuget、搜尋 Swashbuckle，應該可以看到一整排：

![img](https://i.imgur.com/9vn5HUG.png)

我們這個示範專案的環境是 .net Core，所以我們選擇 `Swashbuckle.AspNetCore`，安裝了懶人包，就等於裝好了 Swashbuckle 家的 OpenAPI 三劍客 Swagger、SwaggerGen、SwaggerUI，之後的文件產生和進階操作也就不用煩惱了。

> 環境不是 .net Core 的 Asp.net Web API 朋友，請安裝 `Swashbuckle`，不過整體操作和顯示上並不會相差太多。
>
> 此外，在安裝和操作上也可以參照 mrkt 大大的 Swagger 相關文章：
>
> - [ASP.NET Web API 文件產生器 - 使用 Swagger - mrkt 的程式學習筆記](https://kevintsengtw.blogspot.com/2015/12/aspnet-web-api-swagger.html)
> - [Swashbuckle - Swagger for Web Api 顯示內容的調整 - mrkt 的程式學習筆記](https://kevintsengtw.blogspot.com/2015/12/swashbuckle-swagger-for-web-api.html)

![img](https://i.imgur.com/En0Aarn.png)

安裝完成之後，就讓我們來註冊 Swagger 服務吧！

首先讓我們到 `Startup.cs` 的 `ConfigureServices`，加上 `services.AddSwaggerGen();` 把 Swagger 的服務掛上去：

```csharp
// This method gets called by the runtime.
// Use this method to add services to the container.
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();

    services.AddSwaggerGen(); // 註冊 Swagger
}
```

接著往下看，到 `Configure` 把 Swagger 服務打開，我們需要加上 `UseSwagger` 讓它能夠用 middleware 產生 API 文件的 JSON，並用 `UseSwaggerUI` 指定 JSON 檔案來產生 API 文件的 UI 頁面。

```csharp
app.UseSwagger();
app.UseSwaggerUI(c =>
{
    c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1");
});
```

這樣就啟用了 Swagger 的服務了。

現在讓我們執行偵錯，並且到專案目錄底下的 `/swagger` 路徑（以我為例就是 `localhost:44304/swagger`），應該就能看到 Swagger 工具的介面啦！

![img](https://i.imgur.com/odrQ5IO.png)

並且在上面可以注意到我們自動生成的 API JSON 文件，也就是前面註冊時看過的 `/swagger/v1/swagger.json`（以我為例就是 `localhost:44304/swagger/v1/swagger.json`）

![img](https://i.imgur.com/HysAWQu.png)

這邊大致上就可以了解到，Swagger 工具就是藉由去掃我們的 `ApiController`，產生出對應的 API 規格的 JSON 檔案，再讀取這個 JSON 檔案來產生出 Swagger 的 UI 頁面。

> 補充：這邊也可以對 Swagger 的 UI 路徑進行設定，不一定要在 `/swagger` 底下。只需要在 `UseSwaggerUI` 中使用 `RoutePrefix` 就可以指定 Swagger UI 的 Route。
>
> 例如說我想要一進來我們服務的網址，就直接顯示 Swagger 畫面，像是 `myapi.com` 就顯示 Swagger UI 而非 `myapi.com/swagger` 的時候，就可以這樣設定：
>
> ```csharp
> app.UseSwaggerUI(c =>
> {
>    c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1");
>    c.RoutePrefix = string.Empty; // 指定路徑為 ""
> });
> ```
>
> 這樣就會直接在指定的路徑顯示 Swagger UI 囉！

> 補充：如果有在 `Properties/launchSettings.json` 設定偵錯時的起始頁面的朋友，也可以試試把起始頁面 `launchUrl` 設定成 Swagger UI 的路徑，例如 `"launchUrl": "swagger"`，平常測試的時候會順手很多，推薦給大家

接著讓我們用 Swagger UI 來測試一下 API 吧，首先讓我們新增一張卡片，選擇新增卡片的 API 並試試 `Try it out`，可以看到範例和輸入 Body 的區塊：

![img](https://i.imgur.com/8ruN7w9.png)

執行之後下方就會告訴我們執行結果和回傳：

![img](https://i.imgur.com/UUm4v20.png)

接著試試用 Swagger UI 來 GET 看看是不是真的有新增成功：

![img](https://i.imgur.com/I5eAVZm.png)

確認 Swagger UI 的確和我們的 CardController 銜接在一起了，啟用服務成功！

## 使用 SwaggerDoc 增加專案描述

不過現在只是一個可以互動的操作介面而已，離可以取代文件還有一段距離，接著就讓我們一步一步來增加資訊到這個 UI 介面吧。

首先讓我們回到 `ConfigureServices`，修改一下 `AddSwaggerGen`，讓我們可以丟東西進去，這邊就直接用微軟文件的範例來稍作修改：

```csharp
services.AddSwaggerGen(c =>
{
    // API 服務簡介
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "菜雞 API",
        Description = "菜雞新訓記的範例 API",
        TermsOfService = new Uri("https://igouist.github.io/"),
        Contact = new OpenApiContact
        {
            Name = "Igouist",
            Email = string.Empty,
            Url = new Uri("https://igouist.github.io/about/"),
        },
        License = new OpenApiLicense
        {
            Name = "TEST",
            Url = new Uri("https://igouist.github.io/about/"),
        }
    });
});
```

這邊可以填入版本、API 名稱和說明、聯絡方式等資訊，這些資訊會顯示在 Swagger UI 的開頭：

![img](https://i.imgur.com/9v4DssU.png)

替自己的服務加上說明是絕對必要的，不過平時會比較常用的也是 `Title`、`Description` 這些基本欄位，各位再按照自己的服務調整吧。

## 使用 XML 文件和 IncludeXmlComments 從註解產生 API 說明

我們有了整個服務的說明之後，當然也要替每一支 API 補上說明啦！

這邊我們可以採用產生 XML 檔案的方式來讓 Swagger 取得每支 API 在 Function 上的註解，這樣就能自動產生 API 的說明了。

首先就是要打開 XML 文件，先讓我們從 `方案總管` 對我們的專案 `右鍵`，選擇 `屬性`：

![img](https://i.imgur.com/Iol6yxX.png)

進入屬性頁之後，到 `建置`，找到 `XML 文件檔案` 並勾選起來，通常會自動幫你填入路徑：

![img](https://i.imgur.com/qWU9iJP.png)

> 補充：並非使用 Visual Studio 開發的朋友，也可以參考微軟文件的開啟方式：打開 `.csproj` 檔案，並找到 `PropertyGroup` 加上 `GenerateDocumentationFile` ，並設為 true，例如：
>
> ```xml
> <PropertyGroup>
>  <GenerateDocumentationFile>true</GenerateDocumentationFile>
> </PropertyGroup>
> ```

> 補充：如果開啟 XML 文件檔案的選項後，建置或偵錯時跳出找不到 XML 檔案的錯誤，可能是生成失敗，可以嘗試改用系統管理員開啟 Visual Studio 再重新建置。

完成並儲存之後，讓我們回到 `ConfigureServices` 的 `AddSwaggerGen` 部分，把讀取 XML 的命令也加進去：

```csharp
var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
c.IncludeXmlComments(xmlPath);
```

如果在上一個步驟有加入專案描述，現在的 `AddSwaggerGen` 可能會長這樣：

```csharp
services.AddSwaggerGen(c =>
{
    // API 服務簡介
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "菜雞 API",
        Description = "菜雞新訓記的範例 API",
        TermsOfService = new Uri("https://igouist.github.io/"),
        Contact = new OpenApiContact
        {
            Name = "Igouist",
            Email = string.Empty,
            Url = new Uri("https://igouist.github.io/about/"),
        }
    });

    // 讀取 XML 檔案產生 API 說明
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
    c.IncludeXmlComments(xmlPath);
});
```

> 小提示：這邊的 `xmlFile` 路徑是對照前面步驟 專案屬性中的 XML 產生路徑，並用反射的方式去符合自動產生路徑的規則拿到 XML 檔案。
>
> 如果在前面的步驟有自己指定 XML 檔案產生路徑的朋友，這邊的 `xmlFile` 也要記得和 XML 檔案路徑對應上呦。

最後也是最重要的一步：確保你的 ApiController 底下的各 API 有乖乖加上註解：

![img](https://i.imgur.com/yVQQIln.png)

> 小提示：搭配 [GhostDoc](https://marketplace.visualstudio.com/items?itemName=sergeb.GhostDoc) 自動產生註解，又快又香！用過就回不去了。
>
> 相關的說明可以參見：[使用 GhostDoc 自動產出符合語意的註解 - 搞搞就懂](https://dotblogs.com.tw/wasichris/2016/01/21/172429)

確定 對專案開啟產生 XML、讓 Swagger 讀取 XML、乖乖寫註解 三個步驟都有完成之後，就可以開啟 Swagger UI 來看看啦！

![img](https://i.imgur.com/quHdcGV.png)

可以看到每支 API 都有顯示註解的名稱了，讓我們跟沒有的時候比對一下：

![img](https://i.imgur.com/TsroNer.png)

是不是貼心多了呢？

並且如果對參數、傳入和傳出的 Model 都有確實加上註解的話，在 API 的內容頁面就可以直接看到 QueryString 的參數，並且對 Model 點選 Schema 也會顯示 Model 的說明：

![img](https://i.imgur.com/pI9OJQD.png)

![img](https://i.imgur.com/kPQRL9m.png)

如此一來參數和回傳，從名稱、說明、型別和範例都有了，這樣才有 API 文件的感覺嘛！

除了基本的 `summary` 用來標示 API 的用途、`param` 用來標記參數名稱之外，比較特別的就是可以加上 `remarks` 來替 API 做更詳細的說明，例如：

![img](https://i.imgur.com/E79TDpY.png)

這樣就會顯示在 Swagger UI 上該 API 點開的內文中：

![img](https://i.imgur.com/ZFDLWsv.png)

很適合用來進行更詳細的說明和備註。

通常我們做到這裡就差不多了已經具備 API 文件該有的部分了，不過資訊當然是多多益善嘛，接著就讓我們來補充一些小東西上去吧～

## 使用 Produces 屬性和 response 註解補充回傳資訊

我們在 [API 的介紹](https://igouist.github.io/post/2021/05/newbie-2-webapi) 有提到：API 的回傳有許多格式，例如最常見的 JSON、XML，或者是純文字和檔案等等。

同時，我們也提過 API 可能會根據不同狀況，也會有不同的 HTTP Status 回應，例如 404: 找不到。但讓我們確認一下我們現在的文件…

![img](https://i.imgur.com/IhWDMBe.png)

看起來預設的 Media type 並沒有作用，並且也只有 200 成功時的狀況。現在就讓我們來補充一下吧！

在目標的 Api 方法上加上 `[Produces("application/json")]` 就可以標示該方法的回傳格式為 `application/json`，例如：

![img](https://i.imgur.com/9S1o9sH.png)

這樣在 Swagger UI 上該 API 的 Responses 就會標記為指定的格式：

![img](https://i.imgur.com/OjRt09o.png)

接著，讓我們用 `ProducesResponseType` 來指定回傳時的型別，以及在註解中使用 `<response>` 標籤來替回傳時的 HTTP Status 加上說明吧：

```csharp
/// <summary>
/// 查詢卡片
/// </summary>
/// <remarks>我是附加說明</remarks>
/// <param name="id">卡片編號</param>
/// <returns></returns>
/// <response code="200">回傳對應的卡片</response>
/// <response code="404">找不到該編號的卡片</response>          
[HttpGet]
[Produces("application/json")]
[ProducesResponseType(typeof(Card), 200)]
[Route("{id}")]
public Card Get([FromRoute] int id)
{
    var result = this._cardRepository.Get(id);
    if (result is null)
    {
        Response.StatusCode = 404;
        return null;
    }
    return result;
}
```

![img](https://i.imgur.com/I90gVGu.png)

這樣做的 Swagger UI 就會多出這些 HTTP Status 對應的資訊囉：

![img](https://i.imgur.com/owvkBq4.png)

到這邊我們就提供了各種情況對應的回傳啦，隔壁同事如果問你說「為啥我打是回 400 啊？」就可以對他說「[RTFW](https://www.urbandictionary.com/define.php?term=RTFW)！」

> (2021/7/3) 補充：
>
> 我們可以在方法上加上 `[Obsolete]` 的已過時屬性，這樣 Swagger 也會用刪除線或反灰的方式告訴使用者該方法已經要被淘汰囉。
>
> 在敝司這次的專案重構，進行 API 接口的翻新和淘汰時，就使用了 `[Obsolete]` 來進行標記那些被淘汰的方法和可改用的新方法，挺方便的。
>
> 關於 `[Obsolete]`，可以參見 m@rcus 學習筆記的這篇：[設定方法 (Method) 已過時 - Obsolete](https://marcus116.blogspot.com/2019/10/csharper-method-obsolete.html)

## 小結

這篇記錄了 Swagger 自動產生 API 規格文件的作法，從 API 的路由、說明、參數、Model 跟回傳值全方位說明，還可以試打 API，可以說是完美提供健全的 API 環境啦。

阿彌陀佛阿彌陀佛，所謂寫一篇文件勝造七級浮屠，這個 Swagger 開下去，還不飛昇當神去了。正是：API 文件寫得好，同事溝通沒煩惱；Swagger 用得好，生文件只要一秒。

![img](https://i.imgur.com/THIt8EI.png)

那麼今天就記錄到這邊，最後就快速整理一下：

－ 關於 Swagger －

- 為了提升溝通的效率、確保將來能記得用法，因此我們要寫 API 規格文件
- 為了提升寫文件的效率（和懶惰），因此我們可以嘗試自動產生 API 規格文件
- Swagger（OpenAPI），是一套 API 互動文件產生器，是幫助我們來自動產生 API 規格文件和測試的好幫手
  - 在 Dotnet 陣營裡以 Swashbuckle 和 NSwag 最常見

－ 關於 Swashbuckle －

- 在 NuGet 安裝 `Swashbuckle.Core`

- 在 `Startup.cs` 的 `ConfigureServices` 加上 `services.AddSwaggerGen();` 註冊服務

- 在 `Startup.cs` 的 `Configure` 加上 `UseSwagger` 產生 API 文件的 JSON

- 在 `Startup.cs` 的 `Configure` 加上 `UseSwaggerUI` 來使用 JSON 產生 API 文件的 UI 頁面

- 在 `AddSwaggerGen` 中，使用 `SwaggerDoc` 和 `OpenApiInfo` 加上服務描述

- 在

   

  ```
  AddSwaggerGen
  ```

   

  中，使用

   

  ```
  IncludeXmlComments
  ```

   

  讀取 XML 註解並產生 API 描述（需要先對專案開啟產生 XML 檔案）

  - 在

     

    ```
    ApiController
    ```

     

    的各個 API 接口加上 XML 註解，最常見的有

    - `summary` 用來標示 API 描述
    - `param` 用來標示參數描述
    - `remarks` 用來標示 API 服務的說明
    - `response` 用來標示回傳的狀態碼說明

  - 在 API 接口上加上 `[Obsolete]` 標示已過時

- 在 `ApiController` 的各個 API 接口加上 `[Produces]` 來標記回傳格式

- 在 `ApiController` 的各個 API 接口加上 `[ProducesResponseType]` 來標記回傳狀態對應的型別

今天的紀錄就到這邊，之後如果還有發現什麼小技巧再回來補充，也歡迎幫忙告訴我還能怎麼使用。

那麼，我們下次見～

> 本系列下一篇：[菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)

## 相關文章

- [在 Swagger UI 加上驗證按鈕，讓 Request Header 傳遞 Authorize Token](https://igouist.github.io/post/2021/10/swagger-enable-authorize/)

## 參考資料

- [Swashbuckle 與 ASP.NET Core 使用者入門 | Microsoft Docs](https://docs.microsoft.com/zh-tw/aspnet/core/tutorials/getting-started-with-swashbuckle?view=aspnetcore-5.0&tabs=visual-studio)
- [dotnet Core WebApi實作(使用Dapper、Swagger、Postman)-2 (sunnyday0932.github.io)](https://sunnyday0932.github.io/2020/dotnet-core-webapi實作使用dapperswaggerpostman-2/)
- [mrkt 的程式學習筆記: ASP.NET Web API 文件產生器 - 使用 Swagger (kevintsengtw.blogspot.com)](https://kevintsengtw.blogspot.com/2015/12/aspnet-web-api-swagger.html)
- [mrkt 的程式學習筆記: Swashbuckle - Swagger for Web Api 顯示內容的調整 (kevintsengtw.blogspot.com)](https://kevintsengtw.blogspot.com/2015/12/swashbuckle-swagger-for-web-api.html)
- [Swagger 初試筆記-黑暗執行緒 (darkthread.net)](https://blog.darkthread.net/blog/swagger-notes-1/)
- [使用 Swagger 自動建立清晰明瞭的 REST API文件 - 我與 ASP.NET Core 的 30天 - iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10242295)
- [ASP.NET Core 2 系列 - Web API 文件產生器 (Swagger)](https://ithelp.ithome.com.tw/articles/10195190)
- [原來後端要知道 - 如何寫 API 文件？ - iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10230804)
- [使用 Swagger 自動產生 API 文件 | by 11 | Medium](https://yunchenli.medium.com/使用swagger自動產生api文件-a8f5c65d267c)

## 本系列文章

- [菜雞新訓記 (0): 目錄](https://igouist.github.io/post/2021/04/newbie-0-menu)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger)
- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)
- [菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection)
- [菜雞新訓記 (7): 使用 FluentValidation 來驗證傳入參數吧](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation)

## 其他文章

- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi/)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper/)
- [菜雞新訓記 (0): 前言](https://igouist.github.io/post/2021/04/newbie-0-menu/)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git/)
- [菜雞與物件導向 (Ex1): 小結](https://igouist.github.io/post/2021/01/oo-ex1-end2020/)