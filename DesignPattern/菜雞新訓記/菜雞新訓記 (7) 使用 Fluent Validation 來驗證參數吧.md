# 菜雞新訓記 (7): 使用 Fluent Validation 來驗證參數吧



![Image](https://i.imgur.com/p6aSDH9.png)

這是俺整理公司新訓內容的第七篇文章，目標是紀錄 Fluent Validation 這個好用套件。

FluentValidation 可以幫我們將 Api 傳入的參數的檢查用更口語、更乾淨的方式去處理，除了可以將檢查邏輯拆分成單獨的 Validator 類別，更提供了許多內建的檢查規則和自訂的彈性，相當方便。

並且因為將參數的檢查邏輯整理出去，就可以和 Controller 本身的工作做簡單的拆分，達到關注點分離的目標。

現在就讓我們來認識一下這個好用工具吧！首先要從很久很久以前開始說起…

## 前言

西元前的某一天，憂心的皇帝在朝堂內繞著柱子走，突然大臣奪門而入。

大臣：「陛下！敵軍已經攻到國境內啦！」

皇帝大驚：『邊境的那些檢查站和關口難道都陷落了嗎？不可能！』

大臣：「陛下，有內奸和敵國勾結，檢查站完全沒檢查！髒資料已經闖進來了！」

皇帝喊了一聲：『怎麼可能！讓朕看看！』就打開 Controller 和前一個版本的 Git Log，這一看差點就昏了過去。

原來 Controller 的舊程式碼就已經很亂了，檢查參數的條件 if/else 和其他呼叫的方法、組裝資料都雜在一起。結果這次專案改動時，某一行就被內奸改壞了，關鍵的參數竟然沒檢查到！

『可，可惡！來人啊，把工程師推出午門斬首！』

「皇上！他已經離職啦！」

皇帝跌坐在地，懊悔地說：『如果當初有好好把檢查參數跟實際組資料的部份都拆開的話，也許就不會這樣了…』

「是啊，如果我們有用 Fluent Validation…！」

## 專案現況

大臣提到的 [FluentValidation](https://fluentvalidation.net/) 是一套能幫我們把傳入參數的分離出去、用更口語化的方式去撰寫的工具。

……如果當時他們有使用 Fluent Validation 來把驗證的邏輯和規則跟原本很亂的 Controller 切分的話，說不定就能及時發現問題吧，大概。

為了不要步上他們的後塵，就讓我們直接回到本系列的卡牌管理 API 服務來加上這個好用工具吧！

假設我們在新增一張新的卡牌時，會針對裡面的欄位做一連串檢查：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert([FromBody] CardParameter parameter)
{
    // 這邊需要對參數做檢查
    if (parameter.Attack < 0)
    {
        return BadRequest("卡片的攻擊力不可為負數");
    }

    if (parameter.Health < 0)
    {
        return BadRequest("卡片的生命值不可為負數");
    }

    if (parameter.Cost < 0)
    {
        return BadRequest("卡片的使用成本不可為負數");
    }

    if (parameter.Description != null &&
        parameter.Description.Length > 30)
    {
        return BadRequest("卡片的敘述說明必須少於三十字");
    }

    if (string.IsNullOrWhiteSpace(parameter.Name))
    {
        return BadRequest("卡片的名稱不可為空白");
    }

    if (parameter.Name.Length > 15)
    {
        return BadRequest("卡片的名稱必須少於十五字");
    }

    // 用 AutoMapper 把 Parameter Model 轉換成 Info Model
    var info = this._mapper.Map<CardParameter, CardInfo>(parameter);

    // 呼叫依賴的 Service 層寫入資料
    var isInsertSuccess = this._cardService.Insert(info);
    if (isInsertSuccess)
    {
        return Ok();
    }
    return StatusCode(500);
}
```

可以看到這個新增卡片的方法中，真正操作的只有最後呼叫相關服務來寫入資料的部份，前面就是針對參數做一整串的 if 檢查。隨著傳入參數要檢查的東西變多，檢查的過程也會越來越大坨。

這時候，只要有了 Fluent Validation，我們就可以在參數檢查上做得更好！

## 安裝 Fluent Validation

因為我們的示範專案是 .net Core 的 Api，所以讓我們安裝 FluentValidation.AspNetCore

![img](https://i.imgur.com/5ubV1VG.png)

> 註：這包裡面包含了 Fluent Validation 本體和支援 Dotnet Core 的 DI（DependencyInjection）工具。如果習慣將驗證部分拆成其他類別庫，或是不需要 DI 的朋友可以嘗試安裝 Fluent Validation 就好。

## 撰寫 Validator

要使用 Fluent Validation 來驗證參數，首先我們必須建立一個針對該參數的驗證器（Validator），並繼承 `AbstractValidator<T>`。

其中 `<T>` 的泛型選擇驗證對象的類別即可，接著就可以在 Validator 的建構式來註冊我們要的驗證邏輯。

現在就讓我們針對前面例子的 `CardParameter` 來建立 `CardParameterValidator` 吧：

![img](https://i.imgur.com/BWDZX6R.png)

```csharp
/// <summary>
/// Card Parameter 的驗證器
/// </summary>
public class CardParameterValidator : AbstractValidator<CardParameter>
{
    /// <summary>
    /// 驗證器的建構式: 在這裡註冊我們要驗證的規則
    /// </summary>
    public CardParameterValidator()
    {

    }
}
```

### 使用內建的驗證規則

現在我們已經針對 `CardParameter` 建立了驗證器，接著讓我們處理驗證邏輯的部分吧。

當我們要驗證某個欄位的時候，就需要使用 `RuleFor` 來告訴驗證器現在驗證的欄位，後面再利用 Fluent Validation 提供的各種驗證語法來進行驗證。

例如我們前面的「卡片的攻擊力不應為負數」，也就是 Attack 必須大於等於０，這邊就可以使用 `GreaterThanOrEqualTo`：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleFor(card => card.Attack)
        .GreaterThanOrEqualTo(0);
}
```

如果驗證的對象是個串列之類的，也支援用 `RuleForEach`

例如我們的卡片可以有多個別名（`List<string> Alias` 之類的），且裡面每個別名都不可以是空的，就可以：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleForEach(card => card.Alias)
        .NotEmpty(); // 不可為空
}
```

大部份的狀況下，使用內建的驗證語法就很夠用了。可以參照官方文檔的 [Built-in Validators](https://docs.fluentvalidation.net/en/latest/built-in-validators.html#built-in-validators)，裡面每一項都有範例和參數說明。

平常比較會遇到的就是 `NotNull`、`NotEmpty` 和字串長度檢查或是數值大小的。如果是ㄧ些表單需要驗證的話，就還會用到 `EmailAddress` 等等。

那俺身為一個 ~~懶惰~~ 節能減碳工程師，當然有在 Linqpad 中準備一份範例 ~~才能隨時抄嘛~~，這邊也會附在文末的[附錄](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation/#附錄fluentValidation-內建驗證方法-小抄)。

### 使用 Must 來自訂驗證規則

當然，我們也會遇到內建的驗證規則不夠用的情況。這時候就可以使用 `Must()` 來傳入自訂的規則，例如：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    // 使用 Must 來自訂規則
    this.RuleFor(card => card.Attack)
        .Must(attack => attack > 0 && attack <= 3000);
}
```

只要在 `Must` 裡面指定要驗證的規則就可以囉！

### 使用 When 來指定驗證條件適用的場景

除了規則可以彈性處理以外，有時候我們也會遇到「有某個條件成立才驗證指定欄位」的情況

假設我們的卡牌又分成「怪獸卡」和「魔法卡」等等，而卡牌本身又有個 int? 的攻擊力欄位

規則又要求：「怪獸卡必須是具有攻擊力的」

雖然直覺上就會想要用 `if (卡牌是怪獸卡)` 之類的方式去另外做，但就會變得有點兒醜

這時候我們就能用 `When` 的方式來指定驗證條件的前提：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    // 目標：當 卡牌 是 怪獸卡 的時候，攻擊力不可為 Null 

    // 針對指定規則加上適用場景
    this.RuleFor(card => card.Attack)
        .NotNull()
        .When(card => card.CardType is CardType.Monster);

    // 針對指定場景加上適用規則，我個人比較喜歡這種
    this.When(card => card.CardType is CardType.Monster, () =>
    {
        this.RuleFor(card => card.Attack).NotNull();
    });

    // 以上兩種寫法是相同的，但我個人比較喜歡先 When 才指定規則
    // 除了比較符合日常口語以外，也能把同樣場景的規則整理在一起
}
```

就像 if 有 else，這邊的 When 也有 Otherwise 來幫忙處理剩下的狀況

假設我們除了怪獸卡以外的卡片，例如魔法卡之類的，都不應該有攻擊力，就可以這樣寫：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    // 目標：當 卡牌 是 怪獸卡 的時候，攻擊力不可為 Null
    // 目標：當 卡牌 不是 怪獸卡 的時候，攻擊力必須為 Null

    this.When(card => card.CardType is CardType.Monster, () =>
    {
        this.RuleFor(card => card.Attack).NotNull();
    })
    .Otherwise(() =>
    {
        this.RuleFor(card => card.Attack).Null();
    });
}
```

### 使用 WithName 和 WithMessage 來自訂驗證訊息

雖然內建的驗證規則都有提供制式的回傳訊息，例如對 Attack 做 `.GreaterThanOrEqualTo(0)` 驗證失敗時，會得到「‘Attack’ 必須大於或等於 ‘0’」的訊息

![Image](https://i.imgur.com/KIEDyhI.png)

但我們也可以使用 `WithMessage` 來針對驗證規則指定失敗時的自訂訊息：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleFor(card => card.Attack)
        .GreaterThanOrEqualTo(0)
        .WithMessage("卡片的攻擊力不可為負數");
}
```

這樣在驗證完的 ValidationResult 裡，就會變成我們指定了錯誤訊息了。

那如果我們想用內建的訊息，但又希望「Attack」這個欄位名稱不要顯示出來，而是顯示我們要的「攻擊力」這個名稱呢？這時候就可以使用 `WithName()`：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleFor(card => card.Attack)
        .GreaterThanOrEqualTo(0)
        .WithName("攻擊力");
}
```

這樣原本的「‘Attack’ 必須大於或等於 ‘0’」，就會變成「‘攻擊力’ 必須大於或等於 ‘0’」囉！

當然，要把兩個結合起來用也是可以的，只要在字串加上 `{PropertyName}` 讓他去讀欄位名稱就好囉：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleFor(card => card.Attack)
        .GreaterThanOrEqualTo(0)
        .WithName("攻擊力")
        .WithMessage("卡片的{PropertyName}不可為負數");
}
```

這樣就能拿到「卡片的攻擊力不可為負數」囉！

### 使用 SetValidator 來指定成員的驗證器

我們前面說了許多針對欄位驗證的工具，但平常我們的類別內的成員有可能會是另一個類別。這時候我們就可以用 `SetValidator` 來指定該成員的驗證器。

假設說我們的卡片怪獸現在能夠穿戴裝備了，同時我們也有裝備的 Validator：

```csharp
public class Card
{
	public CardType Type { get; set; }
	public int Cost { get; set; }
	public string Name { get; set; }
	public int Attack { get; set; }
	
	public Equipment Equipment { get; set;} // 可以穿裝備了！
}

public class Equipment { }
public class EquipmentValidator : AbstractValidator<Card> { }
```

這時候我們在寫規則的時候就可以：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleFor(card => card.Equipment)
        .SetValidator(new EquipmentValidator());
}
```

### 指定 CascadeMode.Stop 來提早返回

很多時候，我們並不需要全部的規則都驗證完才返回，而是只要檢查清單中的一項不符合，那就直接掰掰。這時我們就可以更改驗證器的 `CascadeMode`：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    // 驗證失敗時即停止
    this.CascadeMode = FluentValidation.CascadeMode.Stop;

    this.RuleFor(card => card.Attack)
        .GreaterThanOrEqualTo(0);
}
```

CascadeMode 原先預設會是 `Continue`，也就是即使驗證失敗也會繼續執行

例如說它可能一口氣犯了好幾條，就會全部驗證完再一併列出所有驗證失敗的項目：

![Image](https://i.imgur.com/ngLOMaE.png)

當我們把驗證器的 CascadeMode 指定為 `Stop` 之後，犯第一條就會直接原地遣返：

![Image](https://i.imgur.com/deSUlPf.png)

除了指定整個驗證器以外，我們也可以單獨指定某一條規則為天條：

```csharp
/// <summary>
/// 驗證器建構式: 在這裡註冊我們要驗證的規則
/// </summary>
public CardParameterValidator()
{
    this.RuleFor(card => card.Attack)
        .Cascade(CascadeMode.Stop)
        .GreaterThanOrEqualTo(0);
}
```

如此一來只要觸犯這條就會直接送客，皆大歡喜。

### 將前述的規則實作成 Validator

前面我們介紹了如何撰寫一個 Validator，是時候讓我們來處理文章最一開始的範例了！

這邊附一下文章開頭的範例，也就是目前的卡牌系統 Controller 裡的新增卡片方法：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert([FromBody] CardParameter parameter)
{
    // 一堆檢查
    if (parameter.Attack < 0)
    {
        return BadRequest("卡片的攻擊力不可為負數");
    }

    if (parameter.Health < 0)
    {
        return BadRequest("卡片的生命值不可為負數");
    }

    if (parameter.Cost < 0)
    {
        return BadRequest("卡片的使用成本不可為負數");
    }

    if (parameter.Description != null &&
        parameter.Description.Length > 30)
    {
        return BadRequest("卡片的敘述說明必須少於三十字");
    }

    if (string.IsNullOrWhiteSpace(parameter.Name))
    {
        return BadRequest("卡片的名稱不可為空白");
    }

    if (parameter.Name.Length > 15)
    {
        return BadRequest("卡片的名稱必須少於十五字");
    }

    // 用 AutoMapper 把 Parameter Model 轉換成 Info Model
    var info = this._mapper.Map<CardParameter, CardInfo>(parameter);

    // 呼叫依賴的 Service 層寫入資料
    var isInsertSuccess = this._cardService.Insert(info);
    if (isInsertSuccess)
    {
        return Ok();
    }
    return StatusCode(500);
}
```

可以看到在範例中，我們針對一張新的卡牌，需要檢查的項目有：

- 攻擊力不可為負數
- 生命值不可為負數
- 使用成本不可為負數
- 敘述說明必須少於三十字
- 名稱不可以為空值
- 名稱必須少於十五字

現在讓我們建立 CardParameter 的 Validator，並用 RuleFor 加上這些規則吧：

```csharp
/// <summary>
/// Card Parameter 的驗證器
/// </summary>
public class CardParameterValidator : AbstractValidator<CardParameter>
{
    /// <summary>
    /// 驗證器的建構式: 在這裡註冊我們要驗證的規則
    /// </summary>
    public CardParameterValidator()
    {
        this.RuleFor(card => card.Attack)
            .GreaterThanOrEqualTo(0);

        this.RuleFor(card => card.Health)
            .GreaterThanOrEqualTo(0);

        this.RuleFor(card => card.Cost)
            .GreaterThanOrEqualTo(0);

        this.RuleFor(card => card.Description)
            .NotNull()
            .MaximumLength(30);

        this.RuleFor(card => card.Name)
            .NotEmpty()
            .MaximumLength(15);
    }
}
```

可以感覺到比起整串 if/else，這邊整理得更加簡短、也更加口語了。

## 使用 Validator 進行驗證

現在我們已經準備好了 Validator 了，讓我們回到原本的 Controller 來使用它吧！

首先讓我們把原本的 if/else 部分移除：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert(
    [FromBody] CardParameter parameter)
{
    // 這邊需要對參數做檢查

    // 用 AutoMapper 轉換 Model
    var info = this._mapper.Map<CardParameter,CardInfo>(parameter);

    // 呼叫 Service 層寫入資料
    var isInsertSuccess = this._cardService.Insert(info);
    if (isInsertSuccess)
    {
        return Ok();
    }
    return StatusCode(500);
}
```

接著讓我們直接建立一個驗證器出來使用，並且用 `Validate` 來驗證參數：

```csharp
var validator = new CardParameterValidator();
var validationResult = validator.Validate(parameter);
```

加上驗證器的樣子是像這樣的：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert(
    [FromBody] CardParameter parameter)
{
    // 這邊需要對參數做檢查
    var validator = new CardParameterValidator();
    var validationResult = validator.Validate(parameter);

    // 用 AutoMapper 把 Parameter Model 轉換成 Info Model
    var info = this._mapper.Map<CardParameter, CardInfo>(parameter);

    // 呼叫依賴的 Service 層寫入資料
    var isInsertSuccess = this._cardService.Insert(info);
    if (isInsertSuccess)
    {
        return Ok();
    }
    return StatusCode(500);
}
```

接著我們就可以使用 `Validate` 回傳的 `ValidationResult` 來看驗證結果。

先讓我們用 Linqpad 的小範例把 `ValidationResult` 的內容印出來看看：

![Image](https://i.imgur.com/UcBHhci.png)

可以看到，`IsValid` 會告訴我們是不是有通過驗證。如果沒有通過驗證的話，`Errors` 就會有驗證失敗的內容。

現在讓我們加上驗證結果的檢查吧：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert(
    [FromBody] CardParameter parameter)
{
    // 這邊需要對參數做檢查
    var validator = new CardParameterValidator();
    var validationResult = validator.Validate(parameter);

    // 如果沒有通過檢查，就把訊息串一串丟回去
    if (validationResult.IsValid is false)
    {
        var errorMessages = validationResult.Errors.Select(e => e.ErrorMessage);
        var resultMessage = string.Join(",", errorMessages);
        return BadRequest(resultMessage); // 直接回傳 400 + 錯誤訊息
    }

    // 用 AutoMapper 把 Parameter Model 轉換成 Info Model
    var info = this._mapper.Map<CardParameter, CardInfo>(parameter);

    // 呼叫依賴的 Service 層寫入資料
    var isInsertSuccess = this._cardService.Insert(info);
    if (isInsertSuccess)
    {
        return Ok();
    }
    return StatusCode(500);
}
```

現在讓我們來呼叫 API 試試吧！

這邊直接使用先前建置好的 [Swagger](https://igouist.github.io/post/2021/05/newbie-4-swagger/) 頁面來測試，並且故意把攻擊力打成負數：

![Image](https://i.imgur.com/dL34bdN.png)

![Image](https://i.imgur.com/omN0dax.png)

可以看到回傳的確變成了我們驗證失敗的訊息。

## 註冊 Validator 來自動進行驗證

不過都已經到了 .net Core 時代，[依賴注入](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection/) 已經是內建的功能下，還要用 `new` 一個驗證器這種直接依賴的方式還是有點不太舒服……所以 Fluent Validation 也有提供自動驗證的作法！

首先讓我們到熟悉的 `Startup.cs` → `ConfigureServices` 進行註冊：

```csharp
services.AddFluentValidation();
services.AddTransient<IValidator<CardParameter>, CardParameterValidator>();
```

補充：如果不想明確註冊每個類別的 Validator，也可以直接在 `AddFluentValidation` 的時候，使用反射組件自動註冊的方式來抓該組件底下所有的 Validator，比較不怕出錯、也更方便：

```csharp
services.AddFluentValidation(fv => fv.RegisterValidatorsFromAssemblyContaining<Startup>());
```

註冊好了之後就讓我們回到 Controller，並大膽地把驗證器相關的部分刪掉吧：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert(
    [FromBody] CardParameter parameter)
{
    // 將原本的參數檢查刪掉了！

    // 用 AutoMapper 把 Parameter Model 轉換成 Info Model
    var info = this._mapper.Map<CardParameter, CardInfo>(parameter);

    // 呼叫依賴的 Service 層寫入資料
    var isInsertSuccess = this._cardService.Insert(info);
    if (isInsertSuccess)
    {
        return Ok();
    }
    return StatusCode(500);
}
```

然後讓我們用 Swagger 再試一次看看：

![Image](https://i.imgur.com/YLRkBg0.png)

可以看到 Fluent Validation 自動幫我們擋了下來！

## 小結

當檢查參數的過程越來越冗長，為了做到關注點分離、讓方法本體更專注在流程上的處理，我們會選擇將檢查參數的邏輯拆分出去，例如拆成一個私有的 Function 等等。

這時候 Fluent Validation 就提供了我們一個更棒、更優雅的選擇。

本篇稍微記錄了 Fluent Validation 的基本用法，足夠應付大多數的使用場景。簡單小結如下：

- 繼承

   

  ```
  AbstractValidator<T>
  ```

   

  來實作我們的驗證器

  - 使用 `RuleFor` 來針對參數的欄位撰寫規則
  - 有許多內建的規則可以使用；或是使用 `Must` 來自定規則
  - 使用 `When` 可以指定規則生效的前提
  - 使用 `WithName` 可以指定欄位在訊息顯示的名稱
  - 使用 `WithMessage` 可以自訂驗證失敗時的訊息
  - 使用 `SetValidator` 可以指定參數某個成員要用的驗證器
  - 加上 `CascadeMode.Stop` 就可以在驗證失敗時直接跳出

- 使用 Validator 進行驗證

  - 可以直接建立驗證器來驗證
    - 如：`new CardParameterValidator().Validate(parameter);`
  - 也可以註冊進行自動驗證
    - 在 `Startup` 的 `ConfigureServices` 加上 `AddFluentValidation` 及驗證器的註冊

當然，FluentValidation 還有許多進階的應用可以探索，例如：

- 使用 [FluentValidation.TestHelper](https://docs.fluentvalidation.net/en/latest/testing.html) 來替驗證器寫單元測試

- 使用

   

  RuleSets

   

  來將驗證器規則分成多個規則集，再針對狀況使用

  - 例如新增和更新的功能共用同個參數的時候，就可以考慮使用規則集來指定各自要驗證哪些規則

- 需要客製化驗證失敗時回傳的 ViewModel 時，可以將

   

  ```
  validator.Validate
  ```

   

  包裝到 Attribute 裡進行攔截及驗證

  - 實際案例，敝司對 API 回傳格式有嚴格規範，於是前輩就在 Attribute 裡實例化 Validator 再從 actionContext 抓出參數驗證…

諸如此類，畢竟在參數驗證的路上發生什麼事也不奇怪，請再根據狀況自由地調整吧。

那麼，我們下回見～

## 參考資料

- [料理佳餚 - 讓 Fluent Validation 把參數的檢查條件口語化 | 軟體主廚的程式料理廚房 - 點部落 (dotblogs.com.tw)](https://dotblogs.com.tw/supershowwei/2016/04/30/005529)
- [C# .Net MVC 06. 驗證參數- 透過FluentValidation (progressbar.tw)](https://progressbar.tw/posts/117)
- [DotnetCore 後端驗證神器:Fluent Validation | Eugene’s Blog (eugenesu0515.github.io)](https://eugenesu0515.github.io/2021/08/24/fluent-validation/)
- [ASP.NET Core — Fluent Validation documentation](https://docs.fluentvalidation.net/en/latest/aspnet.html)
- [Fluent Validation 使用ActionFilter來驗證參數 | 菜鳥工程師訓練營 - 點部落 (dotblogs.com.tw)](https://dotblogs.com.tw/shadowkk/2019/07/23/140127)
- [基于 .NET 的 Fluent Validation 验证教程-零度 (xcode.me)](https://www.xcode.me/post/5849)
- [FluentValidation documentation](https://docs.fluentvalidation.net/en/latest/built-in-validators.html)

## 同系列文章

- [菜雞新訓記 (0): 目錄](https://igouist.github.io/post/2021/04/newbie-0-menu)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger)
- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)
- [菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection)
- [菜雞新訓記 (7): 使用 FluentValidation 來驗證傳入參數吧](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation)

## 附錄：FluentValidation 內建驗證方法 小抄

```csharp
void Main()
{
    var sut = new Card
    {
        Cost = 10,
        Name = "Blue-Eyes White Dragon",
        Type = CardType.Monster
    };
    
    var validator = new CardValidator();
    var result = validator.Validate(sut);
    
    result.Dump();
}

public class Card
{
    public CardType Type { get; set; }
    public int Cost { get; set; }
    public string Name { get; set; }
}

public enum CardType
{
    Monster = 0
}

public class CardValidator : AbstractValidator<Card>
{
    public CardValidator()
    {
        // Fluent Validation 的 驗證器請參照
        // https://docs.fluentvalidation.net/en/latest/built-in-validators.html

		// 驗證失敗時即停止
		//this.CascadeMode = FluentValidation.CascadeMode.Stop;

        // 為了示範所以做成變數，平時可以直接 RuleFor().XXX() 串接驗證器即可
        var name = this.RuleFor(card => card.Name);
        var cost = this.RuleFor(card => card.Cost);
        var type = this.RuleFor(card => card.Type);

        // 不可為 Null    
        name.NotNull();
        
        // 必須為 Null
        //name.Null();
        
        // 不可為空
        name.NotEmpty();
        
        // 必須為空
        //name.Empty();
        
        // 不可相同
        name.NotEqual("Test Card");

        // 不可相同：也支持 StringComparer
        name.NotEqual("Test Card", StringComparer.OrdinalIgnoreCase);
        
        // 不可相同：也可以比較其他欄位（大多驗證器都支援）
        name.NotEqual(card => card.Type.ToString());
        
        // 必須相同，其餘用法可參考 NotEqual
        name.Equal("Blue-Eyes White Dragon");
        
        // 長度限制，限定１～２００
        name.Length(1, 200);
        
        // 最大長度限制
        name.MaximumLength(200);
        
        // 最小長度限制
        name.MinimumLength(0);
        
        // 數值需低於目標值
        cost.LessThan(11);
        
        // 數值需低於或等於目標值
        cost.LessThanOrEqualTo(10);
        
        // 數值需高於目標值
        cost.GreaterThan(0);
        
        // 數值需高於或等於目標值
        cost.GreaterThanOrEqualTo(0);
        
        // 數值需介於兩個目標值之間
        cost.ExclusiveBetween(0, 11);
        
        // 數值需介於兩個目標值之間（包含目標值）
        cost.InclusiveBetween(1, 10);
        
        // 檢查是否具有指定的位數，例如 (1, 4) = 小數點限１位、總位數限４位
        this.RuleFor(x => (decimal)x.Cost).ScalePrecision(0, 2);
        
        // 正則表達式
        name.Matches(@"^[a-zA-Z-' ]*$");
        
        // 必須為信箱格式
        //name.EmailAddress();
        
        // 必須為信用卡格式
        //name.CreditCard();
        
        // 必須包含在列舉中
        type.IsInEnum();

        // 必須包含在列舉名稱中
        //name.IsEnumName(typeof(CardType));
        
        // 指定驗證場景
        cost.GreaterThan(0).When(card => card.Type is CardType.Monster);

        // 指定驗證場景
        this.When(card => card.Type is CardType.Monster, () =>
        {
            cost.GreaterThan(0);
        });
        // .Otherwise(() => { cost.GreaterThan(0); });

        // 最終大絕招：自訂驗證器
        cost.Must(power => power > 0 && power <= 3000);
    }
}
```

## 其他文章

- [菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection/)
- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture/)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi/)
- [C#: BenchmarkDotnet —— 效能測試好簡單](https://igouist.github.io/post/2021/06/benchmarkdotnet/)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger/)