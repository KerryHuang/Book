# .NET 6 HttpClient單元測試範例

### 目的

面試的時候被問到要如何做包含**外部api**的單元測試問題，稍微查一下其實很簡單，怎麼當下答不出來呢? 主要有兩種方式，一種為.net core 2.1以後有提供IHttpClientFactory的介面可以使用。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟一](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟二](https://user-images.githubusercontent.com/19286751/148767290-44bc0e8d-22eb-4b98-a727-af5b2f4677a7.png)

### 其他資訊

直接進行下一步
![步驟三](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 建立資料夾

![步驟四](https://user-images.githubusercontent.com/19286751/148767905-501f97a0-fd59-4e38-a21c-6155097b4689.png)

### 編輯Program.cs檔案

註冊AddHttpClient。

```c#
builder.Services.AddHttpClient();
```

![步驟五](https://user-images.githubusercontent.com/19286751/148769889-2a36dbbe-1402-4dea-8235-036bfdd609ff.png)

### 新增一個類別檔

- 加入前
![步驟6-1](https://user-images.githubusercontent.com/19286751/148770868-0f177281-56b2-455e-9d8d-89b98d8b4a6f.png)
- 加入後
![步驟6-2](https://user-images.githubusercontent.com/19286751/148771237-33e27b6e-4525-4ab7-98b2-c9b954d23aef.png)

### 建構子注入

將註冊的httpclient透過建構子注入

```c#
    readonly IHttpClientFactory _httpClientFactory;
    public CallAPIServices(IHttpClientFactory httpClientFactory) {
      _httpClientFactory = httpClientFactory;
    }
```

- 加入前
![步驟7-1](https://user-images.githubusercontent.com/19286751/148771846-62cc6b87-ec0d-41ab-9331-e39e67b0573f.png)

- 加入後
![步驟7-2](https://user-images.githubusercontent.com/19286751/148771643-b0764e60-b561-468c-85ed-445a99f4b987.png)

### 新增方法

新增一個會去發外部請求的方法，模擬當有包含第三方api時如何測試

```c#
    public async Task<string> Get() {
      var client = _httpClientFactory.CreateClient();
      var response = await client.GetAsync("https://example.com");
      if (response.IsSuccessStatusCode) {
        var responseString = await response.Content.ReadAsStringAsync();
        return responseString;
      }
      return "";
    }
```

![步驟8](https://user-images.githubusercontent.com/19286751/148773941-4afa7cfc-d592-46c4-9496-30729de428f3.png)

### 新增測試專案

> 對方案點選右鍵>加入>新增專案

![步驟9](https://user-images.githubusercontent.com/19286751/148776104-c14be0ec-ce3a-4a9e-b0d3-ed060ec566eb.png)

### 設定新的專案

替測試專案命名，建議命名規則以.Tests做結尾
![步驟10](https://user-images.githubusercontent.com/19286751/148776565-502dd4f9-b959-4d2e-8535-07a2ab59c301.png)

### 其他資訊

專案架構需要與要測試的專案相同
![步驟11](https://user-images.githubusercontent.com/19286751/148776689-bb62c741-fe5a-4e01-bbb1-39e51ecff11b.png)

### 加入參考

將要測試的專案加入測試專案

> 對CallAPIServices.Tests點選右鍵>加入>專案參考

![步驟12](https://user-images.githubusercontent.com/19286751/148793680-d99d41f2-f650-406f-bbb7-8002ffdc0778.png)

### NuGet加入套件

透過NuGet安裝Moq套件至測試專案
![步驟13](https://user-images.githubusercontent.com/19286751/149161402-7e7eae0b-406d-47d6-8171-ac7a8aa46111.png)

### 新增對應資料夾與測試檔案

新增檔案，檔名需要與要測試的檔案一致，並加上**Tests**
![步驟14](https://user-images.githubusercontent.com/19286751/149358298-e6998a2b-5154-40ff-b669-67333e3ca93d.png)

### 新增程式碼

在新增的檔案內新增一個方法並寫入程式碼，一開始會看到許多紅色波浪，是因為沒有加入參考

```csharp
    //定義這個方法是不需要傳入參數的單元測試，另一種為[Theory]，詳細說明可看相關參考5
    [Fact]
    //命名規則 => 類別名稱_方法名稱_要測試的方法行為_回傳狀態
    public async Task CallAPIServices_Get_HttpClient_Success() {
      //模擬出一個IHttpClientFactory的假物件
      var mockFactory = new Mock<IHttpClientFactory>();
      //產生http回傳的實例
      HttpResponseMessage result = new HttpResponseMessage() {
        StatusCode = HttpStatusCode.OK,
        Content = new StringContent("{'account':'bill','age':18}")
      };
      //模擬出一個http處理程序的基本類型實例的假物件
      var mockHttpMessageHandler = new Mock<HttpMessageHandler>();
      //模擬http發出請求後所做的一連串事情，最後並回傳結果
      //protected => 發出請求的方法SendAsync是一個protected存取修飾詞，不能直接存取，所以告訴moq請幫忙執行protected方法，詳細說明可看參考6
      //Setup => 設定此執行動作為SendAsync方法，並需要兩個傳入參數，HttpRequestMessage與CancellationToken
      //ItExpr.IsAny => 請moq協助傳入一個參數為HttpRequestMessage與CancellationToken的假參數，另一種為It.IsAny是非protected方法使用
      //ReturnsAsync => 回傳非同步的值
      mockHttpMessageHandler.Protected()
          .Setup<Task<HttpResponseMessage>>("SendAsync", ItExpr.IsAny<HttpRequestMessage>(), ItExpr.IsAny<CancellationToken>())
          .ReturnsAsync(result);
      //將製作好的假請求與回傳給HttpClient
      var client = new HttpClient(mockHttpMessageHandler.Object);
      //模擬實際請求，並接收到我們所製作的假物件
      mockFactory.Setup(_ => _.CreateClient(It.IsAny<string>())).Returns(client);
      //將製作好的完整請求流程給我們在使用的方法
      var services = new HttpclientExample.Services.CallAPIServices(mockFactory.Object);
      //執行要測試的方法
      var response = await services.Get();
      //回傳值不能為null
      Assert.NotNull(response);
      //回傳值必須一致
      Assert.Equal("{'account':'bill','age':18}", response);
    }
```

- 加入前
![步驟15-1](https://user-images.githubusercontent.com/19286751/149377202-03626eb3-943b-4831-a7c9-3aea7a757009.png)

![步驟15-2](https://user-images.githubusercontent.com/19286751/149377567-b8de78fb-0171-4ae3-a2e6-2df3bfb5a5de.png)

- 加入後
![步驟15-3](https://user-images.githubusercontent.com/19286751/149376875-ab644b74-a755-4b0c-8939-3dedbd356e4f.png)

![步驟15-4](https://user-images.githubusercontent.com/19286751/149377496-2b27d806-8b4f-4c3e-9e72-ea6b640c9167.png)

### 執行測試

點右鍵執行測試，最後結果會如左下角顯示成功
![步驟16](https://user-images.githubusercontent.com/19286751/150145582-3c5792d0-6939-4a9a-a6dd-7a702b7ae3f1.jpg)

## 相關參考

[單元測試好的做法](https://docs.microsoft.com/zh-tw/dotnet/core/testing/unit-testing-best-practices) [為什麼要使用IHttpClientFactory](https://docs.microsoft.com/zh-tw/dotnet/architecture/microservices/implement-resilient-applications/use-httpclientfactory-to-implement-resilient-http-requests#benefits-of-using-ihttpclientfactory) [moq套件介紹](https://www.code4it.dev/blog/testing-httpclientfactory-moq) [單元測試介紹](https://www.thecodebuzz.com/tdd-unit-testing-naming-conventions-and-standards/) [Fact跟Theory差別](https://stackoverflow.com/questions/22373258/difference-between-fact-and-theory-xunit-net) [存取修飾詞](https://docs.microsoft.com/zh-tw/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/HttpclientExample)