---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/MoqExample
author: CI-YU
---

# .NET 6 Moq範例

### 目的

進行單元測試時，可以隔絕依賴的項目。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![範例2-1](https://user-images.githubusercontent.com/19286751/194517937-1297a60a-d850-4934-8973-74d0ef33b74e.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 建立新的類別庫

進行命名時通常會與要測試的專案同名並加上結尾`.Tests`，以此範例就會變成`MoqExample.Tests`
![範例4-1](https://user-images.githubusercontent.com/19286751/194478957-a37a0632-dfdf-4d41-b91c-f5ebc2ba5d0a.png)

![範例4-2](https://user-images.githubusercontent.com/19286751/194522835-a7b0ada6-cb87-41f3-9548-263bbc3d7e8b.png)

![範例4-3](https://user-images.githubusercontent.com/19286751/194479385-eb09c8a2-7503-4bbc-884c-418a17e3fe26.png)

### NuGet加入套件

針對xUnitExample.Tests加入相關套件

- xunit
- xunit.runner.visualstudio
- Microsoft.NET.Test.Sdk
- coverlet.collector
- Moq

![範例5-1](https://user-images.githubusercontent.com/19286751/194524507-c106f332-8aaa-476d-8030-88290c272db4.png)

### 針對MoqExample.Tests類別庫加入參考

引用要測試的專案，才能將測試與實際專案切分開來
![範例6-1](https://user-images.githubusercontent.com/19286751/194587201-1a299065-1873-4fa5-acb1-018b4257d447.png)

![範例6-2](https://user-images.githubusercontent.com/19286751/194587575-75417dfe-f86a-4838-8d82-2d4838e732c8.png)

### 新增WeatherForecastControllerTests.cs類別檔

刪除預設的類別檔(Class1.cs)，並在MoqExample.Tests專案新增對應資料夾，與類別檔並加結尾`Tests`。
![範例7-1](https://user-images.githubusercontent.com/19286751/194525218-906dae2d-788a-48d9-87bf-bc0a10cd8818.png)

### 編輯WeatherForecastControllerTests.cs類別檔

測試都會分三個階段

- Arrange：準備階段，包含初始化相關資料
- Act：執行測試方法後所取得的結果
- Assert：驗證Act取得的結果是否符合預期結果 這次要測試的是controller，有注入Ilogger，如何將Ilogger隔開的關鍵就是使用Moq這個套件
![範例8-1](https://user-images.githubusercontent.com/19286751/194589131-8673c49f-ee3b-4452-bf14-c8e5c25707b9.png)

```C#
using Microsoft.Extensions.Logging;
using Moq;
using MoqExample.Controllers;
using Xunit;
namespace MoqExample.Tests.Controllers {
  public class WeatherForecastControllerTests {
    [Fact]
    public void Get() {
      //Arrange
      //透過mock將外界的介面包起來
      var MockLogger = new Mock<ILogger<WeatherForecastController>>();
      //當成物件傳入controller，代替實際的介面
      var Controllers = new WeatherForecastController(MockLogger.Object);
      //Act
      //執行要測試的函式
      var Results = Controllers.Get();
      //Assert
      //確認結果不為null
      Assert.NotNull(Results);
      //確認結果數量等於5
      Assert.Equal(5, Results.Count());
    }
  }
}
```

![範例8-2](https://user-images.githubusercontent.com/19286751/194590911-8f26ed2a-38fd-472b-91e1-f5cf68277f2d.png)

### 執行結果

> 點選測試>執行所有測試

![範例9-1](https://user-images.githubusercontent.com/19286751/194592024-209f5acd-6252-4040-8eec-380e99990be2.jpg)

下方視窗就會顯示成功或失敗
![範例9-2](https://user-images.githubusercontent.com/19286751/194592247-36e1a789-f5e4-4203-87d1-3c8a87798da7.png)

### 參考

[Moq-Quickstart](https://github.com/moq/moq4/wiki/Quickstart)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/MoqExample)