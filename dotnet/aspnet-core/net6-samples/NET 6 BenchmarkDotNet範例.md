---
kind: reprint
source: https://github.com/CI-YU/2022-ITHelp/tree/main/BenchmarkDotNetExample
author: CI-YU
---

# .NET 6 BenchmarkDotNet範例

### 目的

快速測試不同寫法的效能差異。

### 建立新專案

選擇主控台應用程式專案範本，並執行下一步
![步驟1](https://user-images.githubusercontent.com/19286751/153220010-7e3ee13e-2a81-4f8f-8b28-2688595c18b2.png)

### 設定新的專案

命名你的專案名稱，並選擇專案要存放的位置。
![步驟2](https://user-images.githubusercontent.com/19286751/153220400-47efdb22-c8cc-4670-80a5-845d3cc7e7b1.png)

### 其他資訊

直接進行下一步

### NuGet加入套件

下載BenchmarkDotNet套件與automapper套件，automapper為這次要測試效能的套件
![步驟4-1](https://user-images.githubusercontent.com/19286751/153220898-2cfa2a2a-9909-4812-bf7c-e3cc1f510bc4.png)

![步驟4-2](https://user-images.githubusercontent.com/19286751/153221310-8dfef6c0-fa33-4c86-85c1-b88f69df4740.png)

### Program寫入程式

此次要測試的項目為三種類別轉換的效能差異

```c#
using AutoMapper;
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;
//指定要測試的class
var summary = BenchmarkRunner.Run<BenchmarkSampleAuto>();
//加入記憶體使用量測試
[MemoryDiagnoser]
public class BenchmarkSampleAuto {

  private readonly List<DbModel> _data = new List<DbModel>();
  private readonly IMapper _mapper;
  public BenchmarkSampleAuto() {
    //automapper設定
    var config = new MapperConfiguration(cfg => {
      cfg.CreateMap<DbModel, ViewModel>();
    });
    _mapper = new Mapper(config);
    //準備一份List資料
    PrepareTestObjects();
  }
  private void PrepareTestObjects() {
    _data.Add(new DbModel() { Id = 1, Name = "Bill", Age = 18, CreatedDate = DateTime.Now });
    _data.Add(new DbModel() { Id = 1, Name = "CI-YU", Age = 20, CreatedDate = DateTime.Now });
    _data.Add(new DbModel() { Id = 1, Name = "Bill Huang", Age = 22, CreatedDate = DateTime.Now });
  }
  //待測方法需要加上Benchmark屬性
  [Benchmark]
  public List<ViewModel> first() {
    return _mapper.Map<List<ViewModel>>(_data);
  }
  //待測方法需要加上Benchmark屬性
  [Benchmark]
  public List<ViewModel> second() {
    var listModel = new List<ViewModel>();
    foreach (var c in _data) {
      listModel.Add(new ViewModel() { Id = c.Id, Name = c.Name, Age = c.Age });
    }
    return listModel;
  }
  //待測方法需要加上Benchmark屬性
  [Benchmark]
  public List<ViewModel> third() {
    var listModel = new List<ViewModel>();
    listModel = _data.Select(c => new ViewModel() { Id = c.Id, Name = c.Name, Age = c.Age }).ToList();
    return listModel;
  }
}

public class DbModel {
  public int Id { get; set; }
  public string? Name { get; set; }
  public int Age { get; set; }
  public DateTime CreatedDate { get; set; }
}
public class ViewModel {
  public ViewModel() {
    Name = string.Empty;
  }
  public int Id { get; set; }
  public string Name { get; set; }
  public int Age { get; set; }
}
```

### 執行測試

> 執行測試前需要將組態改為**Release**才可以進行測試

![步驟6](https://user-images.githubusercontent.com/19286751/153224098-f7f62b1d-9242-4e7a-9a7c-d8899c9bb9f9.png)

### 執行結果

最後的執行結果發現第二種方法的效能是最好的，通常最主要是看mean及allocated兩個參數

- Mean 平均時間
- Allocated 記憶體使用量
![步驟7](https://user-images.githubusercontent.com/19286751/153223898-3652c8da-09e0-4d84-b5ea-8e55cc0ca2fc.png)

### 補充

在專案資料夾**bin\Release\net6.0\BenchmarkDotNet.Artifacts\results**底下會有詳細的報告，檔案格式有csv,html,md

### 參考資料

[參考](https://blog.kkbruce.net/2017/01/donot-use-for-use-benchmark-dotnet.html#.YgKM_d9Bz32) [伊果的沒人看筆記本](https://igouist.github.io/post/2021/06/benchmarkdotnet/)

### 範例檔

[GitHub](https://github.com/CI-YU/2022-ITHelp/tree/main/BenchmarkDotNetExample)