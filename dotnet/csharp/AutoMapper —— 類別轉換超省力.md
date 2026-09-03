---
kind: reprint
source: site:igouist.github.io
author: igouist
---

# AutoMapper —— 類別轉換超省力

類別間的轉換幾乎是每個專案每個工程師都會碰到的動作，舉凡是分層架構每層之間的轉換，如 Dto 轉換成 ViewModel；或是接收到資料要塞進自定義的類別時也需要進行轉換。但在遠古時代，當我們要把一個類別的資料倒進另一個類別時，總免不了一番折騰。

例如一個卡片對戰遊戲的資料庫，光是要先把卡片資料讀取出來就需要：

![img](https://i.imgur.com/c81Hx5I.png)

有些時候也會看見用 Foreach 然後逐一傳值的場景，或是各種差不多的變種情況。同樣的是，光是將一個簡單的卡片資訊轉換成 ViewModel，就花了一大段在做對映的處理。這個過程本身枯燥乏味又占空間，更可怕的是，如果有個陳年資料表，動不動就上百個欄位，那這個轉換過程的恐怖程度可想而知。

幸好！天無絕人之路，這種時候就是本日的主角 —— AutoMapper 出場的時候了。

當 AutoMapper 一出手，轉換的過程瞬間就變成：

![img](https://i.imgur.com/KxHAKpi.png)

是不是精簡很多呢？接著就讓我們來看看怎麼開始使用吧！

## 安裝與使用

首先，當然要先到 NuGet 把 AutoMapper 給裝下來。

![img](https://i.imgur.com/TEAZwU7.png)

![img](https://i.imgur.com/3ADyJXv.png)

確認安裝之後，就開始基本的使用吧。

只需要先註冊好 Mapper 的設定內容，也就是哪些類別之間可以互相對映；再實體化 Mapper 出來使用就可以了。直接看程式碼應該就能理解：

```csharp
public IEnumerable<CardViewModel> GetCard()
{
    var data = this.GetCardFromRepositoryMock();
    
    var config = new MapperConfiguration(cfg => 
        cfg.CreateMap<Card, CardViewModel>()); // 註冊Model間的對映
    var mapper = config.CreateMapper(); // 建立 Mapper
    var result = mapper.Map<IEnumerable<CardViewModel>>(data); // 轉換型別

    return result;
}
```

沒錯，只需要簡簡單單幾步， AutoMapper 會自動將指定類別間同樣名稱的屬性內容做轉換 ，因此能夠省下相當多的功夫，也能夠隱藏類別本身的內容，專心在處理功能本身。

> 註：網路上挺多 AutoMapper 的文章會直接使用 `Mapper.CreateMap()` 這類靜態方法，然而這些方法已經在 AutoMapper 5 的時候被廢除，改成現在由 `MapperConfiguration` 產生 Mapper 的方法。
>
> 然而整體的使用方式仍然大同小異，這些文章仍能稍微調整並使用，惟使用過程中需自己注意語法的差異和多加測試。

### 客製化轉換

但當然實際上我們並不一定每個欄位的名稱都是一模一樣的，總是會有遇到同個資料在不同層的 Model 裡名稱不一樣的時候，又或者是某個欄位是由兩三個欄位組成的時候。對於這種需要客製化的轉換，這時候我們就可以在註冊對映時對欄位內容的對映方式做指定：

```csharp
var config = new MapperConfiguration(cfg =>
    cfg.CreateMap<Card, CardViewModel>()
        .ForMember(x => x.Id, y => y.MapFrom(o => o.CardId))
        .ForMember(x => x.Name, y => y.MapFrom(o => $"{o.Id}: {o.Name}"))
    ); // 註冊Model間的對映 建立設定檔
```

可以看到 我們能用 `ForMember` 去對類別成員做操作，並傳入目標的類別成員，以及該成員對應的操作，像這邊就使用 `MapFrom` 來指定目標類別成員的轉換來源，這樣就可以達到轉換時的客製化了。

> 註：對於欄位之間有使用 `ForMember` 來處理過內容再轉換的型別，建議在轉換型別時，也就是實際 mapper.Map() 的時候，稍做註解提醒一下。
>
> 尤其是會將 Mapper 的 Config 集中整理的架構裡更應該要對額外的操作做揭露，這樣對彼此都好。真的。

> 補充：AutoMapper 在轉換像是 `IEnumerable<T>` 這類的集合時，預設會將來源為 Null 的成員轉換成空集合（而非 Null）
>
> 如果希望 Null 就好好轉換成 Null 的朋友，可以在建立設定檔時用 `cfg.AllowNullCollections = true;` 來讓所有為 Null 的空集合轉換對象都乖乖保持 Null
>
> 也能夠在 ForMember 的時候使用 AllowNull 來針對欄位指定規則。例如 `ForMember(x => x.Members, y => y.AllowNull())`
>
> 需要更詳細說明的朋友，也可以參照官方文檔的 [Handling null collections](https://docs.automapper.org/en/stable/Lists-and-arrays.html#handling-null-collections) 一節

### 忽略指定的欄位

除了會有欄位名稱和來源的不同以外，最常遇到的應該就是兩個類別之間大多數欄位雖然對映，但某幾個欄位是沒有對映的。例如傳送給前端使用時一併送出其他來源的資料，但資料由資料表取出時並沒有這個欄位，必須轉換以後再呼叫別的方法去補上資料。如果直接使用 Map 來進行轉換，就會發生找不到對映欄位的錯誤。這時候就可以使用 `Ignore` 來忽略掉指定的欄位。

```csharp
var config = new MapperConfiguration(cfg =>
    cfg.CreateMap<Card, CardViewModel>()
       .ForMember(x => x.ImgUri, y => y.Ignore())
    );
```

如上述程式碼，可能卡片的圖像位置必須由別的方式取得，這種情況我們在 `ForMember` 的時候就可以將其指定為 `Ignore` 讓 AutoMapper 不要去嘗試轉換它。除了 `Ignore` 以外，AutoMapper 還有配備像是 `IgnoreAllPropertiesWithAnInaccessibleSetter` 這種光方法名稱長度就有點強的大殺器，也還有像是 `AllowNull` 等更多對欄位操作的方法，這部份請各位在使用時按照需求自行摸索。

> 註(1)：上述舉的例子中有需要從多個來源轉換為一個類別的場合，可以參照 [AutoMapper 兩個物件對映到一個類別 - mrkt 的程式學習筆記](https://kevintsengtw.blogspot.com/2014/03/automapper.html)

> 註(2)：上面使用到的 Ignore 方法還是有些眉角需要注意，可以參照 [[料理佳餚\] AutoMapper 中不容忽視的 Ignore() Mapping 的順序 - 軟體主廚的程式料理廚房](https://dotblogs.com.tw/supershowwei/2016/07/17/162815)

> 註(3)：面對一些比較複雜的轉換時，也可以考慮使用 [ConvertUsing](https://igouist.github.io/post/2021/12/automapper-convert-using/)

最後還要補充的一個方法是 `ReverseMap` ，它能夠反轉對映，建立一個反方向的對映表。當你的類別之間可能需要往回轉型，又或是想要忽略來源類別的欄位時，`ReverseMap` 就會顯得相當有用。通常為了避免轉來轉去轉出意外，建議註冊時還是補上一個 `ReverseMap` 為佳。

```csharp
var config = new MapperConfiguration(cfg =>
    cfg.CreateMap<Card, CardViewModel>()
       .ForMember(x => x.Id, y => y.MapFrom(o => o.CardId))
       .ForMember(x => x.ImgUri, y => y.Ignore())
       .ReverseMap() // 反轉
    );
```

到目前為止，程式碼可能會變成如下：

```csharp
public IEnumerable<CardViewModel> GetCard()
{
    var data = this.GetCardFromRepositoryMock();
    
    var config = new MapperConfiguration(cfg =>
        cfg.CreateMap<Card, CardViewModel>()
           .ForMember(x => x.Id, y => y.MapFrom(o => o.CardId))
           .ForMember(x => x.Name, y => y.MapFrom(o => $"{o.Id}: {o.Name}"))
           .ForMember(x => x.ImgUri, y => y.Ignore())
           .ReverseMap());

    var mapper = config.CreateMapper(); // 建立 Mapper
    var result = mapper.Map<IEnumerable<CardViewModel>>(data); // 轉換型別

    return result;
}
```

> (2021/6/9) 補充：
>
> 在我們前面提到的欄位轉換時，要特別注意兩個欄位的型別是否能夠對應上。由於 AutoMapper 會貼心地幫我們進行轉換，但有些時候可能會產生問題，讓我們看看下面這個例子：
>
> ```csharp
> public class Boo
> {
>     public double Val { get; set; }
> }
> 
> public class Foo
> {
>     public int Val { get; set; }
> }
> 
> public Foo Sut()
> {
>     var boo = new Boo
>     {
>         Val = 2.65
>     };
> 
>     var config = new MapperConfiguration(cfg =>
>         cfg.CreateMap<Boo, Foo>());
>     var mapper = config.CreateMapper();
>     
>     var foo = mapper.Map<Foo>(boo);
>     return foo; // 3
> }
> ```
>
> 可以看到上面這個例子中，我們可以把 `double` 的欄位直接 Mapping 到 `int` 的欄位上，因為 AutoMapper 的貼心，所以不會出錯，但過程中還是可能發生喪失精度的問題。
>
> 像是例子中的 2.65 就直接變成了 3，如果符合我們的需求（例如本來就打算轉型）倒是沒關係，但如果是因為不小心轉到的話，在找問題上可能就會比較麻煩。
>
> 因此在轉換的時候，還請特別留意一下轉換雙方的型別，測試一下轉換結果是不是自己要的結果會比較好呦。

## 簡化整理

可能看到這裡有些讀者就開始疑惑了：這好像跟一開始簡介不太一樣啊，詐欺？又或者是：我每個方法裡面都要重新建一個 Mapper？這不太對吧？

的確是這樣沒錯，AutoMapper 要達到更簡潔，還需要再做一些整理。例如使用 Profile 將對映關係集中起來，以及把 Mapper 的建構抽取出來。可能是在建構式建立共用的 Mapper ，或是以依賴注入 (Dependency Injection) 的方式來注入 Mapper 等等。以下就逐步進行介紹。

### Profile

首先我們先建立一個用來放對映關係的 Profile。我個人習慣會另開一個 Mappings 資料夾，並按照轉換所在的分層 + Mappings 來命名。

```csharp
public class ServiceMappings : Profile
{
    public ServiceMappings()
    {
        CreateMap<Card, CardViewModel>()
            .ForMember(x => x.Id, y => y.MapFrom(o => o.CardId))
            .ForMember(x => x.Name, y => y.MapFrom(o => $"{o.Id}: {o.Name}"))
            .ForMember(x => x.ImgUri, y => y.AllowNull())
            .ReverseMap(); 

        // ...其他的對映內容 (使用 CreateMap<> 建立下一組)
    }
}
```

從上面可以看到，我們繼承 AutoMapper 提供的 Profile 類，接著在建構式裡面將需要的轉換關係組都建立起來。接著當我們建立 Mapper 時，就可以直接用 `AddProfile` 和建立好的 Profile 來直接讀入對映關係：

```csharp
public IEnumerable<CardViewModel> GetCard()
{
    var data = this.GetCardFromRepositoryMock();
    var config = new MapperConfiguration(cfg => cfg.AddProfile<ServiceMappings>());
    var mapper = config.CreateMapper(); // 用設定檔建立 Mapper
    var result = mapper.Map<IEnumerable<CardViewModel>>(data); // 轉換型別

    return result;
}
```

當然，在 `MapperConfiguration` 的時候是可以對 cfg 去做多次 `AddProfile` 的，既然可以載入多組對映關係，就代表可以按照實務上的運用去將對映關係做分類和整理。

這邊還是要再度提醒一下，將 `CreateMap` 都整理到 Profile 之後，若是有些類別之間的轉換有對欄位做額外的處理，例如 DateTime 去除時間只留下年月日，又或是某幾個欄位銜接成一個欄位等等，在實際進行類別轉換的時候需要註記一下，請後續的維護人員或團隊夥伴記得先確認過 Profile，避免造成一些隱藏重要資訊挖洞給人跳的問題。

### 整理到建構式

接著由於一個處理資料或商業邏輯的部分通常會有許多方法都用到 Mapper，因此將建立 Mapper 的過程取出來避免重複絕對是必要的。故整理的第一步就是將 Mapper 的建立拆分出來，不再等每次用到的時候才建，而是先建立好一個 Mapper，需要的時候再來使用它。

這邊就先嘗試將其挪到私有變數和建構式處理：

```csharp
private IMapper _mapper;

public MapSimpleService() // 建構式
{
    var config = new MapperConfiguration(cfg => 
        cfg.AddProfile<ServiceMappings>());

    this._mapper = config.CreateMapper();
}
```

那麼我們實際上的方法就會變成：

```csharp
public IEnumerable<CardViewModel> GetCard()
{
    var data = this.GetCardFromRepositoryMock();
    var result = this._mapper.Map<IEnumerable<CardViewModel>>(data);
    return result;
}
```

### 走向注入

由於本篇篇幅無法說明好依賴注入（DI）的概念，相關的部份就留待在[之後的文章](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection)中說明，這邊就以 .net Core 為示範來記錄一下步驟，提供給已經會 DI 的朋友參考。

在開始之前，我們會需要再前往 NuGet 安裝 AutoMapper DI 用的套件：![img](https://i.imgur.com/hae1zfj.png)

接著在 `Startup.cs` 裡的 `ConfigureServices` 加上 `services.AddAutoMapper(typeof(Startup))` 來註冊我們的 Mapper：

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers(); 

    // Demo 用的 Service
    services.AddScoped<IMapSimpleService, MapSimpleService>();

    // 註冊 Mapper
    services.AddAutoMapper(typeof(Startup)); 
}
```

可能有些人會有點疑惑：前面還需要 `MapperConfiguration` 怎麼這次不用了呢？那是因為 `AddAutoMapper` 的時候就會用反射去取得同組件中的 `Profile` 來載入，所以這部分就可以不用擔心，只要專心在使用上就好。

> (2021/4/23) 補充：
>
> 感謝同事們的討論，這邊也補充給大家參考一下
>
> 當我們直接使用 `services.AddAutoMapper(typeof(Startup));` 註冊的時候，AutoMapper 會去抓我們 `typeof` 的型別，並對該型別所在的 Assembly 進行反射找出所有的 `Profile`。
>
> 但如果你有用到多層的架構、或是不同的組件內都有 `Profile` 需要註冊，又或者只是想要逐個 `Profile` 進行註冊，方便進行控管的話，可以考慮使用 `AddProfile` 或 `AddProfiles` 的方式來進行註冊，例如：
>
> ```csharp
> services.AddAutoMapper(config =>
> {
>     config.AddProfile<ControllerProfile>();
>     config.AddProfile<ServiceProfile>();
> });
> ```
>
> 這樣的可讀性更好，也能讓維護的人迅速掌握當前的 Profile，有需要的朋友可以嘗試看看。

> (2021/8/27) 補充：
>
> 感謝 [Ray](https://raychiutw.github.io/) 大大提供的方法，這邊也補充給大家參考一下
>
> 我們前面有提到 `AddAutoMapper` 會對該型別所在的 Assembly 進行反射找出所有的 `Profile`，那麼我們也可以轉換一下思路：只要把全部的組件都丟到 `AddAutoMapper` 裡就好了！這種時候我們就可以利用反射來達到我們的目的：
>
> ```csharp
> services.AddAutoMapper(AppDomain.CurrentDomain.GetAssemblies());
> ```
>
> 相較於 `AddProfile` 這種逐一新增 `Profile` 的作法，利用反射會讓註冊顯得更乾淨，並且也更不容易有所遺漏。各位可以按照開發的場景選擇一下註冊的方式，有需要的朋友也可以都嘗試看看。

註冊好之後，我們就能將剛剛的示範部分更改為使用注入的方式來取得 Mapper：

```csharp
private IMapper _mapper;

public MapSimpleService(IMapper mapper) // 建構式
{
    this._mapper = mapper;
}
```

執行之後就能確認確實有轉換到值囉！最後再來對照一下商業邏輯的部份：

－－瘦身前－－

```csharp
public IEnumerable<CardViewModel> GetCard()
{
    var data = this.GetCardFromRepositoryMock();
    var result = data.Select(x =>
        new CardViewModel
        {
            Id = x.Id,
            Name = x.Name,
            Cost = x.Cost,
            Attack = x.Attack,
            Health = x.Health,
            Note = x.Note // ...etc
        });
    return result;
}
```

－－瘦身後－－

```csharp
public IEnumerable<CardViewModel> GetCard()
{
    var data = this.GetCardFromRepositoryMock();
    var result = this._mapper.Map<IEnumerable<CardViewModel>>(data);
    return result;
}
```

## 結語

當我們把類別轉換的區段利用 AutoMapper 擷取出來，就能讓原本的程式碼更著重在該方法本身的邏輯和功能，而不會被冗長的轉換過程洗版，使用 Mapper 的方法只要知道這兩個類別能夠互相轉換即可。除了看起來更舒服、更能將焦點放在方法本身以外，也能夠讓維護時的修改更加直覺，若是轉換的過程需要修改，就去變更 Profile，不需要去變動實現商業邏輯的方法本身，這樣就能朝單一職責的目標更前進一點。

到這邊算是把 AutoMapper 基本的用法介紹過一遍了，當然還有很多進階的用法和需要注意的部分並沒有說明完全，但相信這樣的紀錄已經能夠幫助我在將來需要的時候回想起怎麼使用，和解決大部分需要做類別轉換的場景了。剩餘的延伸閱讀將會補充在參考資料裡，那麼下週見～

## 參考資料及延伸閱讀

- [[AutoMapper\] AutoMapper 5.0.2 的新寫法 - 余小章 @ 大內殿堂](https://dotblogs.com.tw/yc421206/2016/07/15/automapper_version_5_MapperConfiguration)
- [使用 AutoMapper 處理類別之間的對映轉換 - mrkt 的程式學習筆記](https://kevintsengtw.blogspot.com/2013/04/automapper.html)
- [AutoMapper 兩個物件對映到一個類別 - mrkt 的程式學習筆記](https://kevintsengtw.blogspot.com/2014/03/automapper.html)
- [AutoMapper 的設定 (Configuration) - mrkt 的程式學習筆記](https://kevintsengtw.blogspot.com/2013/04/automapper-configuration.html)
- [[C#.NET\] 使用 AutoMapper.Profile 簡化對應設定 - 余小章 @ 大內殿堂](https://dotblogs.com.tw/yc421206/2014/12/12/147619)
- [AutoMapper 介紹 - 簡單化Entity和ViewModel之間的轉換](https://ithelp.ithome.com.tw/articles/10157130)
- [AutoMapper 初體驗 - 中年大叔的鹹魚翻身作戰計畫](https://dotblogs.com.tw/keigen/2017/06/28/151917)
- [.NET Core 中依賴注入 AutoMapper 小記 - IT人](https://iter01.com/155318.html)
- [[料理佳餚\] AutoMapper 中不容忽視的 Ignore() Mapping 的順序 - 軟體主廚的程式料理廚房](https://dotblogs.com.tw/supershowwei/2016/07/17/162815)
- [AutoMapper 使用 ConvertUsing 自定義類型轉換，將包含串列成員的物件映射為一組串列](https://igouist.github.io/post/2021/12/automapper-convert-using/)

## 其他文章

- [Electron.net —— 把網頁包成桌面應用吧](https://igouist.github.io/post/2020/06/electron-net/)
- [C#: 位元旗標 (Bit flag) 與列舉](https://igouist.github.io/post/2020/06/bit-flags-and-enum/)
- [Visual studio 環境設定 —— 字型、套件、快捷鍵](https://igouist.github.io/post/2020/03/visualstudio/)
- [讀《黑馬思維》](https://igouist.github.io/post/2020/06/darkhorse/)
- [WakaTime —— 我 Coding 了多久？](https://igouist.github.io/post/2020/06/wakatime/)