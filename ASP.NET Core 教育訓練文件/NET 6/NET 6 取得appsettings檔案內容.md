# .NET 6 取得appsettings檔案內容

### 目的

透過強行別的模式使用appsetting設定檔資料

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/162605693-91b5c04f-008e-49bb-bda3-c063bba0da4f.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 設定appsetting檔案

在appsetting新增一筆json資料

```json
  "PersonalInformation": {
    "Name": "Bill",
    "Age": 20
  }
```

![步驟4](https://user-images.githubusercontent.com/19286751/162606196-fe29d713-664d-4d7c-a42a-89faa7c14c61.png)

### 新增model資料夾，並在裡面新增AppsettingConfig類別檔

![步驟5](https://user-images.githubusercontent.com/19286751/162606275-9360ae88-fec5-4efa-9eb4-6b56ef0f9100.png)

### 編輯AppsettingConfig類別檔案

```c#
  public class PersonalInformation {
    public PersonalInformation() {
      Name = string.Empty;
    }
    public string Name { get; set; }
    public int Age { get; set; }
  }
```

![步驟6](https://user-images.githubusercontent.com/19286751/162606799-69973fe9-d465-4aaa-b8c1-d2cd2e3ba6b2.png)

### 編輯Program.cs檔案

在program.cs中把appsetting的來源綁定在PersonalInformation這個class上

```c#
builder.Services.Configure<PersonalInformation>(
    builder.Configuration.GetSection("PersonalInformation"));
```

![步驟7](https://user-images.githubusercontent.com/19286751/162624188-359f3b96-c656-4985-9208-2b496f604dad.png)

### 注入所需要的地方

注入到預設的WeatherForecastController中，就可以使用。

```c#
    private readonly PersonalInformation _options;

    public WeatherForecastController(ILogger<WeatherForecastController> logger, IOptionsMonitor<PersonalInformation> options) {
      _logger = logger;
      _options = options.CurrentValue;
    }
```

> 此範例使用的是IOptionsMonitor

|     選項模式     | 可使用singleton | 重載 | 具名選項 |
| :--------------: | :-------------: | :--: | :------: |
|     IOptions     |        V        |  X   |    X     |
| IOptionsSnapshot |        X        |  V   |    V     |
| IOptionsMonitor  |        V        |  V   |    V     |

![步驟8](https://user-images.githubusercontent.com/19286751/162624433-baa5b9c1-00d3-4664-8ebe-d293e4fb519b.png)

### 參考

[選項模式](https://docs.microsoft.com/zh-tw/aspnet/core/fundamentals/configuration/options?view=aspnetcore-6.0) [IOptions與IOptionsSnaphot與IOptionsMonitor](https://stackoverflow.com/questions/50788988/difference-between-ioptionsmonitor-vs-ioptionssnapshot) [程式範例參考](https://andrewlock.net/how-to-use-the-ioptions-pattern-for-configuration-in-asp-net-core-rc2/) [options差別](https://www.youtube.com/watch?v=Doj9W5Rv7vs)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/ConfigurationExample)