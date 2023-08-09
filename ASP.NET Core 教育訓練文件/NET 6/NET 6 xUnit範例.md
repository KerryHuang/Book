# .NET 6 xUnit範例

### 目的

單元測試

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![範例2-1](https://user-images.githubusercontent.com/19286751/194479249-f9f9b167-e231-48d9-bfc8-993592523bcf.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 建立新的類別庫

進行命名時通常會與要測試的專案同名並加上結尾`.Tests`，以此範例就會變成`xUnitExample.Tests`
![範例4-1](https://user-images.githubusercontent.com/19286751/194478957-a37a0632-dfdf-4d41-b91c-f5ebc2ba5d0a.png)

![範例4-2](https://user-images.githubusercontent.com/19286751/194479052-2b9d9783-e457-4327-b6f1-d140440f96e8.png)

![範例4-3](https://user-images.githubusercontent.com/19286751/194479385-eb09c8a2-7503-4bbc-884c-418a17e3fe26.png)

### NuGet加入套件

針對xUnitExample.Tests加入相關套件

- xunit
- xunit.runner.visualstudio
- Microsoft.NET.Test.Sdk
- coverlet.collector

![範例5-1](https://user-images.githubusercontent.com/19286751/194501068-d315650e-77b3-4a87-8e34-e8d07c060f86.png)

### 新增Calculator.cs類別檔

在xUnitExample專案新增Calculator.cs類別檔
![範例6-1](https://user-images.githubusercontent.com/19286751/194501945-44193e5e-fb17-43f8-b5c1-73a3e53790ed.png)新增一個簡單的加法函式

```C#
  public static class Calculator {
    public static double Add(int a, int b) {
      return a + b;
    }
  }
```

![範例6-2](https://user-images.githubusercontent.com/19286751/194502632-95b3e9d3-f218-4363-b443-19f476d96988.png)

### 針對xUnitExample.Tests類別庫加入參考

引用要測試的專案，才能將測試與實際專案切分開來
![範例7-1](https://user-images.githubusercontent.com/19286751/194481272-736b7183-f967-4f0e-a495-d29d4fabeab5.jpg)

![範例7-2](https://user-images.githubusercontent.com/19286751/194481822-cbfb741c-e564-4397-aca8-cf8545cc3714.png)

### 新增CalculatorTests.cs類別檔

刪除預設的類別檔(Class1.cs)，建立對應的資料夾以及類別檔案，並在結尾加上`Tests`
![範例8-1](https://user-images.githubusercontent.com/19286751/194503023-1341df65-6d99-416d-be3b-a50fd50ef1bb.png)

### 編輯CalculatorTests.cs類別檔

測試都會分三個階段

- Arrange：準備階段，包含初始化相關資料
- Act：執行測試方法後所取得的結果
- Assert：驗證Act取得的結果是否符合預期結果

```C#
  public class CalculatorTests {
    //告訴編譯器要執行的測試方法
    [Fact]
    public void Add_() {
      //Arrange
      double Expected = 20;
      //Act
      var Actual = Calculator.Add(5, 15);
      //Assert
      Assert.Equal(Expected, Actual);
    }
  }
```

![範例9-1](https://user-images.githubusercontent.com/19286751/194506362-888e2cb6-5ecf-4e65-8b76-088bbcda9b21.png)

### 執行結果

> 點選測試>執行所有測試

![範例10-1](https://user-images.githubusercontent.com/19286751/194508692-d06ef526-8aed-4bc8-a987-f1578e0beabf.jpg)

下方視窗就會顯示成功或失敗
![範例10-2](https://user-images.githubusercontent.com/19286751/194510672-0c1998a6-2c3c-4a32-9dba-abe8d1af1b70.png)

### 後記

單元測試有另外兩種NUnit與mstest，基本上大同小異，並無太大的區別。

### 參考

[xUnit官網](https://xunit.net/docs/getting-started/netcore/cmdline) [該用什麼Packages](https://xunit.net/docs/nuget-packages)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/xUnitExample)