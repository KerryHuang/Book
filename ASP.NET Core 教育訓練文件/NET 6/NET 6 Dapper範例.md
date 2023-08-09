# .NET 6 Dapper範例

### 目的

透過dapper對db做查詢，為了降低門檻採用SQLite當範例資料庫。

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/192088439-9c246a80-790b-4467-86e1-860fab1df133.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

- Dapper
- Microsoft.Data.Sqlite(微軟官方還是SQLite官方?
[黑暗執行緒](https://blog.darkthread.net/blog/sqlitepclraw-version/)

前輩有做說明，我的選擇比較單純有微軟用微軟)
![步驟4](https://user-images.githubusercontent.com/19286751/192090481-8bee9294-2cd7-4026-b48a-f789e62809da.png)

### 編輯WeatherForecastController檔案

- 將預設的API註解![步驟5-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)
- 寫新的對外API

```C#
    /// <summary>
    /// 檢查有沒有sqlite檔案，沒有就新增，並增加一筆資料
    /// </summary>
    /// <returns></returns>
    [HttpGet("InsertAsync")]
    public async Task<IActionResult> InsertAsync() {
      //連接sqlite資料庫
      using var connection = new SqliteConnection("Data Source=Student.sqlite");
      var SQL = new StringBuilder();
      //當找不到sqlite檔案時，建立新表，新表創建後就會產生sqlite檔案了
      if (System.IO.File.Exists(@".\Student.sqlite")) {
        //組語法，新建名為Student的表
        SQL.Append("CREATE TABLE Student( \n");
        //Id欄位設定數字型別為PKey，並且自動遞增
        SQL.Append("Id INTEGER PRIMARY KEY AUTOINCREMENT, \n");
        //Name欄位設定為VARCHAR(32)不允許是null
        SQL.Append("Name VARCHAR(32) NOT NULL, \n");
        //Age欄位設定為int
        SQL.Append("Age INTEGER) \n");
        //執行sql語法
        await connection.ExecuteAsync(SQL.ToString());
        //清除字串內的值
        SQL.Clear();
      }
      //組語法
      SQL.Append("INSERT INTO Student (Name, Age) VALUES (@Name, @Age);");
      //建立SQL參數化要使用的變數
      DynamicParameters parameters = new();
      //參數1
      parameters.Add("Name", "BillHuang");
      //參數2
      parameters.Add("Age", 20);
      //執行語法，insert一筆資料到Student
      var Result = await conn.ExecuteAsync(SQL.ToString(), parameters);
      //回傳執行成功的數量
      return Ok(Result);
    }
    /// <summary>
    /// 取得Student所有資料
    /// </summary>
    /// <returns></returns>
    [HttpGet("SelectAsync")]
    public async Task<IActionResult> SelectAsync() {
      //連接sqlite資料庫
      using var conn = new SqliteConnection("Data Source=Student.sqlite");
      var SQL = new StringBuilder();
      //組語法
      SQL.Append("select * from Student");
      //執行，並且將執行結果存為強型別
      var Result = await conn.QueryAsync<Student>(SQL.ToString());
      //回傳結果
      return Ok(Result);
    }
    public class Student {
      public int Id { get; set; }
      public string Name { get; set; } = "BillHuang";
      public int Age { get; set; }
    }
```

![範例5-1](https://user-images.githubusercontent.com/19286751/192134916-237b2766-f7ce-4c63-a07d-a53e3c2e54a9.png)![範例5-2](https://user-images.githubusercontent.com/19286751/192134945-c933a686-77e9-4a64-8f00-3e5981cd6aca.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果

- Insert
![範例6-1](https://user-images.githubusercontent.com/19286751/192099999-5019c63b-606d-4d31-b4e6-389b0f13ecea.png)

![範例6-2](https://user-images.githubusercontent.com/19286751/192100034-b8e4a43b-8168-4a0f-9359-842faf677b00.png)

![範例6-3](https://user-images.githubusercontent.com/19286751/192100058-7619d8bf-b863-45b5-9ab2-71bb38818522.png)

- Select
![範例6-4](https://user-images.githubusercontent.com/19286751/192100101-513510d6-bec4-423d-900a-e7b894b545f6.png)

![範例6-5](https://user-images.githubusercontent.com/19286751/192100122-9f41a917-1016-48c6-aa67-d21f6a0e68bb.png)

![範例6-6](https://user-images.githubusercontent.com/19286751/192100174-a7768122-5e55-4294-a8f1-abc319ca8981.png)

### 參考

[微軟官方還是SQLite官方](https://blog.darkthread.net/blog/sqlitepclraw-version/)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/DapperExample)