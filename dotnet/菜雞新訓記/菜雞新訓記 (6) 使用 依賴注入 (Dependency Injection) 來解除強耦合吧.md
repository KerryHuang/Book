---
kind: reprint
source: https://igouist.github.io/post/2021/11/newbie-6-dependency-injection
author: igouist
---

# 菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧



![Image](https://i.imgur.com/2XYv7X2.png)

這是俺整理公司新訓內容的第六篇文章，目標是紀錄什麼是依賴注入（Dependency Injection）。包含：

- [為什麼要依賴注入](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection#為什麼需要依賴注入)
- [依賴注入的種類（建構式注入、屬性注入、方法注入）](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection#依賴注入的種類)
- [.net Core 中依賴注入的生命週期](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection#依賴注入的三種生命週期-transientscopedsingleton)

並用 [.net Core 實際跑一次依賴注入](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection#實作)，藉由將控制權轉移給注入容器，解除分層與分層間、類別與類別間的依賴和耦合關係，達到以介面分離實作的目標。

## 前言

西元前的某一天，憂心的皇帝在朝堂內繞著柱子走，正巧被路過的廷尉看見。

廷尉：「敢問陛下在煩惱什麼呢？」

皇帝：『朕這是在想封賞的事兒哪。前朝之所以覆滅，根本的原因就在於大肆封賞臣下，四處分封土地給他們做諸侯。

這些諸侯呢，肆意起用自己喜歡的人擔任要職、結黨營私，心情好就 `new 將軍("我ㄉ朋友");`，
十天就封了十個將軍。這些人若犯了錯，要處理他們還得看諸侯面子；而諸侯一聲令下，這些人便群起造反。

並且，這些諸侯之間彼此喜歡直接往來，動不動就在自家裡下命令給 `隔壁諸侯.借糧草(100)`，哪天就變成 `隔壁諸侯.揪團造反()`。彼此之間偷來暗去，實在難以掌握。

最後呢，一個逆賊起來造反，若要將他給辦了，附近諸侯就一起響應，每個都一齊報錯，Exception 成千上百，國家也就這樣滅了，想到這朕就頭痛得很，不知愛卿可有法子？』

廷尉想了一想，便說：「陛下，此事要點還是在於諸侯之間相互依賴、彼此耦合，致生禍端。

臣有一計，先收回諸侯的人事任命權，使其不可私自 `new` 自己人，所有人事異動，須由中央進行管理與派遣。這樣即使諸侯要造反，也不知道下面這群打工仔是不是自己人。大家各司其職，諸侯做好自己的行政作業，打工仔派到崗位就做好自己的工作，彼此不直接依賴，這樣出事的機率就少了。

其次，明令禁止諸侯私自往來，對諸侯們進行隔離，若是有公務上的需要，一律藉由中央提供的接口來溝通，彼此之間明訂契約，由中央進行隔離與調派，諸侯間就只需要按照協議好的合約下去合作，這樣勾結的機會也就少了，耦合也就降低了。陛下覺得如何？」

皇帝大喜：『如此甚好！治眾如治寡，在於分而治之。此計可有名字？』

「此乃－－依賴注入之計！」

### 為什麼需要依賴注入

各位好，我們前面引用了民明書坊的《朕的郡縣制哪有這麼耦合》，相信各位對依賴注入應該已經有初步的了解了。說到依賴注入的觀念，就得先從 SOILD 中的依賴反轉原則開始談。

這部份我們之前在[依賴反轉原則篇](https://igouist.github.io/post/2020/12/oo-14-dependency-inversion-principle)已經有詳細的說明，基於江湖道義，接下來就引用該篇的例子來快速帶過一下。

> 註：想好好了解的朋友，也可以從依序閱讀這幾篇相關文章後再回到這篇呦：
>
> - [多型](https://igouist.github.io/post/2020/07/oo-5-polymorphism)
> - [介面](https://igouist.github.io/post/2020/07/oo-7-interface)
> - [依賴反轉原則](https://igouist.github.io/post/2020/12/oo-14-dependency-inversion-principle)

讓我們從之前依賴反轉的範例開始吧：假設現在有間小小公司，老闆請來了小明當工程師，並請他開工撰寫產品程式碼。

當「撰寫產品程式」對「工程師」直接依賴的時候，狀況可能是這樣的：

```csharp
public Product Work() // 撰寫產品程式
{
    Ming programmer = new Ming();
    var product = programmer.Programming();
    return product;
}
```

過一陣子，老闆發現小明寫出來的東西似乎不太行，於是把小明趕走，另外請了小華。這時候因為用到的類別不一樣了，我們就必須要改一次程式碼：

```csharp
public Product Work()
{
    Hua programmer = new Hua(); // 把小明改成小華
    var product = programmer.Programming();
    return product;
}
```

又過了好一陣子，老闆又另外請了小美來工作。於是又要再改一次，而且小美的工作方式甚至不叫做 `Programming`，而是 `Coding`：

```csharp
public Product Work()
{
    Mei programmer = new Mei(); // 把小華改成小美
    var product = programmer.Coding(); // 呼叫方法也要改
    return product;
}
```

現在有感覺到一點問題了嗎？如果一直換人，`Work` 的程式碼豈不是每次都要修改？

但我們平常開發程式的思維，會習慣從大範圍到小細節、從抽象到具體、從整體目標逐漸拆解成各個步驟的方向去處理，也就是從高階模組往低階模組的方向設計。

例如說我們需要「會員查詢」功能，才用「DB 連線方法」和「資料篩選方法」等具體方式去達成我們要「會員查詢」這個目標。

然而以上面工程師的例子來看：低階模組的變更，卻會導致使用它的高階模組連帶受到影響，在我們決定大方向大目標的時候卻被實作細節綁手綁腳，實在是很怪的一件事，和我們上述的習慣是相悖的。

而依賴的低階模組越多，會被影響的機會就越高、修改的範圍和頻率也會急遽地拉高，變得無法掌握修改程式碼時影響的範圍，最終導致架構變得不穩固、程式碼到處都是不健康的[耦合](https://igouist.github.io/post/2020/09/oo-8-cohesion-and-coupling)。

面對這樣的困境，依賴反轉原則告訴我們：高階模組不應該依賴於低階模組。兩者都應該依賴抽象。

也就是指，我們可以不要讓高階模組直接去依賴低階模組，而是使用抽象的、具有契約精神的[介面](https://igouist.github.io/post/2020/07/oo-7-interface)來對他們進行隔離。

如此一來，只要介面的契約成立了，高階模組就可以專心做好自己的事情（[職責](https://igouist.github.io/post/2020/10/oo-10-single-responsibility-principle)），而不用去管低階模組的方法名稱之類的鳥事、低階模組也只要專注在實作介面要求的契約內容就行了。

在這裡的重要前提是，我們必須了解到：並不是高階模組去依賴低階模組，而是高階模組提出它需要的功能，低階模組去實作出這些功能、達成高階模組的目標，這也比較接近我們開發程式時的思維。

例如前面的會員查詢：我們並不是因為有「DB 的連線方法」和「處理會員資料的方法」所以才說「我們有這兩個東西欸，那我們來組成會員查詢功能吧」；而是「我們想做一個會員查詢功能，所以我們需要連線到 DB，然後對這些資料做篩選和處理」

而用工程師的例子來看，應該是要這樣的：「老闆為了製造產品（高階模組的目標），開出了工程師的應徵條件（介面），而小明前來應徵（低階模組的實作）」

如此一來，依賴就「反轉」了。原本是 `高階模組 → 低階模組` 的關係，變成了 `高階模組 → 介面 ← 低階模組`。

現在讓我們把上面例子的「工程師」改成介面，如此一來就會變成：

```csharp
// 工程師的介面
public interface IProgrammer
{
    void Programming();
}

// 小明，一位工程師
public class Ming : IProgrammer
{
    public void Programming() { /* Work */ }
}

public Product Work()
{
	// 這邊需要一名工程師，呼叫小明前來
    IProgrammer programmer = new Ming();

	// 根據介面的契約，工程師一定都有 Programming 方法
    var product = programmer.Programming();
    return product;
}
```

這邊就會遇到我們介面篇結束時所問的問題：我們使用功能之前，必須先建立該類別的實例，也就是 `new Ming()`，那麼，我們不就還是直接依賴了實作嗎？

面對這個問題，大大們提出了許多個解決的方法，其中最常見的就是：控制反轉 (Inversion of Control, IoC)。

思路非常的簡單：我們把實例的建立和實例的使用切分開來就好了，讓建立的去建立、讓使用的去使用，不再是由高階模組去建立並控制低階模組，而是我們讓一個控制反轉中心去建立低階模組，然後高階模組要使用的時候再把這個低階模組交給高階模組使用。

如此一來，控制權也跟著反轉過來了，高階模組從主動建立低階模組，變成被動接收低階模組；也就是從原先的 `高階模組 —(建立)→ 低階模組`，變成了 `高階模組 ←(傳遞低階模組)— 控制反轉中心`。

也就是說，高階模組再也不需要關心如何建立，該建立哪個實體，只專注於使用功能，真正達到介面的精神。低階模組也只需要等待控制反轉中心分發，到了崗位就把份內事做好，專心在自己的職責身上即可。如此一來就能解除兩者之間的耦合。

但是，要怎麼把控制中心建立的低階模組，交給高階模組做使用呢？這時候的實作方式就是我們今天的主角：依賴注入 (Dependency Injection)。

## 依賴注入的種類

白話一點來說，「注入」也就是「丟進去」的意思。所以依賴注入就是指用各種方法把低階模組丟到高階模組裡。

主要常見的有三種作法：建構式注入、方法注入、屬性注入。也就是從建構式丟進去、從方法丟進去、從屬性丟進去。

### 建構式注入

建構式注入顧名思義就是從建立物件時的建構式進行注入。

現在假設我們有個「法師」的類別，並且它有個屬性用來表示他目前裝備的法術：

```csharp
public class Wizard
{
    // 只有建構式時會給值，所以可以順手加上 readonly 防止被變動
    private readonly ISpell _spell;

    // 在建構式決定要裝備什麼法術
    public Wizard(ISpell spell)
    {
        this._spell = spell;
    }
}

public interface ISpell { } // 法術介面
```

而建立物件時也使用建構式來傳遞：

```csharp
void Main()
{
    var spell = new Fireball();
    var wizard = new Wizard(spell);
}

public class Fireball : ISpell { } // 火球術
```

由於建構式注入比較符合封裝的「管控邊界」精神、能明確地讓維護者一看就知道哪些東西會被注入，因此絕大部分的時候都應該使用建構式注入，只有特殊情況可以使用方法注入和屬性注入。而到了 .net Core 的時代，預設的 DI 容器更是只提供建構式注入。所以理想的情況下，建構式注入應該要是最熟悉的注入方式。

> 補充：要注意，對建構式做多載可能會造成 DI 容器混淆，不知道要選哪個建構式才好。因此設計類別時盡量以一個建構式為主，或是先了解一下使用的 DI 容器有沒有特別的處理方式再決定。
>
> 關於在 .net Core 裡面對多個建構式的對象註冊 DI 的作法，可以參閱黑大的這篇 [ASP.NET Core DI 之多建構式問題](https://blog.darkthread.net/blog/aspnet-core-di-multi-constructors/)

### 方法注入

方法注入適用於「呼叫方法時需要注入不同的依賴對象」時。例如說該方法在不同地方被呼叫的依賴對象不一樣，又或者是第一次呼叫和第二次呼叫時的依賴對象不一樣。

這時候我們就可以在呼叫方法的時候才把依賴對象一起丟進去，讓使用端來決定要注入什麼。

例如說我們的法師可以隨身攜帶法術卷軸，使用卷軸就可以放出對應的法術，因此法師類別就會有一個使用法術卷軸的方法。而我們想要等到施法的時候再決定要用哪個卷軸的咒語，這時候就可以把這件事情交給外部決定：

```csharp
public class Wizard
{
    // 施放指定的法術卷軸
    public void Enchant(ISpellScroll scroll)
    {
        scroll.CastSpell(); // 詠唱
    }
}

// 法術卷軸介面
public interface ISpellScroll
{
    void CastSpell();
}
```

那我們等到實際使用（使用卷軸施法）的時候再把依賴對象（卷軸）丟進去即可

```csharp
void Main()
{
	var wizard = new Wizard();
	var scroll = new LevitationCharmScroll();

	wizard.Enchant(scroll); // 使用卷軸施放漂浮咒
}

// 漂浮咒
public class LevitationCharmScroll : ISpellScroll
{
    public void CastSpell() {}
}
```

如此一來就可以處理一些每次操作依賴對象都會不同的狀況了。但在使用方法注入的時候要注意：由於該方法的呼叫端需要準備依賴對象給方法當作參數使用，整個過程是在方法被呼叫的時候才動態處理的，所以呼叫端還是需要想辦法弄到該依賴對象，也就是再從上一層注入或是工廠製造之類的。

在這個過程中就會增加類別或介面之間的依賴關係、並且讓注入的位置散落在各地等等，維護的時候就必須多注意一下。

我個人比較常在一些輔助工具，例如擴充方法或是 Helper 看到方法注入，像這類單純操作邏輯的場合，就可以考慮採用方法注入的方式去處理。

> 註：絕對不要把方法注入的依賴對象留在物件內部給其他方法使用，例如Ａ方法注入了某個物件，保留給之後呼叫Ｂ方法的時候用，這樣容易造成時序耦合（Temporal Coupling）的問題，也就是使用者（通常是後續的維護人員）不照你想好的順序呼叫的話，方法就會直接死去。
>
> 如果使用者不清楚這些方法之間的關係，就很容易踩到地雷，而這樣挖坑的行為很明顯違反了封裝精神，並且也容易產生預期外的副作用。如果真的有需要針對依賴對象做初始化，還是考慮用建構式注入吧。

### 屬性注入

接著讓我們來看看屬性注入，顧名思義就是從公開的屬性丟進去，因此有時候也會被叫做設值注入。

通常我們會在 「外部使用者要能夠隨時切換依賴對象」或是「類別已經有預設值了，但希望提供使用者可以覆寫掉預設值的彈性」時用到屬性注入，例如說我們的法師同時只能裝備／記得一個法術，預設是火球術，但同時我們又想要可以從外部來替換裝備中的法術：

```csharp
public class Wizard
{
	// 因為屬性注入的特性，請不要 readonly
    private ISpell _spell; 
    
    // 提供屬性給外部控制
    public ISpell Spell
    {
        get 
        { 
            // 屬性注入的時候要注意: 如果沒有預設值很容易會發生錯誤
            if (this._spell is null)
            {
                this._spell = new Fireball();
            }
            return this._spell; 
        }
        set 
        { 
            this._spell = value; 
        }
    }
}

public interface ISpell {} // 法術介面
public class Fireball : ISpell { } // 火球術
```

使用的時候就可以直接對屬性賦值，例如我們現在有個法師就不想用火球術，而是使用邪王炎殺黑龍波：

```csharp
void Main()
{
    var wizard = new Wizard();
    var spell = new DragonOfTheDarknessFlame();
    wizard.Spell = spell;
}

public class DragonOfTheDarknessFlame : ISpell { } // 邪王炎殺黑龍波
```

我個人是覺得屬性注入的範例其實就是使用介面的封裝小範例啦…。

提到封裝，由於使用者並不會知道物件內部的狀態，所以屬性注入沒有提供預設值的話就很容易壞掉，但給預設值的時候又不可避免地產生耦合（例如上例的法師為了預設是火球術，所以和火球術產生了耦合）

因此如果有為了將來的可擴充性而設計成「預設值使用內建的、通常會存在的類別，但允許外部隨時替換」，也就是讓呼叫端決定「要不要」依賴的場合，再考慮使用會比較合適。否則一律推薦建構式注入。

## 組合根（Composition Root）

認識完注入的方式之後，讓我們來聊聊組合根吧。前面的例子可以注意到：即使我們要注入法術給法師，也還是要在呼叫端建立法術的實體。而如果呼叫端也使用依賴注入，就會需要呼叫端的呼叫端來注入實體。層層反轉之下，最終就會有一個地方來注入和分配全部的實體給各個物件。

這也就是我們在前面提到的：我們會需要一個負責把各個材料注入到需要的類別中的「控制反轉中心」－－也就是叫做「組合根」的部份。

由於每一個類別會將依賴的對象交給外部，也就是呼叫者去決定。而呼叫者又會再往上拋給它的呼叫者，如此不斷往外推之後，就會集中到整個應用程式的啟動點，如此一來我們也就必須在啟動點進行依賴關係的處理。

因此這個組合根的位置通常會盡可能地靠近程式的啟動點，例如整個應用程式 Startup 的地方，或是各個 DI 容器最終註冊的部分。在我們的實作例子中，也就是 API 的專案部份。

> 補充：請注意，組合根並不一定是在展示層，並且從「為了管理依賴關係而產生組合根」和「為了切分職責而產生展示層」是不同的觀點，不能混為一談。退一步說，我們也可能會把啟動點、組合根之類的切分出去，減少展示層的耦合。所以還是要看專案架構怎麼設計的才能確定組合根的位置。

同時，由於組合根必須分配各個類別前往自己負責的崗位，因此它可以說是和所有模組都有直接依賴的關係（並且也應該只有組合根可以知道整體的物件關聯）。因此，我們應該要在應用程式啟動的部份，找個風水寶地去統一管理我們的組合根和依賴關係，而不能讓注入的部分散亂在各地。

不過這個部份現在的 DI 容器都已經處理好了，例如 Unity 的 UnityConfig、.net Core 的 ConfigureServices 等等，所以只要注意別在其他地方偷偷搞注入、挖坑給別人跳就好囉。

> 註：不要以為真的遇不到……同事維護的專案就有遇到前同事直接在單元測試案例裡把 DI 容器叫出來註冊依賴注入的，都不知道從哪裡開始吐槽囧

如果在別的地方去亂對依賴關係動手動腳，很可能就會踩到一些坑。總之，盡量別在組合根以外的地方使用 DI 容器。

## .Net Core 中的依賴注入

接著讓我們回到本系列的專案吧。可喜可賀的是：在 .net Core 的時代，依賴注入已經是內建提供的功能了！

> 補充：使用 .net Framework 的朋友也不用擔心，可以使用 Unity, AutoFac 這幾個猛猛的 IoC 容器。教學文章也是網路一抓一大把那種。
>
> 甚至到了預設使用建構式注入的 .net Core 時代，還是不少人會為了要用動態代理之類的花式注入手段而把 Autofac 裝回來呢。

我們得有一個地方來做我們的組合根，註冊介面和實體的關係，並讓它可以將實體注入進來。也就是要告訴應用程式：「某某介面 對應的就是 某某實作，請幫我在需要到的時候丟進來。」

在 .net Core 中，我們可以在 `Startup.cs` 的 `ConfigureServices` 註冊我們需要的服務：

```csharp
public void ConfigureServices(IServiceCollection services)
{
	services.AddControllers();

	// 這邊可能還有其他註冊的服務，Swagger 之類的
}
```

例如在先前的 [Swagger](https://igouist.github.io/post/2021/05/newbie-4-swagger) 我們就在這裡用套件提供的 `AddSwaggerGen()` 註冊過 Swagger UI 服務。

### 使用 `AddScoped` 來註冊介面對應的實作類別

而當我們要註冊我們的介面和實作時，例如說我們有一個 `ITestService` 的介面，希望告訴 DI 容器對應的實作是 `TestService`，我們就可以使用 `AddScoped<>` 來註冊對應關係：

```csharp
// 註冊 ITestService 的實作為 TestService
services.AddScoped<ITestService, TestService>();
```

如此一來，當 DI 容器發現要注入 `ITestService` 的場合，就會替我們建構 `TestService` 並注入。

![Image](https://i.imgur.com/Y5BexuX.png)

例如說我們的 `TestController` 的建構式部分如下，可以看到我們有使用建構式注入：

```csharp
public TestController(ITestService testService)
{
	this._testService = testService;
}
```

當 `TestController` 建立的時候，DI 容器就會知道需要 `ITestService` 來注入，並找到我們註冊的 `TestService` 來注入到 `TestController`。

這時候如果 `TestService` 也有需要注入的依賴對象，DI 容器就會再回來找我們註冊對應的實作，依此類推，不斷遞迴下去，直到注入都完成為止。

### 使用 `AddScoped` 和委派來註冊介面對應的實作類別的產生方法

有些朋友可能會有疑問：我的物件建立時還需要做一些處理才能建立，沒辦法直接告訴 `AddScoped` 就完事了。

不用擔心，`AddScoped` 也提供了委派的做法，讓我們可以直接告訴 DI 容器這個實作的產生方法，這個產生過程中我們就能進行一些操作，現在讓我們來示範一次。

假設我們的 `TestService` 必須要傳遞一個服務 Token 的字串進去，就會像是這樣：

```csharp
services.AddScoped<ITestService>(sp =>
{
	var token = @"TestServiceToken";
	return new TestService(token);
});
```

那如果不只是字串這種寫死的狀況，而是我們基於一些原因，想要指定拿到註冊中其他服務的實作的話，就可以使用委派傳入的 ServiceProvider 來取得目前註冊的內容，例如這個 token 其實是另一個 `ITokenService` 提供的話：

```csharp
services.AddScoped<ITestService>(sp =>
{
	var tokenService = sp.GetRequiredService<ITokenService>();
	var token = tokenService.Get();
	return new TestService(token);
});
```

可以看到，我們能藉由 `ServiceProvider` 的 `GetRequiredService` 這個方法來取得其他註冊的實體，並利用這個實體來完成注入所需的材料。

### 依賴注入的三種生命週期 Transient、Scoped、Singleton

除了 `AddScoped()` 以外，.net Core 還提供了另外兩種注入方法：`AddTransient()` 和 `AddSingleton()`，他們對應的是三種不同的生命週期：

- Transient（一次性）：每次注入都建立一個新的
- Scoped（作用域）：每次 Request 都建立一個新的，同個 Request 重複利用同一個
- Singleton（單例）：只建立一個新的，每次都重複利用同一個

假設我們有一個 `ILogger` 類別，專門幫我們寫 Log。然後我們的 API 會經過 `TestController`、`TestService`、`TestRepository` 這三層物件去查詢資料，其中每一層都注入了 `ILogger`。那麼：

- Transient：每一層物件都有自己的、全新的 `ILogger`
- Scoped：同一次 API 呼叫裡的每一層物件都是用同一個 `ILogger`，等到下一次呼叫才建立新的 `ILogger`
- Singleton：不論哪次呼叫、不論哪一層注入，所有人都共用同一個 `ILogger`

一般來說最常用的會是 Scoped，例如功能服務或登入者資訊，在同一次呼叫中保持同一個即可。但面對 HttpCilent 這類能共用同個實例節省資源的，我們就可以考慮使用 Singleton。這邊就再請各位按照使用場景來決定該用哪種生命週期。

另外，注入時請注意生命週期的範圍。例如註冊為 Singleton 的類別不能依賴註冊為 Scoped 的類別，因為如果大家一起用的 Singleton 程式跑到一半，綁在 Request 的 Scoped 依賴對象先消失了，問題可就大了，不可不慎。

> 關於 HttpClient 的部份，更棒的做法是使用 HttpClientFactory。可以參照：
>
> - [HttpClient，該 using 還是 static? - 黑暗執行緒](https://blog.darkthread.net/blog/httpclient-sigleton/)
> - [在 ASP.NET Core 中使用 IHttpClientFactory 發出 HTTP 要求 | Microsoft Docs](https://docs.microsoft.com/zh-tw/aspnet/core/fundamentals/http-requests?view=aspnetcore-6.0)

> 關於 Singleton 的部份，有興趣的朋友可以了解看看。
>
> - [單例模式 Singleton Pattern – LinZiyou Dev Blog](https://linziyou.info/2020/11/10/單例模式-singleton-pattern/)
> - [Singleton Pattern 介紹，是否為 Anti-pattern？ | by Camel | 嗨，世界](https://medium.com/哈嘍-世界/singleton-pattern-介紹-是否為-anti-pattern-1c685a1d7134)

### 延伸閱讀

- [ASP.NET Core 2 系列 - 依賴注入 (Dependency Injection) | John Wu’s Blog](https://blog.johnwu.cc/article/ironman-day04-asp-net-core-dependency-injection.html)
- [不可不知的 ASP.NET Core 依賴注入 - 黑暗執行緒](https://blog.darkthread.net/blog/aspnet-core-di-notes/)
- [.Net Core 服務存留期 (Service Lifetime)：叡揚部落格](https://www.gss.com.tw/blog/net-core-service-lifetime)
- [ASP.Net Core DI 容器中 Service 生命週期 | Ray’s Notes](https://raychiutw.github.io/2019/ASP-Net-Core-DI-容器中-Service-生命週期/)>)

### 補充：.net Core 使用 BuildServiceProvider 會建立多個實體

我們在前面提到過藉由 `AddScoped` 傳入委派的 ServiceProvider 的 `GetRequiredService` 方法來取得其他註冊的實體這個做法。

那可能就有一些比較聰明的朋友，知道 ServiceProvider 能拿到其他註冊的實體之後，為了在沒有 ServiceProvider 的地方也能取得其他實體（例如想直接在 `ConfigureServices` 就直接拿到實體，然後經過處理再提供給多個注入使用等等）

所以 Google 了一下怎麼弄出個 ServiceProvider，就用了 `BuildServiceProvider` 來建立一個 ServiceProvider，但這實際上是相當危險的。

因為 `BuildServiceProvider` 建立的是一個全新的 ServiceProvider，並非注入時 DI 容易幫我們建來使用的那一個 ServiceProvider，這樣就會造成有兩個 ServiceProvider 在場的狀況。

如此一來如果使用一些 Singleton 的服務，可能就會產生預期外的結果。因此建議還是乖乖在 `AddScoped` 之類的方法內使用委派的 ServiceProvider 比較好。

參考資料：

- [ASP.NET Core 3 系列 - 自行建置 Service Provider | John Wu’s Blog](https://blog.johnwu.cc/article/asp-net-core-3-build-service-provider.html)
- [c# - What are the costs and possible side effects of calling BuildServiceProvider() in ConfigureServices() - Stack Overflow](https://stackoverflow.com/questions/56042989/what-are-the-costs-and-possible-side-effects-of-calling-buildserviceprovider-i)

## 實作

現在我們稍微了解了 .net Core 裡的注入方式，接著就延續我們在 [分層架構](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture) 篇的進度，來把依賴注入導入到我們本系列的 ProjectN 菜雞專案吧。在上一期，我們利用分層的概念將整個流程拆分成 Controller, Service, Repository 三個主要區塊。

其中有直接依賴的部分，會在 Controller 銜接到 Service 以及 Service 銜接到 Repository 的部份。例如：

```csharp
public class CardService : ICardService
{
	private readonly ICardRepository _cardRepository;

	/// <summary>
	/// 建構式
	/// </summary>
	public CardService()
	{
		this._cardRepository = new CardRepository();
	}
}
```

可以注意到我們在 `CardService` 裡面直接 new 了 `CardRepository` 來使用，這就是直接依賴。

> 註：前篇分層時用到的 AutoMapper 套件的注入方式，請參見 [AutoMapper#走向注入](https://igouist.github.io/post/2020/07/automapper#走向注入)，此處暫且忽略。

基於依賴反轉原則，我們會希望達成「CardService 依賴的是 ICardRepository 這個介面，並由 CardRepository 實作該介面，藉由介面隔離實作來解除耦合」的目標。

> 對這個概念不太熟悉的朋友，可以參照 [介面](https://igouist.github.io/post/2020/07/oo-7-interface) 與 [依賴反轉原則](https://igouist.github.io/post/2020/12/oo-14-dependency-inversion-principle) 的說明

### 開始重構為建構式注入

現在讓我們改成使用建構式注入吧：

```csharp
public class CardService : ICardService
{
	private readonly ICardRepository _cardRepository;

	/// <summary>
	/// 建構式
	/// </summary>
	public CardService(ICardRepository cardRepository)
	{
		this._cardRepository = cardRepository;
	}
}
```

接著為了要讓 DI 容器知道 `ICardRepository` 對應的實作是 `CardRepository`，讓我們前往 `Startup.cs` 的 `ConfigureServices` 把它註冊起來：

```csharp
public void ConfigureServices(IServiceCollection services)
{
	// 註冊 ICardRepository 的實作為 CardRepository
	services.AddScoped<ICardRepository, CardRepository>();

	services.AddControllers();

	// 這邊可能還有其他註冊的服務，Swagger 之類的
}
```

> 補充：請注意前面提到過的「組合根會直接依賴所有註冊的模組」因此這邊有需要的話記得把參考 using 補上呦。
>
> 並且由於這個範例的組合根在展示層，因此和[上篇](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)的三層式架構圖略有不同，展示層也會依賴到資料存取層，還請注意。

接著讓我們如法炮製，把 Controller 裡直接依賴的 Service 也拆開吧：

```csharp
[ApiController]
[Route("[controller]")]
public class CardController : ControllerBase
{
	private readonly ICardService _cardService;

	/// <summary>
	/// 建構式
	/// </summary>
	public CardController(ICardService cardService)
	{
		this._cardService = cardService;
	}
}
```

然後補上註冊。

```csharp
public void ConfigureServices(IServiceCollection services)
{
	services.AddScoped<ICardService, CardService>();

	services.AddScoped<ICardRepository, CardRepository>();

	services.AddControllers();

	// 這邊可能還有其他註冊的服務，Swagger 之類的
}
```

最後再將前面系列用到的一些工具，例如 [AutoMapper](https://igouist.github.io/post/2020/07/automapper), [Dapper](https://igouist.github.io/post/2021/05/newbie-3-dapper/) 給注入好（這部分就請根據自己專案的內容調整囉），就完成啦。

那我們前面有提到，可以用「告訴 DI 容器該物件的產生方法」來做一些額外的事情，這邊就讓我們優化一下。

我們在先前的 `CardRepository` 有用私有欄位來存放連線字串：

```csharp
/// <summary>
/// 卡片管理
/// </summary>
/// <seealso cref="ProjectN.Repository.Interface.ICardRepository" />
public class CardRepository : ICardRepository
{
	/// <summary>
	/// 連線字串
	/// </summary>
	private readonly string _connectString = @"Server=(LocalDB)\MSSQLLocalDB;Database=Newbie;Trusted_Connection=True;";
}
```

現在我們希望連線字串不要寫死在類別裡，而是用建構式注入的方式丟進去，就會變成：

```csharp
/// <summary>
/// 卡片管理
/// </summary>
/// <seealso cref="ProjectN.Repository.Interface.ICardRepository" />
public class CardRepository : ICardRepository
{
	/// <summary>
	/// 連線字串
	/// </summary>
	private readonly string _connectString;

	public CardRepository(string connectString)
	{
		this._connectString = connectString;
	}
}
```

接著讓我們回到註冊 `ICardRepository` 的地方，因為 `CardRepository` 的建構式現在必須要提供連線字串了，所以我們要改一下 `AddScoped` 的寫法，把連線字串丟給它：

```csharp
services.AddScoped<ICardRepository>(sp =>
{
	var connectString = @"Server=(LocalDB)\MSSQLLocalDB;Database=Newbie;Trusted_Connection=True;";
	return new CardRepository(connectString);
});
```

可以看到我們用 `AddScoped` 提供了 `ICardRepository` 對應物件的產生方法。

這樣 .net Core 就會知道要先執行裡面的委派與匿名函式 `sp => {}`，就能拿到 `CardRepository` 來用囉！

### 補充：從 appsettings.json 取得組態

另外補充一下，在連線字串這類字串的注入時，我個人偏好更進一步使用 `appsettings.json`（以前 .net framework 時用過 `web.config` 的朋友可能會比較熟）

> 關於 appsettings.json 的用法這邊就不再贅述，想了解的朋友可以參考這幾篇：
>
> - [如何讀取 AppSettings.json 組態設定檔 | 余小章 @ 大內殿堂](https://dotblogs.com.tw/yc421206/2020/06/28/how_to_read_config_appsettings_json_via_net_core_31)
> - [ASP.NET Core 練習 - 使用 appSetting - 黑暗執行緒](https://blog.darkthread.net/blog/aspnet-core-practice-appsetting/)
> - [如何取得 appsettings.json 組態設定 ~ m@rcus 學習筆記](https://marcus116.blogspot.com/2019/03/how-to-get-value-appsettingsjson-in-netcore.html)

因此這邊就把連線字串丟到 `appsettings.json`，增加一欄 `ConnectionString`：

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  },
  "AllowedHosts": "*",
  "ConnectionString": "Server=(LocalDB)\\MSSQLLocalDB;Database=Newbie;Trusted_Connection=True;"
}
```

接著回到 `Startup` 的建構式，建立一個連線字串的欄位 `_connectionString` 然後把連線字串讀出來：

```csharp
public class Startup
{
	private readonly string _connectionString;

	public Startup(IConfiguration configuration)
	{
		Configuration = configuration;
		this._connectionString = configuration.GetValue<string>("ConnectionString");
	}
}
```

這樣我們就完成了 `Startup` 的連線字串注入囉，只要再把這個字串提供給 `CardRepository` 就行了：

```csharp
services.AddScoped<ICardRepository>(sp =>
{
	return new CardRepository(_connectionString);
});
```

如果沒有多個類別共用同一個連線方法的話，我們也可以直接從組態拿就行了：

```csharp
services.AddScoped<ICardRepository>(sp =>
{
	var connectionString = this.Configuration.GetValue<string>("ConnectionString");
	return new CardRepository(connectionString);
});
```

再請根據狀況靈活地運用 `Configuration.GetValue` 吧！

### 補充：組合根請稍作分類

這邊補充一下，在實務上由於一個應用程式的注入可能有數十個，因此我們會稍微用註解或可摺疊的 `#Region` 來分段一下，例如：

```csharp
public void ConfigureServices(IServiceCollection services)
{
    // Service
	services.AddScoped<ICardService, CardService>();
	
    // Repsitory
	services.AddScoped<ICardRepository, CardRepository>();
	
    // Others
	services.AddControllers();
}

// 或是使用 region，數量很多的時候就可以收攏
public void ConfigureServices(IServiceCollection services)
{
    #region -- Service --
	
	services.AddScoped<ICardService, CardService>();
	
	#endregion
	
	#region -- Repository --
	
    // Repsitory
	services.AddScoped<ICardRepository, CardRepository>();
	
	#endregion
		
    // Others
	services.AddControllers();
}
```

而前幾個月的時候，敝司某服務的註冊數量多到一個連滑鼠中鍵滾輪都會痛哭的程度。咱同事就利用對 `IServiceCollection` 做擴充方法的方式，將組合根分類並切出去管理：

```csharp
// ProjectN.DIExtensions

/// <summary>
/// Service 相關註冊
/// </summary>
public static class ServiceDIExtensions
{
	public static IServiceCollection AddServices(this IServiceCollection services)
	{
		services.AddScoped<ICardService, CardService>();

		return services;
	}
}

// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
	services.AddServices(); // 呼叫 ServiceDIExtensions 進行註冊

	services.AddRepositories();

	services.AddControllers();
}
```

雖然可以有效把註冊切分出去，但也會沒辦法在同個地方管理所有註冊，略麻煩，還是請真的有需要的時候再嘗試。這邊就當作分享這個做法給大家。

### 驗證

現在我們已經將三層的內容都改成使用注入了，最後就來測試一下是否有串接成功吧！

![Image](https://i.imgur.com/SFfOkFT.png)

下中斷點，可以看到我們 CardService 要求的 ICardRepository 的確傳入了實作的 CardRepository

![Image](https://i.imgur.com/1qS3DHL.png)

也成功從資料庫中查詢到卡片了！打完收工～

## 小結

這篇文章介紹了一些依賴注入的作法，並在 .net Core 的專案上進行實作。這邊就做個小總結：

- 為什麼要依賴注入
  - 解除類別與類別間的直接耦合
  - 由組合根來負責物件的建立和傳遞，更能讓依賴雙方專注於自己的職責
- 依賴注入常見的做法有
  - 建構式注入：把依賴對象從建構式扔進去
  - 屬性注入：把依賴對象從公開屬性扔進去
  - 方法注入：呼叫方法時再把依賴對象當參數扔進去
- .net Core 中的依賴注入
  - 是內建的功能，我們可以在 `Startup.cs` 的 `ConfigureServices` 進行註冊
  - .net Core 中，依賴注入的生命週期有
    - Transient（一次性）：每次注入都建立一個新的
    - Scoped（作用域）：每次 Request 都建立一個新的，同個 Request 重複利用同一個
    - Singleton（單例）：只建立一個新的，每次都重複利用同一個

最後還是要叮嚀一下，依賴注入在實務上還會遇到許多眉角，不同的 DI 容器也會提供不同的方法，或是面對眼前的架構不知道從何拆起之類的，這些都是重構日常。

例如說：

- [要怎麼對一個介面註冊兩個實作，再根據狀況使用？](https://dotblogs.azurewebsites.net/yc421206/2021/05/21/how_to_register_the_same_interface_for_multiple_implement_microsoft_extensions_dependencyInjection)
- [是不是可以乾脆把 DI 容器注入到對象中再彈性取用（就像服務定位器）？](https://stackoverflow.com/questions/22795459/is-servicelocator-an-anti-pattern)

等等的問題。

但我個人認為只要有依賴反轉、隔離耦合這些依賴注入的基本觀念，剩下的就是了解工具如何使用、開 Google 查詢有哪些坑的步驟而已了。~~然後上班一半時間都在 Google~~

除了藉由依賴注入去解耦合，避免讓類別成為控制狂（就是指類別依賴的對象都自己 new 出來，從建立到生命週期都由類別自己控制，最終變成強耦合的狀況）以外，我們使用依賴注入的時候，有時會發生一些令人困惑的事情，這些其實就是讓我們動手重構的好幫手。

例如說循環依賴，當我們發現Ａ類別依賴了Ｂ類別，Ｂ類別又依賴Ａ類別而發生錯誤時，就可以考慮是不是能夠整合這兩個類別，例如抽出一個更高階的類別來統合這兩個類別的動作流程等等。

又或是像過度注入：當我們用建構式注入的時候，有時候會發現其中幾個類別的建構式會變得超級肥，可能光是傳入參數就多達二三十個等等。

這時候其實就是一種警示：這個類別為什麼會依賴這個多個對象？是不是這個類別負責的[職責](https://igouist.github.io/post/2020/10/oo-10-single-responsibility-principle)太多了？

諸如此類，依賴注入其實可以幫助我們重新梳理我們類別的邊界和耦合關係，讓我們注意到一些需要重構的徵象。這也是最近跟著同事重構的心得哪。

那麼今天就先到這兒，祝各位解耦順利、斷開魂結。那麼，我們[下次](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation)見～

## 參考資料

- [依賴注入：原理、實作與設計模式 (Dependency Injection: Principles, Practices, Patterns, 2/e)](https://www.tenlong.com.tw/products/9789864344987)
- [[鐵人賽 Day04\] ASP.NET Core 2 系列 - 依賴注入 (Dependency Injection) | John Wu’s Blog](https://blog.johnwu.cc/article/ironman-day04-asp-net-core-dependency-injection.html)
- [Dependency Injection 筆記 (5) - Huan-Lin 學習筆記](https://www.huanlintalk.com/2011/11/dependency-injection-5.html)
- [NET Core 中的相依性插入 | Microsoft Docs](https://docs.microsoft.com/zh-tw/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-5.0)
- [mrkt 的程式學習筆記: ASP.NET MVC 專案分層架構 Part.6 - DI/IoC 使用 Unity.MVC](https://kevintsengtw.blogspot.com/2013/04/aspnet-mvc-part6-diioc-unitymvc.html)
- [DI(Dependency injection) 注入方式 - iT 邦幫忙](https://ithelp.ithome.com.tw/articles/10229256)
- [依賴注入 DI(Dependency Injection) - Sian](https://sunnyday0932.github.io/2020/依賴注入-didependency-injection/)
- [IOC(控制反轉) ， DI(依賴注入) 深入淺出~~ | 石頭的coding之路 - 點部落 (dotblogs.com.tw)](https://dotblogs.com.tw/daniel/2018/01/17/140435)
- [控制反轉 (IoC) 與 依賴注入 (DI) - NotFalse 技術客](https://notfalse.net/3/ioc-di)
- [搬砖方法论：组合根(Composition Root)_su9257的博客-CSDN博客](https://blog.csdn.net/su9257/article/details/115456338)
- [通過 Microsoft.Extensions.DependencyInjection，多個實作如何註冊相同的介面 | 余小章 @ 大內殿堂](https://dotblogs.azurewebsites.net/yc421206/2021/05/21/how_to_register_the_same_interface_for_multiple_implement_microsoft_extensions_dependencyInjection)
- [依赖注入DI的代替，服务定位器模式 - 简书](https://www.jianshu.com/p/33ea3da8a5a2)

其他參考資料

- [Levitation Charm | Harry Potter Wiki | Fandom](https://harrypotter.fandom.com/wiki/Levitation_Charm)
- [Dragon of the Darkness Flame (technique) | YuYu Hakusho Wiki | Fandom](https://yuyuhakusho.fandom.com/wiki/Dragon_of_the_Darkness_Flame)
- [秦帝國以後的郡縣制 - 維基百科](https://zh.wikipedia.org/wiki/郡县制#秦帝国以后的郡县制)

## 本系列文章

- [菜雞新訓記 (0): 目錄](https://igouist.github.io/post/2021/04/newbie-0-menu)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger)
- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)
- [菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection)
- [菜雞新訓記 (7): 使用 FluentValidation 來驗證傳入參數吧](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation)

## 其他文章

- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture/)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi/)
- [C#: BenchmarkDotnet —— 效能測試好簡單](https://igouist.github.io/post/2021/06/benchmarkdotnet/)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger/)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper/)