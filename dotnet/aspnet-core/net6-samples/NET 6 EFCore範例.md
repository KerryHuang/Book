---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/EFCoreExample
author: CI-YU
---

# .NET 6 EFCore範例

### 目的

透過EFCore對db做查詢，為了降低門檻採用SQLite當範例資料庫。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/192133220-0a7e3474-6533-456e-a881-073c4e5bdbda.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Microsoft.EntityFrameworkCore.Sqlite
- Microsoft.EntityFrameworkCore.Design

![步驟4](https://user-images.githubusercontent.com/19286751/192144108-34319964-4189-4a43-bee1-90e81b90c2a7.png)

### 新增Student.cs類別檔

新增Models資料夾，並在裡面新增Student.cs類別檔
![範例5-1](https://user-images.githubusercontent.com/19286751/192144859-09e9bccf-1fc2-4895-b7a5-f0373e84ba01.png)

### 編輯Student.cs類別檔

```C#
  public class Student {
    public int Id { get; set; }
    public string Name { get; set; } = "BillHuang";
    public int Age { get; set; }
  }
```

![範例6-1](https://user-images.githubusercontent.com/19286751/192144999-5f4e9cd3-6e4d-4f43-ae85-b8c4b9433975.png)

### 新增EFCoreContext.cs類別檔

新增DBContext資料夾，並在裡面新增EFCoreContext.cs類別檔
![範例7-1](https://user-images.githubusercontent.com/19286751/193632519-763f6fff-33cd-45b5-862b-9f778c20baef.png)

### 編輯EFCoreContext.cs類別檔

```C#
//別忘了using
using Microsoft.EntityFrameworkCore;
using EFCoreExample.Models;

namespace EFCoreExample.DBContext {
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

![範例8-1](https://user-images.githubusercontent.com/19286751/192145087-b100e9d1-e901-4d61-90fe-e98aa148c70f.png)

### 編輯Program.cs檔

```C#
//別忘了using
using EFCoreExample.DBContext;

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

![範例9-1](https://user-images.githubusercontent.com/19286751/192145499-184ebbfb-9df9-4685-b3e0-2a6132af07d5.png)

### 到套件管理器主控台下Terminal指令

檢視>其他視窗>套件管理器主控台
![範例10-1](https://user-images.githubusercontent.com/19286751/192145927-dc54f669-8b83-4c01-9afa-f4ded0cdabc5.jpg)

下方會出現命令列
![範例10-2](https://user-images.githubusercontent.com/19286751/192146003-e32e32c5-7f9d-405d-9374-13a6aeea86d3.png)

輸入`dir`會顯示目錄檔案及子目錄清單
![範例10-3](https://user-images.githubusercontent.com/19286751/192146080-ecd9341b-51ac-471a-bc1d-8289b6a00672.png)

輸入`cd EFCoreExample`移動到專案檔底下後再輸入`dir`確認是否到正確路徑
![範例10-4](https://user-images.githubusercontent.com/19286751/192146188-4c0946b3-58bb-4fa4-a0af-b2fa8314acb9.png)

輸入`dotnet tool install --global dotnet-ef`在全域安裝EFCore CLI工具(如果已經安裝，會出現下圖訊息，即可忽略此步驟)
![範例10-5](https://user-images.githubusercontent.com/19286751/192146323-4bfd1b6b-a367-4eba-be7b-11850c755106.png)

輸入`dotnet ef migrations add CreateInitial`初始化SQLite
![範例10-6](https://user-images.githubusercontent.com/19286751/192146700-7375bbfb-d678-456c-b4f4-2f72ddb9afba.png)

輸入`dotnet ef database update`更新SQLite資料表
![範例10-7](https://user-images.githubusercontent.com/19286751/192147220-21ed77a4-1bd6-4db3-a52f-6c794ca9d922.png)

成功就會自動產生Migrations資料夾
![範例10-8](https://user-images.githubusercontent.com/19286751/192147306-983ea9b5-256f-4fce-a27f-caead7a9b757.png)

### 編輯WeatherForecastController.cs類別檔

將EFCoreContext注入WeatherForecastController.cs![步驟11-1](https://user-images.githubusercontent.com/19286751/192147618-10ee72b7-b36c-4772-94d4-bbd0423e9975.png)

- 將預設的API註解

![步驟11-2](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

- 寫新的對外API

```C#
    //
    [HttpGet("InsertAsync")]
    public async Task<IActionResult> InsertAsync() {
      //新增一筆資料
      var data = new Student() { Name = "BillHuang", Age = 20 };
      //加到Students這張table內
      _context.Students.Add(data);
      //執行，並回傳成功數量
      return Ok(await _context.SaveChangesAsync());
    }
```

![範例11-3](https://user-images.githubusercontent.com/19286751/192148162-4647d85e-0471-4dfe-8114-a54298cbe8ba.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果
![範例12-1](https://user-images.githubusercontent.com/19286751/192148343-65459327-6d94-47a1-a532-b73c4998e0ae.png)

![範例12-2](https://user-images.githubusercontent.com/19286751/192148388-98901307-9b0d-472f-9797-363c84b7e571.png)

![範例12-3](https://user-images.githubusercontent.com/19286751/192148422-1a0b7a3b-dce3-4f83-a7fd-8684bbdc294a.png)

### 參考

[efcore影片介紹](https://www.youtube.com/watch?v=Fbf_ua2t6v4) [余小章 @ 大內殿堂](https://dotblogs.com.tw/yc421206/2019/11/28/ef_core_migration)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/EFCoreExample)