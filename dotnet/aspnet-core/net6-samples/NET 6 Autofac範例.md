---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/AutoFacExample
author: CI-YU
---

# .NET 6 Autofac範例

## 目的

批次註冊

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/150818232-53acaaf2-8cd5-4428-84fd-2129a7a80d8e.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

![步驟4](https://user-images.githubusercontent.com/19286751/150818596-1d0f0233-530c-49bb-a8ff-4b133313cb3f.png)

### 新增類別檔

新增之後需要來描述要批次注入的規則

- 加入前![步驟5-1](https://user-images.githubusercontent.com/19286751/150822860-782a88af-3589-4012-b924-e76508064c4b.png)
- 
- 加入後![步驟5-2](https://user-images.githubusercontent.com/19286751/150823083-ba45a741-8cb6-4a41-bae4-dcfc740a2739.png)

並且繼承autofac的類別Module
![步驟5-3](https://user-images.githubusercontent.com/19286751/150823828-218d5bbc-368f-4ca3-966b-d3520cf910ef.png)

### 編輯Program.cs檔案

```c#
//初始化並建立一個實例
builder.Host.UseServiceProviderFactory(new AutofacServiceProviderFactory());
//註冊autofac這個容器
builder.Host.ConfigureContainer<ContainerBuilder>(builder => builder.RegisterModule(new AutofacModuleRegister()));
```

![步驟5-1](https://user-images.githubusercontent.com/19286751/150821790-08efd03f-651b-41be-9441-a4a2efcd8e07.png)

有繼承autofac的類別Module
![步驟5-2](https://user-images.githubusercontent.com/19286751/150824053-c203cc0a-d275-4ca6-8224-d1f1086817d5.png)

### 新增資料夾

新增下圖兩個資料夾
![步驟6](https://user-images.githubusercontent.com/19286751/150994269-a6b62257-2e5b-40d0-82c5-52de17644f87.png)

### 新增類別檔

此次的目的是要可以進行批次注入，所以檔名結尾都需要包含**Service**，做批次注入時可以辨識

- 在Services資料夾底下加入類別檔案，名稱為TestService

![步驟7-1](https://user-images.githubusercontent.com/19286751/150996311-df912085-56b6-4efc-8bad-d3e71729de60.png)

- 在Interface資料夾底下加入介面檔案，名稱為ITest

![步驟7-2](https://user-images.githubusercontent.com/19286751/151011451-dd7a96eb-b2da-4860-92e1-1c42beb55b19.png)

- ITest.cs寫入程式

```c#
namespace AutoFacExample.Services.Interface {
  public interface ITest {
    public string GetName(string id);
  }
}
```

![步驟7-3](https://user-images.githubusercontent.com/19286751/151011702-e2dbf8ac-6e74-410b-8deb-23ac970b590d.png)

- TestService.cs寫入程式 繼承介面後寫上與介面相同的方法

```c#
using AutoFacExample.Services.Interface;

namespace AutoFacExample.Services {
  public class TestService : ITest {
    public string GetName(string id) {
      return $"{id}:Bill";
    }
  }
}
```

![步驟7-4](https://user-images.githubusercontent.com/19286751/151011931-029c0fd9-9dbc-4e4a-9600-f3b0cb779753.png)

### AutofacModuleRegister執行批次註冊

```c#
    protected override void Load(ContainerBuilder builder) {
    //RegisterAssemblyTypes => 註冊所有集合
    //Where(t => t.Name.EndsWith("Service")) => 找出所有Service結尾的檔案
    //AsImplementedInterfaces => 找到Service後註冊到其所繼承的介面 
      builder.RegisterAssemblyTypes(typeof(Program).Assembly)
            .Where(t => t.Name.EndsWith("Service"))
            .AsImplementedInterfaces();
    }
```

![步驟8](https://user-images.githubusercontent.com/19286751/151009841-9b8e7167-7655-4eaf-9611-bdb76768fc2d.png)

### 新增測試用controller

![步驟9-1](https://user-images.githubusercontent.com/19286751/151018422-888dc235-1ddb-45f5-b876-d7bf01f0ee8d.png)

![步驟9-2](https://user-images.githubusercontent.com/19286751/151018731-8f9515cd-63ba-4dd4-a27b-6fa5cee9428c.png)

- TestController.cs寫入程式

```c#
using AutoFacExample.Services.Interface;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AutoFacExample.Controllers {
  [Route("api/[controller]")]
  [ApiController]
  public class TestController : ControllerBase {
    //為隱私修飾詞並且唯讀
    private readonly ITest _test;
    //在建構子時注入需要使用的服務
    public TestController(ITest test) {
      _test = test;
    }
    [HttpGet("GetName")]
    public string Get(string id) { 
    //使用注入的服務
    return _test.GetName(id);
    }
  }
}
```

> 注入的服務都是使用介面，目的是之後方便抽換，才可以進行測試 命名原則都會加一個底線代表全域變數
![步驟9-3](https://user-images.githubusercontent.com/19286751/151019654-437a7f9f-db9b-4137-bf75-a8bd25d094a6.png)

### 執行結果

最終確認程式是可執行，就沒有問題了。
![步驟10-1](https://user-images.githubusercontent.com/19286751/151020764-3e3e2d0d-7a51-41a3-b3dd-cece7914f736.png)

### 參考

[.net6註冊autofac說明文件](https://docs.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-5.0#custom-dependency-injection-di-container) [參考文件](https://toyo0103.github.io/2018/07/12/【Autofac】生命週期/) [參考文件](https://ithelp.ithome.com.tw/articles/10277198?sc=iThomeR) [參考文件](https://dotblogs.com.tw/nigelhome/2017/09/22/autofac)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/AutoFacExample)