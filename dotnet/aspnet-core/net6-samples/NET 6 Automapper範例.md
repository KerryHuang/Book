---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/AutoMapperExample
author: CI-YU
---

# .NET 6 Automapper範例

## 目的

快速對應，不需要寫linq來將資料庫端的model對應到view要用的model

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟一](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟二](https://user-images.githubusercontent.com/19286751/150151645-46df6dfe-a981-4a46-8f2e-7143ada3f503.png)

### 其他資訊

直接進行下一步
![步驟三](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

透過NuGet安裝AutoMapper.Extensions.Microsoft.DependencyInjection
![步驟4](https://user-images.githubusercontent.com/19286751/150152375-7e9590a3-155b-45c4-8f97-040c4feca36c.png)

### 編輯Program.cs檔案

註冊AutoMapper

```c#
//找到所有繼承profile
builder.Services.AddAutoMapper(AppDomain.CurrentDomain.GetAssemblies());
```

![步驟5](https://user-images.githubusercontent.com/19286751/150171450-fc1077d4-e27e-42a9-815f-e508f9c44186.png)

### 新增Mappings資料夾與Models資料夾

![步驟6](https://user-images.githubusercontent.com/19286751/150153595-fbf8e4a9-57b8-44e5-82a6-f1a7c439248d.png)

### 在Models資料夾內加入DbModel資料夾與ViewModel資料夾

![步驟7](https://user-images.githubusercontent.com/19286751/150154151-14c8f746-5550-4172-9580-ae3b0b7bc71b.png)

### 加入類別檔

在兩個資料夾內加入同名稱的類別檔案
![步驟8](https://user-images.githubusercontent.com/19286751/150154607-ff7ab43f-b2cc-47dd-beae-d00ba29c9117.png)

- DbModel.cs寫入程式碼

```c#
    public int Id { get; set; }
    public string? Name { get; set; }
    public int Age { get; set; }
    public DateTime CreatedDate { get; set; }
```

> 可能會有些人問?是什麼，這是因為建立.net6專案預設會開啟判斷值可能為null的警告訊息，可以加上?代表允許此屬性為null，會建議在建構子時提供預設值，來避免嘗試對null值做處理的exception。

![步驟8-1](https://user-images.githubusercontent.com/19286751/150158192-aafbf5cc-876d-4876-9806-c3a9bc32bddd.png)

- ViewModel.cs寫入程式

```c#
    public ViewModel() { 
    Name = string.Empty;
    }
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
```

> 在建構子提供預設值後，來避免對null做處理。

![步驟8-2](https://user-images.githubusercontent.com/19286751/150158960-eb7dc043-77e0-413a-bb74-f5abe1f7b8a4.png)

### 加入類別檔

在Mappings資料夾內加入名稱為ExampleMapping的類別檔
![步驟9-1](https://user-images.githubusercontent.com/19286751/150160741-668aa223-ce75-4079-96c8-e2cadb4ed921.png)

- 寫入程式 在新增的ExampleMapping.cs檔案內寫入程式碼

```c#
using AutoMapper;
using AutoMapperExample.Models.DbModel;
using AutoMapperExample.Models.ViewModel;

namespace AutoMapperExample.Mappings {
  //需要繼承AutoMapper的Profile
  public class ExampleMapping : Profile {
    public ExampleMapping() {
      //來源與目標=>白話文是我要將DbModel對應到ViewModel
      CreateMap<DbModel, ViewModel>();
    }
  }
}
```

![步驟9-2](https://user-images.githubusercontent.com/19286751/150163037-48cec3e2-d3ff-4a7f-b3ba-98ebbc0fc8e0.png)

### 加入檔案

在Controllers加入一個空白的API控制器，並命名為ExampleController.cs
![步驟10-1](https://user-images.githubusercontent.com/19286751/150167913-85b03450-b173-4ea4-82b0-9725d027c045.png)

![步驟10-2](https://user-images.githubusercontent.com/19286751/150168059-90a3f2e4-b18b-4b88-a009-f6e2b40916f7.png)

- 寫入程式

```c#
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using AutoMapperExample.Models.DbModel;
using AutoMapperExample.Models.ViewModel;
using AutoMapper;

namespace AutoMapperExample.Controllers {
  [Route("api/[controller]")]
  [ApiController]
  public class ExampleController : ControllerBase {

    private readonly IMapper _mapper;
    public ExampleController(IMapper mapper) {
      _mapper = mapper;
    }
    [HttpGet("Index")]
    public IEnumerable<ViewModel> Index() {
      var DbModel = new List<DbModel>();
      //新增DbModel的List模擬從資料庫來的資料
      DbModel.Add(new DbModel() { Id = 1, Name = "Bill", Age = 18, CreatedDate = DateTime.Now });
      DbModel.Add(new DbModel() { Id = 1, Name = "CI-YU", Age = 20, CreatedDate = DateTime.Now });
      DbModel.Add(new DbModel() { Id = 1, Name = "Bill Huang", Age = 22, CreatedDate = DateTime.Now });
      //將DbModel資料自動與ViewModel做對應(相同名稱的屬性)
      var map = _mapper.Map<IEnumerable<ViewModel>>(DbModel);
      return map;
    }
  }
}
```

![步驟10-3](https://user-images.githubusercontent.com/19286751/150169646-ab71d0b2-5b68-4f22-9836-98a7d6c3f3c6.png)

### 執行結果

可以自動對應到結果了。
![範例11-1](https://user-images.githubusercontent.com/19286751/191064600-da8ad592-99df-40d4-9c76-6a1bda469ccb.png)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/AutoMapperExample)