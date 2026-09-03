---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/DapperExample_Advanced
author: CI-YU
---

# .NET 6 Dapper語法說明

### 目的

說明Dapper基本語法

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/192102211-29c1dfe4-7e57-477d-85d9-8074d0f45f74.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Dapper
- Microsoft.Data.Sqlite
- ![步驟4](https://user-images.githubusercontent.com/19286751/192090481-8bee9294-2cd7-4026-b48a-f789e62809da.png)

### 編輯WeatherForecastController檔案

- 將預設的API註解
- ![步驟5-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)
- 基本設定

```C#
    /// <summary>
    /// 初始化SQLite
    /// </summary>
    /// <returns></returns>
    private static async Task InitSqliteAsync() {
      //建立SQLite連線
      using var conn = new SqliteConnection("Data Source=Student.sqlite");
      var SQL = new StringBuilder();
      //判斷是否有Student.sqlite檔案
      if (!System.IO.File.Exists(@".\Student.sqlite")) {
        //新增一張表，就會建立.sqlite檔案
        SQL.Append("CREATE TABLE Student( \n");
        SQL.Append("Id INTEGER PRIMARY KEY AUTOINCREMENT, \n");
        SQL.Append("Name VARCHAR(32) NOT NULL, \n");
        SQL.Append("Age INTEGER) \n");
        //執行sql語法
        await conn.ExecuteAsync(SQL.ToString());
      }
      //Task不建議使用void，當不需要回傳值時會改用Task.CompletedTask說明已經完成，可以下一個步驟了。
      await Task.CompletedTask;
    }
    public class Student {
      public int Id { get; set; }
      //Name預設值為Billhuang，與以前建構子的寫法一樣，如下方寫法
      //public Student(){Name="BillHuang";}
      public string Name { get; set; } = "BillHuang";
      public int Age { get; set; }
    }
```

![步驟5-2](https://user-images.githubusercontent.com/19286751/192135168-150b4c22-973a-41b8-bb93-937cb2a77bcf.png)

- 寫新的對外API：ExcuteAsync

```C#
    /// <summary>
    /// ExecuteAsync可用於insert、delete、update
    /// </summary>
    /// <returns></returns>
    [HttpGet("ExcuteAsync")]
    public async Task<IActionResult> ExcuteAsync() {
      //建立SQLite連線
      using var conn = new SqliteConnection("Data Source=Student.sqlite");
      var SQL = new StringBuilder();
      //初始化SQLite
      await InitSqliteAsync();
      SQL.Append("INSERT INTO Student (Name, Age) VALUES (@Name, @Age);");
      DynamicParameters parameters = new();
      parameters.Add("Name", "BillHuang");
      parameters.Add("Age", 20);
      var Result = await conn.ExecuteAsync(SQL.ToString(), parameters);
      return Ok(Result);
    }
```

![步驟5-3](https://user-images.githubusercontent.com/19286751/192135198-6f17caac-bbc2-4574-bbdf-e285b0b584de.png)

- 寫新的對外API：QueryAsync

```C#
    /// <summary>
    /// QueryAsync可用於select
    /// </summary>
    /// <returns></returns>
    [HttpGet("QueryAsync")]
    public async Task<IActionResult> QueryAsync() {
      //建立SQLite連線
      using var conn = new SqliteConnection("Data Source=Student.sqlite");
      var SQL = new StringBuilder();
      //初始化SQLite
      await InitSqliteAsync();
      SQL.Append("select * from Student");
      var Result = await conn.QueryAsync<Student>(SQL.ToString());
      return Ok(Result);
    }
```

![範例5-4](https://user-images.githubusercontent.com/19286751/192135210-5e66cc64-fe1a-4c60-ac2d-fd893f1b13d8.png)

- 寫新的對外API：QueryFirstOrDefaultAsync 取得第一筆的方法有四種，個人都是使用QueryFirstOrDefault，並判斷是否為null，如下列範例。

| 指令                 | 沒有值    | 有一個值 | 有多個值  |
| -------------------- | --------- | -------- | --------- |
| QueryFirst           | exception | V        | 取第一筆  |
| QuerySingle          | exception | V        | exception |
| QueryFirstOrDefault  | null      | V        | 取第一筆  |
| QuerySingleOrDefault | null      | V        | exception |

```C#
    /// <summary>
    /// 取得select第一筆
    /// </summary>
    /// <returns></returns>
    [HttpGet("QueryFirstOrDefaultAsync")]
    public async Task<IActionResult> QueryFirstOrDefaultAsync() {
      //建立SQLite連線
      using var conn = new SqliteConnection("Data Source=Student.sqlite");
      var SQL = new StringBuilder();
      //初始化SQLite
      await InitSqliteAsync();
      SQL.Append("select * from Student");
      var Result = await conn.QueryFirstOrDefaultAsync<Student>(SQL.ToString());
      if (Result is not null) {
        return Ok(Result);
      }
      return Ok(Result);
    }
```

![範例5-5](https://user-images.githubusercontent.com/19286751/192135225-ff1098fb-85e0-4a5e-bf55-26bb7113b6d6.png)

- 交易機制 當有多張表需要異動時，為了確認資料的一致性，會需要透過交易機制做保護，只有全部成功或全部失敗。

```C#
    /// <summary>
    /// 交易機制，簡單說就是全部成功才算成功，不然就全部取消。
    /// </summary>
    /// <returns></returns>
    [HttpGet("TransactionsAsync")]
    public async Task<IActionResult> TransactionsAsync() {
      using var conn = new SqliteConnection("Data Source=Student.sqlite");
      //開啟連線，前面沒有這行是因為在執行語法時(Execute、Query)會自動檢查是否連接資料庫
      conn.Open();
      //開始資料庫交易
      var trans = conn.BeginTransaction();
      var SQL = new StringBuilder();
      //初始化SQLite
      await InitSqliteAsync();
      SQL.Append("INSERT INTO Student (Name, Age) VALUES (@Name, @Age);");
      DynamicParameters parameters = new();
      parameters.Add("Name", "BillHuang");
      parameters.Add("Age", 20);
      //執行完並不會真的異動資料
      await conn.ExecuteAsync(SQL.ToString(), parameters, trans);
      SQL.Clear();
      SQL.Append("select * from Student");
      var Result = await conn.QueryFirstOrDefaultAsync<Student>(SQL.ToString(), trans);
      //當程式執行到Commit才是真的執行成功。
      trans.Commit();
      return Ok();
    }
```

![範例5-6](https://user-images.githubusercontent.com/19286751/192135248-578c710b-e3f4-430d-abb2-464a07d63a43.png)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/DapperExample_Advanced)