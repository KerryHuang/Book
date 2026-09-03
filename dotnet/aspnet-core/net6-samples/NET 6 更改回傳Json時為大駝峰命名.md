---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/JsonExample_Advanced_Deserialize
author: CI-YU
---

# .NET 6 更改回傳Json時為大駝峰命名

### 目的

將預設回傳的Camel-Case(temperatureCelsius)改為Pascal Case(TemperatureCelsius)

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/181061038-268ff840-a762-4c74-a4b2-5da34782b570.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### 編輯WeatherForecastController檔案

將預設的API註解，寫入新的Action，預設不會引用System.Text.Json，記得在最上面using
![步驟4-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

```c#
    /// <summary>
    /// 反序列化
    /// </summary>
    /// <returns></returns>
    [HttpGet("JsonDeserialize")]
    public ActionResult JsonDeserialize() {
      var options = new JsonSerializerOptions {
        PropertyNamingPolicy = null,
      };
      var jsonString = @"{""Name"":""中文名"",""Age"":18,""TemperatureCelsius"":52}";
      var Result = JsonSerializer.Deserialize<TestClass>(jsonString,options);
      return Ok(Result);
    }
    public class TestClass {
      public string Name { get; set; }
      public int Age { get; set; }
      public int TemperatureCelsius { get; set; }
    }
```

![步驟4-2](https://user-images.githubusercontent.com/19286751/181886521-af1b187b-fb27-4538-ba44-ce8005e3bb17.png)

### Program寫入程式

```c#
builder.Services.AddControllers()
    .AddJsonOptions(options => {
      //預設為小駝峰命名，將此參數改為null即可使用大駝峰命名
      options.JsonSerializerOptions.PropertyNamingPolicy = null;
    });
```

![步驟5-1](https://user-images.githubusercontent.com/19286751/181888145-a6c3bb3e-fcf1-4022-9e90-abafc59f32fd.png)

### 執行結果

![步驟6-1](https://user-images.githubusercontent.com/19286751/181894859-c32709a7-502c-49db-9cdb-e7f3c886e9fe.png)

### 參考

[大駝峰命名](https://www.dotblogs.com.tw/Null/2020/05/29/165723)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/JsonExample_Advanced_Deserialize)