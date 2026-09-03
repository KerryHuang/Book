---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/JsonExample
author: CI-YU
---

# .NET 6 Text.Json範例

### 目的

不使用Newtonsoft.Json，改採.net6內建的System.Text.Json System.Text.Json更著重在效能與安全性，大多數人應該都跟我一樣只會使用基本的序列化及反序列化。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/172006764-a1038c9a-8db5-4b04-b817-cef185e2cdaf.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 編輯WeatherForecastController檔案

將預設的API註解，寫入新的Action，預設不會引用System.Text.Json，記得在最上面using
![步驟4-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

```c#
    /// <summary>
    /// 序列化
    /// </summary>
    /// <returns></returns>
    [HttpGet("JsonSerialize")]
    public ActionResult JsonSerialize() {
      var Test = new TestClass() {
        Name = "中文名",
        Age = 18
      };
      var Result = JsonSerializer.Serialize(Test);
      return Ok(Result);
    }
    /// <summary>
    /// 反序列化
    /// </summary>
    /// <returns></returns>
    [HttpGet("JsonDeserialize")]
    public ActionResult JsonDeserialize() {
      var jsonString = @"{""Name"":""中文名"",""Age"":18}";
      var Result = JsonSerializer.Deserialize<TestClass>(jsonString);
      return Ok(Result);
    }
    public class TestClass {
      public string Name { get; set; }
      public int Age { get; set; }
    }
```

![步驟4-2](https://user-images.githubusercontent.com/19286751/172038285-ddd3a6f6-460b-44de-8d39-629421cd9d0d.png)

### 執行結果

- 點選Try it out
![步驟5-1](https://user-images.githubusercontent.com/19286751/172039220-8847792f-e33a-4aab-b79d-574d11567ed6.png)

- 點選Execute
![步驟5-2](https://user-images.githubusercontent.com/19286751/172039284-62a16305-33a7-43d8-8686-3b52bc939ba5.png)

- 查看執行結果1(序列化)
![步驟5-3](https://user-images.githubusercontent.com/19286751/172039333-435db4dd-6521-4f1c-8840-1df89cea1aba.png)

- 查看執行結果2(反序列化)
![步驟5-4](https://user-images.githubusercontent.com/19286751/172039346-10b0d900-50bc-46ba-a435-0c9778b6e3ae.png)

### 延伸問題

在不做任何設定的情況下，內建的序列化會有些微差異

- 序列化預設會將所有非ASCII轉為Unicode代碼，例如：中文名=>\u4E2D\u6587\u540D

使用ActionResult中的JsonResult回傳時會將開頭改為小寫

- 反序列化後輸出為小寫的key(如結果2)，原先的TestClass是大寫的Name與Age

> 兩個問題都會在另一個章節補充說明

### 參考

[Compare Newtonsoft.Json to System.Text.Json, and migrate to System.Text.Json](https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-migrate-from-newtonsoft-how-to?pivots=dotnet-6-0)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/JsonExample)