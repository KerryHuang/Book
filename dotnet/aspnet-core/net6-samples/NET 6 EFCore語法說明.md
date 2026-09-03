---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/EFCoreExample_Advanced
author: CI-YU
---

# .NET 6 EFCore語法說明

### 目的

說明EFCore基本語法，EFCore的基礎為Linq，所以使用上與Linq邏輯一模一樣，只是語法有些微差異。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/193629639-9162edb8-82dc-45d1-a257-b2815846e908.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Microsoft.EntityFrameworkCore.Sqlite
- Microsoft.EntityFrameworkCore.Design

![步驟4](https://user-images.githubusercontent.com/19286751/192144108-34319964-4189-4a43-bee1-90e81b90c2a7.png)

### 新增Student.cs類別檔

新增Models資料夾，並在裡面新增Student.cs類別檔
![範例5-1](https://user-images.githubusercontent.com/19286751/193629859-38197b6e-06c7-472c-ae76-2e1e7aeb92dc.png)

### 編輯Student.cs類別檔

```C#
  public class Student {
    public int Id { get; set; }
    public string Name { get; set; } = "BillHuang";
    public int Age { get; set; }
  }
```

![範例6-1](https://user-images.githubusercontent.com/19286751/193630104-ef3ac38e-0892-4aae-a106-366f773a05f7.png)

### 新增EFCoreContext.cs類別檔

新增DBContext資料夾，並在裡面新增EFCoreContext.cs類別檔
![範例7-1](https://user-images.githubusercontent.com/19286751/193630327-131beeb3-1717-4b8a-8d11-d21efc177739.png)

### 編輯EFCoreContext.cs類別檔

```C#
//別忘了using
using Microsoft.EntityFrameworkCore;
using EFCoreExample_Advanced.Models;

namespace EFCoreExample_Advanced.DBContext {
  //繼承DbContext
  public class EFCoreContext : DbContext {
    //複寫OnConfiguring
    protected override void OnConfiguring(DbContextOptionsBuilder options) {
      //指定連線字串，連到SQLite
      options.UseSqlite("Data Source=Student.sqlite");
    }
    //設定student資料表
    public DbSet<Student> Students { get; set; }
  }
}
```

![範例8-1](https://user-images.githubusercontent.com/19286751/193630503-ec3c9a5b-82c6-4237-82c4-a4bac166b61e.png)

### 編輯Program.cs檔

```C#
//別忘了using
using EFCoreExample_Advanced.DBContext;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
//註冊EFCoreContext
builder.Services.AddDbContext<EFCoreContext>();
//下面省略
```

![範例9-1](https://user-images.githubusercontent.com/19286751/193630503-ec3c9a5b-82c6-4237-82c4-a4bac166b61e.png)

### 到套件管理器主控台下Terminal指令

檢視>其他視窗>套件管理器主控台
![範例10-1](https://user-images.githubusercontent.com/19286751/193631711-6f9c077f-9af1-42d4-8db5-35122e4914fa.jpg)

下方會出現命令列
![範例10-2](https://user-images.githubusercontent.com/19286751/192146003-e32e32c5-7f9d-405d-9374-13a6aeea86d3.png

)輸入`dir`會顯示目錄檔案及子目錄清單
![範例10-3](https://user-images.githubusercontent.com/19286751/193631871-37a966a9-0713-4d21-a3f5-04d93c08559b.png)

輸入`cd EFCoreExample_Advanced`移動到專案檔底下後再輸入`dir`確認是否到正確路徑
![範例10-4](https://user-images.githubusercontent.com/19286751/192146188-4c0946b3-58bb-4fa4-a0af-b2fa8314acb9.png)

輸入`dotnet tool install --global dotnet-ef`在全域安裝EFCore CLI工具(如果已經安裝，會出現下圖訊息，即可忽略此步驟)
![範例10-5](https://user-images.githubusercontent.com/19286751/192146323-4bfd1b6b-a367-4eba-be7b-11850c755106.png)

輸入`dotnet ef migrations add CreateInitial`初始化SQLite
![範例10-6](https://user-images.githubusercontent.com/19286751/192146700-7375bbfb-d678-456c-b4f4-2f72ddb9afba.png)

輸入`dotnet ef database update`更新SQLite資料表
![範例10-7](https://user-images.githubusercontent.com/19286751/192147220-21ed77a4-1bd6-4db3-a52f-6c794ca9d922.png)

成功就會自動產生Migrations資料夾
![範例10-8](https://user-images.githubusercontent.com/19286751/193632147-f524d84b-fe04-44f3-8e6d-da6af6d9214a.png)

### 編輯WeatherForecastController檔案編輯

- 寫新的對外API：QueryAsync

```C#
    [HttpGet("QueryAsync")]
    public async Task<IActionResult> QueryAsync() {
      //透過ToListAsync方法就可以將Students所有資料取出
      var Result = await _context.Students.ToListAsync();
      return Ok(Result);
    }
```

![步驟11-1](https://user-images.githubusercontent.com/19286751/192151372-c0f2c266-703f-4d83-b238-48f0969676af.png)

- 寫新的對外API：QueryFirstOrDefaultAsync

```C#
    [HttpGet("QueryFirstOrDefaultAsync")]
    public async Task<IActionResult> QueryFirstOrDefaultAsync() {
      //取得第一筆
      var Result = await _context.Students.FirstOrDefaultAsync();
      return Ok(Result);
    }
```

![步驟11-2](https://user-images.githubusercontent.com/19286751/192151404-c390296b-1474-4aa7-abe1-6c4c1d08551f.png)

- 交易機制 當有多張表需要異動時，為了確認資料的一致性，會需要透過交易機制做保護，只有全部成功或全部失敗。

```C#
    [HttpGet("TransactionsAsync")]
    public async Task<IActionResult> TransactionsAsync() {
      //開始資料庫交易
      using var trans = _context.Database.BeginTransaction();
      //建立一筆資料
      var data = new Student() { Name = "BillHuang", Age = 20 };
      //新增到Students資料表中
      _context.Students.Add(data);
      //執行，此步驟還不會真的異動到資料
      await _context.SaveChangesAsync();
      //取得第一筆資料
      var Result = await _context.Students.FirstOrDefaultAsync();
      //當執行了Commit後才會將上面的異動存到資料庫
      trans.Commit();
      return Ok(Result);
    }
```

![步驟11-3](https://user-images.githubusercontent.com/19286751/192151427-e16d7151-50bb-4e87-8640-8ec58190e915.png)

### 參考

[N+1](https://stackoverflow.com/questions/97197/what-is-the-n1-selects-problem-in-orm-object-relational-mapping) [交易](https://learn.microsoft.com/zh-tw/ef/core/saving/transactions)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/EFCoreExample_Advanced)