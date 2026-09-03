---
kind: original
---

# CORS

在 .NET 8 中，CORS 設定變得更加簡潔，可以直接在 `AddCors` 方法中定義 CORS 策略，而不需要像以前一樣通過委派進行設定。以下是將您的 CORS 設定改為 .NET 8 風格的寫法。

### 更新後的 CORS 設定

```csharp
var builder = WebApplication.CreateBuilder(args);

// 新增 CORS 設定
builder.Services.AddCors(options =>
{
    options.AddPolicy("Dev", policy =>
        policy.WithOrigins(
                "http://localhost:8082",
                "http://localhost:8081",
                "https://localhost:8080",
                "http://localhost:9000",
                "http://localhost:8080",
                "http://192.168.8.113:8080")
            .AllowAnyHeader()
            .AllowCredentials()
            .WithMethods("GET", "POST", "PUT", "DELETE"));
});

var app = builder.Build();

// 使用 CORS 策略
app.UseCors("Dev");

app.MapGet("/", () => "Hello World!");

app.Run();
```

### 說明

- **`AddCors` 設定**：CORS 策略現在可以直接在 `AddPolicy` 中定義，這樣設定更清晰，並符合 .NET 8 的簡潔風格。
- **`UseCors` 中指定策略**：使用 `app.UseCors("Dev")` 來啟用指定的策略，這樣可確保每個請求都應用該 CORS 設定。

此設定方式在 .NET 8 中更加直觀，並且保持原本的彈性，可以更簡潔地設定多個來源及允許的方法和標頭等規則。