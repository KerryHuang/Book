---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/BogusExample
author: CI-YU
---

# .NET 6 Bogus範例

### 目的

快速且簡單的製造假資料

### 建立新專案

選擇ASP.NET Core Web API專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/143255617-9964a993-becd-414b-aba2-632e99dd985d.png)

### 設定新的專案

![範例2](https://user-images.githubusercontent.com/19286751/183701560-5fe61436-28ec-4148-bec5-a44e328ce89a.png)

### 其他資訊

直接進行下一步
![步驟3](https://user-images.githubusercontent.com/19286751/148767425-ef0c8469-3d95-4f86-87ca-1c47c5cd0791.png)

### NuGet加入套件

透過NuGet安裝

1. Bogus

![範例4](https://user-images.githubusercontent.com/19286751/183705381-0650c8e8-dae2-4fd2-944d-a2dd8b2603c0.png)

### 編輯WeatherForecastController檔案

將預設的API註解
![步驟5-1](https://user-images.githubusercontent.com/19286751/154978191-e218edc4-5df3-49ad-9b7b-c4ddfa9fcdb1.png)

```c#
//除了using Bogus外，需注意需要using static Bogus.DataSets.Name，為了取得Gender
using static Bogus.DataSets.Name;
    [HttpGet("Test")]
    public List<User> Test() {
      //可限制隨機值為定值
      //Randomizer.Seed = new Random(8675307);
      //建立一個假的貨品陣列
      var fruit = new[] { "apple", "banana", "orange", "strawberry", "kiwi" };
      //預設訂單編號為0
      var orderIds = 0;
      //預設取得英文資料
      var testOrders = new Faker<Order>()
        //強制所有屬性都要有規則存在，預設為false
        .StrictMode(true)
        //OrderId is deterministic
        .RuleFor(o => o.OrderId, f => orderIds++)
        //從自訂陣列隨機取值
        .RuleFor(o => o.Item, f => f.PickRandom(fruit))
        //從1-10隨機取值
        .RuleFor(o => o.Quantity, f => f.Random.Number(1, 10))
        //從1-100隨機取值，並有20%機會為NULL
        .RuleFor(o => o.LotNumber, f => f.Random.Int(0, 100).OrNull(f, .2f));
      //預設使用者編號為0
      var userIds = 0;
      var testUsers = new Faker<User>()
        //使用需要初始化的類別
        .CustomInstantiator(f => new User(userIds++, f.Random.Replace("(##)###-####")))

        //從列舉中隨機取值(Gender為Bogus內建)
        .RuleFor(u => u.Gender, f => f.PickRandom<Gender>())

        //使用內建的生成器
        .RuleFor(u => u.FirstName, (f, u) => f.Name.FirstName(u.Gender))
        .RuleFor(u => u.LastName, (f, u) => f.Name.LastName(u.Gender))
        .RuleFor(u => u.Avatar, f => f.Internet.Avatar())
        .RuleFor(u => u.UserName, (f, u) => f.Internet.UserName(u.FirstName, u.LastName))
        .RuleFor(u => u.Email, (f, u) => f.Internet.Email(u.FirstName, u.LastName))
        .RuleFor(u => u.SomethingUnique, f => $"Value {f.UniqueIndex}")

        //可使用非Bogus的方法，建立一個新的GUID
        .RuleFor(u => u.CartId, f => Guid.NewGuid())
        //可使用複合屬性
        .RuleFor(u => u.FullName, (f, u) => $"{u.FirstName} {u.LastName}")
        //複雜的集合也可以使用，並重複產生5個訂單的陣列
        .RuleFor(u => u.Orders, f => testOrders.Generate(5).ToList())
        //最後結束後可以執行特定動作
        .FinishWith((f, u) =>
        {
          Console.WriteLine("User Created! Id={0}", u.Id);
        });
      //產生3個使用者
      var user = testUsers.Generate(3);
      return user;
    }
    public class User {
      public User(int v1, string v2) {
        Id = v1;
        SSN = v2;
      }
      public int Id { get; set; }
      public Gender Gender { get; set; }
      public string SSN { get; set; }
      public string FirstName { get; set; }
      public string LastName { get; set; }
      public string Avatar { get; set; }
      public string UserName { get; set; }
      public string Email { get; set; }
      public string SomethingUnique { get; set; }
      public Guid CartId { get; set; }
      public string FullName { get; set; }
      public List<Order> Orders { get; set; }
    }

    public class Order {
      public int OrderId { get; set; }
      public string Item { get; set; }
      public int Quantity { get; set; }
      public int? LotNumber { get; set; }
    }
```

![步驟5-2](https://user-images.githubusercontent.com/19286751/184668463-caa6878c-7f61-4d58-ba10-83e6dd5f04a7.png)

### 執行結果

F5執行後，依照下列步驟操作，並確認結果
![步驟6-1](https://user-images.githubusercontent.com/19286751/154981306-58a41739-acac-448d-851f-b7d3666999b1.png)

![步驟6-2](https://user-images.githubusercontent.com/19286751/154981450-28bd0211-3653-4b03-9ab3-877b060deb97.png)

![步驟6-3](https://user-images.githubusercontent.com/19286751/184669103-5e06bf22-cd80-4ccc-9a1c-173f903566bf.png)

### 參考

[kinanson的技術回憶](https://dotblogs.com.tw/kinanson/2017/04/27/083741) [參考](https://blog.myctw.cc/post/a1fe.html)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/BogusExample)