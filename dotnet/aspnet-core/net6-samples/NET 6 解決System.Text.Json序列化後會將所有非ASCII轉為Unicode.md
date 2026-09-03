---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/JsonExample_Advanced
author: CI-YU
---

# .NET 6 解決System.Text.Json序列化後會將所有非ASCII轉為Unicode

### 目的

序列化時不自動將非ASCII轉為Unicode

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/172055165-99c69bf5-3937-45e6-bfe5-874312539df1.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 編輯WeatherForecastController檔案

將預設的API註解，寫入新的Action，預設不會引用System.Text.Json，記得在最上面using
![步驟4-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

```c#
    [HttpGet("JsonSerialize")]
    public ActionResult JsonSerialize() {
      var options = new JsonSerializerOptions {
        //美化輸出，會有空白字元
        WriteIndented = true,
        //將所有語言都不進行轉換
        Encoder = JavaScriptEncoder.Create(UnicodeRanges.All)
      };

      var Test = new TestClass() {
        Name = "中文名",
        Age = 18,
      };
      var Result = JsonSerializer.Serialize(Test, options);
      return Ok(Result);
    }

    public class TestClass {
      public string Name { get; set; }
      public int Age { get; set; }
    }
```

![步驟4-2](https://user-images.githubusercontent.com/19286751/179349354-20a678bc-a2ea-48fc-9c57-6f1937b41432.png)

### 執行結果

中文就不會是unicode了
![步驟5-1](https://user-images.githubusercontent.com/19286751/179349388-57f84637-6299-47e8-89cc-fa93d688af59.png)

### 參考

[How to serialize and deserialize](https://docs.microsoft.com/zh-tw/dotnet/standard/serialization/system-text-json-how-to?pivots=dotnet-6-0#how-to-write-net-objects-as-json-serialize)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/JsonExample_Advanced)