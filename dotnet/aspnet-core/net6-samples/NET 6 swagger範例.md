---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/SwaggerExample
author: CI-YU
---

# .NET 6 swagger範例

### 目的

每次要使用swaggerUI時候範例總是各式各樣，千奇百怪，下列範例是使用官方預設的Swashbuckle套件來教學。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟一](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟二](https://user-images.githubusercontent.com/19286751/143256840-e7546057-3f12-4622-8cb2-d996175a51e9.png)

### 其他資訊

選擇.net6版本，支援OpenAPI支援一定要勾選，此選項.net5以後才會有，.net core 3.1並沒有此選項，需要從NuGet安裝，並點建立
![步驟三](https://user-images.githubusercontent.com/19286751/143257352-79b0ced0-fdba-4846-8275-f35ce5bffc7f.png)

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

修改program檔案內容，調整AddSwaggerGen的內容，目的是為了可以讀取我們所寫的註解 program檔案與.net5以前不一樣，保哥的[部落格](https://blog.miniasp.com/post/2021/10/25/ASP-NET-Core-6-Project-Template-and-CSharp-10-New-Features)有比較詳細的說明

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

### 編輯WeatherForecastController檔案

這裡有個**重點**，如果要增加下一個action時候，預設的範例檔案，需要調整route的設定，才能讀取到，不然會跳錯誤訊息

- 加入前
![步驟6-1](https://user-images.githubusercontent.com/19286751/143261906-a4d3ead6-27fa-4692-99a5-79b130e9373d.png)

- 加入後
![步驟6-2](https://user-images.githubusercontent.com/19286751/143262285-c6239607-6b20-4176-a337-206b778a1d67.png)

加入第二個方法
![步驟6-3](https://user-images.githubusercontent.com/19286751/143273239-f336fbbf-8128-43e6-9f87-48397741d7f7.png)

### 執行結果

就可以成功讀取到兩個方法了
![步驟6-4](https://user-images.githubusercontent.com/19286751/143273674-0c85bad9-9e8c-48bf-a645-28991b458aa5.png)

### 參考

[微軟官方](https://docs.microsoft.com/en-us/aspnet/core/tutorials/getting-started-with-swashbuckle?view=aspnetcore-6.0&tabs=visual-studio)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/SwaggerExample)