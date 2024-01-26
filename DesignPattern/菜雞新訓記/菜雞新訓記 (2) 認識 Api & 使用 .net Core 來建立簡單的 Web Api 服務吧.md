# 菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧



![Image](https://i.imgur.com/d2xM94x.png)

這是俺整理公司新訓內容的第二篇文章，目標是對 Api, Restful Api, HTTP 等相關的知識點做個筆記，並用 .net Core 建立一個簡易的 Web Api 專案。

## 前言、基本觀念

我們在 [上一篇](https://igouist.github.io/post/2021/04/newbie-1-hello-git) 記錄了新訓第一天的 Git 操作筆記。接著在這篇，我們終於要進入 .net Core 啦！

目前的規劃是先從建立一個可以使用的、最簡單版本的 Web Api 服務開始，再將各個工具擴增進來。所以後續的文章應該都會以這篇的簡易 API 為基底繼續延伸下去（如果順利的話啦）

這篇文章的前半段會用來記錄一些使用或開發 API 常用到的相關知識，如果對 HTTP 的部分已經有點頭緒，或是迫不及待想直接動手用 .net Core 開 Api 服務的朋友們，可以直接跳到 [正式開工](https://igouist.github.io/post/2021/05/newbie-2-webapi/#正式開工) 的部份。那麼，我們開始吧～

------

### 什麼是 API

我們在物件導向的 [介面](https://igouist.github.io/post/2020/07/oo-7-interface/) 時有稍微聊過所謂介面（Interface）的概念：「在兩個系統，或是兩個分層之間要介接的時候，只需要提供我這個功能的接口／介面給對方，就能讓對方知道如何使用」

API（Application Programming Interface）也是同樣的道理：

在不同的應用程式或服務（Application）之間，使用程式碼（Programming）的方式提供一組 介面（Interface），讓提供方和使用方可以藉由這組介面銜接起來。

API 最貼切的比喻就是我們在 [封裝篇](https://igouist.github.io/post/2020/07/oo-3-encapsulation) 也用過的販賣機：販賣機會提供不同飲料的按鈕，當我們選擇了其中一個按鈕按下、投了錢之後，對應的飲料就會掉下來。

對應回來就是：我們到了某個服務（販賣機），去拿我們想要的資料（飲料），所以呼叫了該服務的某支 API（按鈕）並且提供了一些該 API 要求的資料（投錢），最後 API 就會把我們想要的資料交給我們（飲料）

再用更實際的例子來說就像是：假設我們想要做一款可以查詢台北市的公車動態的 APP，於是我們到了提供公車動態的服務 [MOTC Transport API v2](https://ptx.transportdata.tw/MOTC?t=Bus&v=2#!/CityBus/CityBusApi_RealTimeByFrequency) 去找我們想要的 API，過程中我們可能需要告訴服務我們要查的是台北市，最後服務就會將公車動態的資料交給我們。

關於 API 的部份，推薦可以先閱讀過 Huli 大大的這兩篇，將基本觀念說明的相當好懂且透徹：

- [從傳紙條輕鬆學習基本網路概念](https://medium.com/@hulitw/learning-tcp-ip-http-via-sending-letter-5d3299203660)
- [從拉麵店的販賣機理解什麼是 API](https://medium.com/@hulitw/ramen-and-api-6238437dc544)

另外，也推一下我在 CodingBar 看到的這篇 [API 到底是什麼？ 用白話文帶你認識](https://medium.com/codingbar/api-到底是什麼-用白話文帶你認識-95f65a9cfc33) 和它所引用的影片：

<iframe src="https://www.youtube.com/embed/zvKadd9Cflc" width="100%" height="480" frameborder="0" scrolling="no" allowfullscreen=""></iframe>

------

### 什麼是 Restful API

都提到 API 了，當然不能不提 Restful 了。Restful 說起來比較像是 API 界的一種流派，大概就像「飛天御劍流」之於「劍道」的關係一樣。只不過因為 Restful 太 Restful（？），所以幾乎已經成為主流了。

那麼 Restful 到底是什麼呢？

前一段我們有提過，API 的一個重點是：提供我這個功能需要的接口／介面給對方，就能讓對方知道如何使用。

如果有點進去看 Huli 大大的文章，尤其是 [傳紙條](https://medium.com/@hulitw/learning-tcp-ip-http-via-sending-letter-5d3299203660) 那一篇的話，應該會察覺到在資料交換的過程中，最重要的一環就是建立共識，或者說是建立原則以降低溝通成本。

Restful 想做的也是同一件事：只要大家都有一個制定路由的共識，就可以降低閱讀和維護成本。

原先的 API 在路由的制定上並沒有什麼原則，幾乎就是看提供者爽怎麼訂就怎麼訂：

```
/api/create-order
/api/getProduct?id=1
/api/productDetailByProductId
```

但這樣就會造成額外的溝通成本。

為了消除這些溝通成本，Restful 就出現了！Restful 提倡使用「符合 HTTP 語意」和「以資源為主」的方式來處理 API 的路由。

我們用白話一點的方式來理解：大多數時候，我們發出的請求都是「對『什麼東西』做『什麼動作』」，也就是通常會有一個「動詞」和一個「目標」，Restful 就是從這兩個部份下手來達成共識。

那我們從「動作」的部分開始，也就是建立「符合 HTTP 語意」的共識：我們可以利用 HTTP 定義的請求方法（HTTP Method，也被稱為 HTTP 動作）來表達我們的要求。

上面推薦過的 Huli 大大這篇[傳紙條文章](https://medium.com/@hulitw/learning-tcp-ip-http-via-sending-letter-5d3299203660)中有提到，因為能做的事情太多了，光是一個訂便當相關的動作，既可以訂購便當，也要能查有哪些便當可以訂，或是訂好了卻要換成別的便當等等。因此為了將動作做個統一，就在紙條的 Header 加了欄位，用來標示這次動作是哪種類型，這就是所謂的 HTTP 方法。

#### 常見的 HTTP Method

我們比較常見的 HTTP 方法有這幾個：

- `GET`
  - 用來查詢、取得資源。例如說「Get 最新的一筆訂單」
- `POST`
  - 用來建立新資源。例如說「Post 一筆新訂單」
  - 也可以用來當萬用動詞，就是不太確定歸類在哪一個、使用其他動詞遇到障礙的時候使用
- `PUT`
  - 通常用來更新現有的資源。例如說「Put 一號訂單的新訂單內容」
  - 如果服務有額外處理的話，有時候也會做成 沒有這筆資源就新增一筆
- `PATCH`
  - 用來更新資源的時候做「部分更新」。例如說「Patch 一號訂單的出貨狀況」
- `DELETE`
  - 用來刪除資源，例如說「Delete 一號訂單」

其中有幾個部分可能會讓人有點疑惑，這邊稍微整理一下，也歡迎大家補充：

------

#### PUT vs PATCH 都是更新？

兩者的更新方式不太一樣。通常 PUT 會指整批更新、PATCH 是指部分更新。

以產品舉例的話：

- `PUT` 比較像是把整個產品資料丟上去，然後整團更新掉
- `PATCH` 則是只更新一部份，像是只丟產品名稱上去，然後就只更新名稱

------

#### POST 的「萬用動詞」是什麼意思？

- 我們有時還是會遇到不太確定要歸類到哪個動詞，或是其他動詞處理不來的情況，預設就使用 `POST` 處理
- 例如說，以 `GET` 查詢的時候，參數的規劃有些問題導致於 QueryString 放不太下，就可以考慮改用 `POST`，並將參數放入 Body

------

#### 安全（Safe）、冪等（idempotent）

在查詢 HTTP 動作的時候（例如維基百科的[請求方法](https://zh.wikipedia.org/wiki/超文本传输协议#请求方法)），總是會看到「安全（Safe）」、「冪等（idempotent）」這些用詞，是什麼意思？

- 安全（Safe）的方法是指沒有對資料進行變更的操作

  。例如：

  - 當我 `GET` 的時候，我單純只是查詢資料
    不會對資料進行任何變動，所以是安全的
  - 反過來說像是 `PUT`, `DELETE` 這些會對資料進行變更的方法就是不安全的
  - 使用不安全的方法的時候，就得要考慮用特殊的方式告訴系統的使用者該操作可能的變更。例如前端呼叫前會跳出視窗警告：「確認是否刪除」等等

- 冪等（idempotent）則是指該方法在同樣的條件下，不管重複作幾次，對資源的結果都相同

  。例如：

  - 我一直 `GET`，不管我 `GET` 幾次，資料還是同樣那一份不會變動

  - 我一直 `PUT`，不管我 `PUT` 同樣的參數幾次，資料的結果還是會長一樣

  - 我一直 `DELETE`，不管我 `DELETE` 幾次，那一份資料都一樣不在了

  - 我一直 `POST` ，就會一直長出新資料（！注意，不是 idempotent ！）

  - ```
    PATCH
    ```

     

    的部份比較特殊一點：

    - 因為我們要求更新這個資源的某一些部份的時候，並不能確定其他地方會不會變動
    - 例如說，我們更新了 產品描述 這個欄位，結果其實還有一個欄位是 版本號，然後服務偵測到每次更新都會自動增加。
      這樣我們就算重複 `PATCH` 結果也有可能不一樣，因此 `PATCH` 並不能算是 idempotent 的

當我們知道一支 API 是不是安全的、是不是冪等的，也就可以幫助我們知道這支 API 能不能重試，當遇到某些問題時能不能大膽地再打一次請求過去。

例如說連續查詢兩次並不會對資料進行任何變動，就可以原地重查一次；但面對扣款這種危險狀況，我們當然就不會想再扣一次錢。當我們確實按照安全和冪等這些特性來運用 HTTP 動詞，就可以讓使用端得到這些資訊。

------

#### 小小結與推薦閱讀

那麼補充就先到這裡。除了上面只列出了我個人平常比較常接觸的 HTTP 方法之外，其他還有 `HEAD`、`TRACE` 等等，有興趣的朋友可以再逛逛 MDN 的 [HTTP 請求方法](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Methods)。

現在我們大概知道了有這些 HTTP 方法可以使用，也因此已經將動作抽離出來了。接著就輪到我們要進行這些動作的「目標」了，這部份則要求：我們在制定路由的時候，應該從「資源」的角度下去考慮。

這相當直覺，例如「新增 訂單」、「查詢 產品」這樣，我們動作後面接續的應該要是一個資源。從這個方式下去定的話，上面的範例應該就會變成：

```
POST /api/order
GET /api/product/1
```

很明確就能夠看出意圖。這邊就讓我們來看看微軟的 [Web Api 設計](https://docs.microsoft.com/zh-tw/azure/architecture/best-practices/api-design#define-operations-in-terms-of-http-methods) 文中的範例表格：

| Resource            | POST                | GET                   | PUT                              | DELETE                |
| ------------------- | ------------------- | --------------------- | -------------------------------- | --------------------- |
| /customers          | 建立新客戶          | 擷取所有客戶          | 大量更新客戶                     | 移除所有客戶          |
| /customers/1        | 錯誤                | 擷取客戶 1 的詳細資料 | 更新客戶 1 的詳細資料 (若有的話) | 移除客戶 1            |
| /customers/1/orders | 為客戶 1 建立新訂單 | 擷取客戶 1 的所有訂單 | 大量更新客戶 1 的訂單            | 移除客戶 1 的所有訂單 |

這邊大致上有個感覺就行了，畢竟 Restful 是一種風格，並沒有強烈的規定，只要符合共識和約束，就可以算是 Restful 了。

在微軟把拔的 [RESTful Web API 設計](https://learn.microsoft.com/zh-tw/azure/architecture/best-practices/api-design) 中，援引了 Leonard Richardson 的 API 成熟度模型：

- 等級 0：定義一個 URI，而所有的作業對此 URI 都是 POST 要求
- 等級 1：針對個別資源建立不同的 URI
- 等級 2：使用 HTTP 方法來定義資源上的作業
- 等級 3：使用[超媒體 (HATEOAS)](https://learn.microsoft.com/zh-tw/azure/architecture/best-practices/api-design#use-hateoas-to-enable-navigation-to-related-resources)

目前就內文所述，大多數的已發行 API 約略是等級 2 附近，也就是這次介紹的：使用 HTTP 動詞 + 從資源出發的設計方針。只要掌握這個方向，基本上就沒什麼問題了。

同樣的，這個訂立的原則，也就得仰賴多去看人家的 Api 怎麼設計來培養了。但只要把握幾個重點：建立共識、提高可讀性，還有設計的時候好好和來介接的夥伴喬一下，基本上就不會有什麼差錯啦，畢竟這東西很彈性的。

當然，本篇只是稍微說明而已，非常鼓勵各位朋友再進一步搜尋了解。最後推一下這兩篇 Restful API 相關的文章：

- 休息(REST)式架構? 寧靜式(RESTful)的Web API是現在的潮流？
  - 我個人覺得寫得很清楚明瞭，並且範例也相當好懂，咱們當初新訓的時候也是看這篇來了解概念的
- 簡明 RESTful API 設計要點
  - 針對一些要點有說明，有興趣的朋友可以稍微看過一遍。內文提到的 HTTP Status 我們等等也會進行說明

------

### 什麼是 HTTP Request 和 Response

現在讓我們運用動詞（HTTP 動詞）和名詞（Restful 風格的路由），就可以組出像是 `GET product/1` 這樣子的 Api 路徑。用寄送信封的方式來說的話，現在我們就等於已經掌握了寄送的地址。

我們有了地址之後，才能寄信到這個地址給對方，並且等待對方的回信（話說這年頭大家都用網路通訊了，會不會過幾年沒人看得懂這組經典比喻啊？）。

而我們有了 Api 的地址（URL）之後，就可以對這個地址上的服務送出一個 Request（請求），服務接受到請求之後，就會給予我們一個 Response（回應）。

這個送出請求、取得回應的動作，就是網路運作的原理。例如當你打開瀏覽器到某個網站，就是對該網站發出一個取得網站內容的請求，網站再給你網站內容的回應。

> 補充一下，聰明的朋友可能發現了，我們前面介紹的 Api 也就是這組動作：當我們呼叫某個服務，例如 Google Map 的 Api，也就是對目標的 Api 發出了一個想要使用服務的請求，服務再針對請求給予回應。因此，要想了解 Api 的各個知識點，接觸 HTTP 是必不可免的。
>
> 但 HTTP 這水挺深的哪，所以我們這篇的紀錄先以「打 Api 服務的時候不至於都看不懂」為目標進行，稍微介紹一下 Request 和 Response 的內容吧。來日方長嘛。

Request 和 Response 的內容，有興趣的朋友可以直接在瀏覽器進入開發人員工具就能看到了，以 Edge 和 Chrome 為例：首先按下 F12 ，並找到網路（Network）的部分，就可以看到進入網頁的各個請求和回應，隨便點開一個就會有 Request 和 Response 的內容囉：

![img](https://i.imgur.com/kdK0xo1.png)

或者是可以直接參考 NotFalse 技術客的這篇 [HTTP/1.1 — 訊息格式 (Message Format)](https://notfalse.net/39/http-message-format)，裡面對 HTTP 請求格式的各個部分上色並逐步講解的方式讓我蠻喜歡的，相當清楚。

接著就讓我們來看一下訊息的格式，通常會分成三個比較主要的區塊：Start Line、Header、Body：

```json
HTTP/1.1 200 OK // Start Line

// Header
Content-Type: application/json; charset=utf-8
Date: Mon, 26 Apr 2021 14:00:31 GMT

// Body
{
  "name": "nike",
  "category": "shoes"
}
```

首先讓我們看看 Start Line：

```json
HTTP/1.1 200 OK // Start Line
```

Start Line 在 Request 的時候又叫做 Request-line，會標明 HTTP Method、URL、HTTP 版本。

例如 `GET /product/1 HTTP/1.1`。我們 [上一節](https://igouist.github.io/post/2021/05/newbie-2-webapi/#關於-restful-與-http-method) 學的 HTTP 動作（GET、POST…）和路由地址（`/product/1`）就是用在這裡。

而 Start Line 在 Response 的時候又叫做 Status-line，會標明 HTTP 版本、HTTP 狀態碼（Status Code）和描述。

例如 `HTTP/1.1 200 OK`，這個狀態碼就是 Response 中的主要回應，我們在 [下一節](https://igouist.github.io/post/2021/05/newbie-2-webapi/#關於-http-status-code) 會介紹一些常看到的 Status Code，現在先知道這裡就是服務用來告訴你「好呀」跟「不要」的地方即可。

Start Line 會放在整個訊息的第一行，之後會用個空行做分隔，後面再接著 Header。

讓我們順著來看看 Header：

```json
// Header
Content-Type: application/json; charset=utf-8
Date: Mon, 26 Apr 2021 14:00:31 GMT
```

Header 又叫作標頭、表頭等，主要是用來放這次訊息相關的參數和資訊。

例如說用 Content-Type 來說明這次訊息傳輸的格式，可能是表示 HTML 的 `text/html`，或者是表示 JSON 的 `application/json` 等等；也有可能用 `cookie` 來表示瀏覽器當前紀錄的資訊等等。

Header 可以放的資訊有挺多種的，有興趣的朋友可以看看這篇 [HTTP 前後端傳輸流程](https://medium.com/ttyy2985/http前後端傳輸流程-8ee40ffca1bd)，列出了常見的 HTTP Header 欄位；如果好奇上面提到的 Content-Type 有那些常用的種類，也可以參照這篇 [Postman 常見的 Content-type](https://medium.com/hobo-engineer/ricky筆記-postman-常見的-content-type-b17a75396668)，這邊就先按下不表。

Header 結束之後，按照訊息的種類和內容，可以再加上 Body，兩者之間會空一行隔開：

```json
// Body
{
  "name": "nike",
  "category": "shoes"
}
```

Body 又叫做回應主體，是非必須、選填的，通常我們會用來存放本次訊息需要的資料。

以寄信來舉例的話，Header 就像是外面的 寄信人、收件人等資訊，而 Body 則是裡面的信件內文。但要注意，一個訊息並不一定要有 Body，就像我們也可以只寄送明信片一樣。很常聽到的一個比喻就是：GET 就像明信片、POST 就像是包裹，中間就是需不需要附加 Body 的差別。

當 GET 的時候，我們通常並不會用到 Body，如果有需要附上參數的話，GET 我們會放到 QueryString（就是接續在往指後面，常常見到的 ?a=1&b=2 那串）。

例如說取得產品列表，我們需要向 `/product` 發出 `GET` 請求，同時我們又只想要類別是鞋子、關鍵字為 Nike 的產品，那我們組出來的整個 URL 和 QueryString 可能就是這樣的：

```json
GET /product?category=shoes&keyword=nike

/* 這邊會有一些 Header */
```

其他的場景，例如 POST 時，如果有需要附上資料，我們通常會用到 Json 或 XML 之類的格式放到 Body 中。例如我們現在要新增一筆新的產品，是叫做 Nike 的鞋子，那可能就會附上：

```json
POST /product

/* 這邊會有一些 Header */

{
  "name": "nike",
  "category": "shoes"
}
```

如果是 XML 的話，可能就會是這樣表示：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <name>nike</name>
  <category>shoes</category>
</root>
```

當然也有可能是用其他的格式，只要服務願意接受，兩邊能夠通訊其實也就沒什麼關係，說到底網頁最基本的部分也還是一個回傳 HTML 格式的 Response。所以各位如果遇見了沒看過的格式也不用驚慌，因為放在這裡都一樣是用來表示資料的格式，只是表達的方式不一樣而已。

不過我平常開發和使用 API 都是用 JSON 的場合居多（個人覺得體感上 JSON 已經快一統 API 的天下了），強烈建議至少還是要能看懂 JSON。

> 備註：關於 JSON 如果不太了解的朋友，可以參閱 [JSON精要讀書紀錄](http://miniaspreading.github.io/guide-to-json/1-what-is-json.html)

最後再複習一次，當我們呼叫一個 API 的時候，我們可能會送出一個 HTTP Request（請求）

```json
GET /product/1 HTTP/1.1 // Start Line

// Header
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) //...其他一堆標頭
```

然後服務就會回給我們一個 HTTP Response（回應）

```json
HTTP/1.1 200 OK // Start Line

// Header
Content-Type: application/json; charset=utf-8
Date: Mon, 26 Apr 2021 14:00:31 GMT

// Body
{
  "name": "nike",
  "category": "shoes"
}
```

這樣我們就成功交換資料啦！

……當然，所謂天有不測風雲，API 有 500 Internal Server ERROR，沒有每次打 API 都一定是 OK 的啦，其他什麼 404, 500 動不動就會跑出來。

就像我們去網路購物的時候，按下購買把購物車清空後，網頁就會告訴我們「訂單成立」或是「結帳失敗」等等，當 API 的使用者將這個要求發送給 API 服務，服務就會告訴使用者針對這個要求的回應。這就是我們之前提到的 HTTP 狀態碼（Status Code）出場的時候了。

------

### 什麼是 HTTP Status Code

在上個小節中我們有提到，Response 的 Start Line 會帶著一組 HTTP 狀態碼（Status Code）和描述，用來告訴你這次請求的回應。

大概就像是告白之後的好呀、謝謝你、你是個好人等等，回應也有分成很多種，這邊就稍微紀錄一下平常遇到的幾種狀態。

------

1xx: 參考資訊

- 大多是在正式回應之前先暫時給使用者一些資訊。就像是「先讓我考慮一下…」

------

2xx: 成功

- 200: 要求成功。就像是「好呀」
- 201: 已建立。要求新增資源的時候會用到，就像是「OK，那我掛穩交囉」
- 204: 無內容。雖然點頭了，可是什麼話也沒說

------

3xx: 重新導向

- 301: 永久轉址。就像是傳了簡訊之後得到「她換手機了，我是她爸」
- 303: 臨時轉址，原本存在但是換了位置，就像是打電話過去結果「她出門了，我是她爸」
- 304: 沒有變動，可以直接去快取拿就好。就像是「說啥呢，我們都結婚五十年了= =」

------

4xx: 用戶端錯誤

- 400: 要求錯誤，大多數使用者造成無法處理的問題都會丟到這，可能是
  參數沒給、這個網域不存在等等。就像是『她』說「其實我是 ♂ 的呦，沒關係嗎？」
- 401: 拒絕存取，可能是沒有登入、授權失敗等等。
  就像是「你是誰？！我根本不認識你啊？！」
- 403: 禁止使用，可能是沒有權限、沒有憑證、被拒絕等等。
  就像是「抱歉，你的長相實在…抱歉。」
- 404: 找不到，這個應該是最常見的用戶端錯誤了。
  就像是「你認錯人了吧…？」
- 418: [我是個茶壺](https://blog.huli.tw/2019/06/14/http-status-code-418-teapot/)，啊人家就只是個茶壺…

------

5xx: 伺服器錯誤

- 500: 內部伺服器錯誤，大多數問題都會被丟到這一類，我們開發人員頭痛的時候就到了…
- 501: 未實作，通常對一個只提供 `GET` 的 `URL` 打 `POST` 就會看到了。
  就像是「我已經結婚囉，謝謝你呢 ^^」
- 502: 無效回應。就像是「我也喜歡哆啦Ａ夢呢」
- 503: 伺服器維護或過載。追求者太多了，根本沒空回你。
- 504: 閘道逾時。（已讀不回）。

------

對還有哪些 HTTP Status 或是想對每個 HTTP Status 發生的狀況了解得更詳細的朋友，可以參閱以下兩篇：

- 常見與不常見的 HTTP Status Code - Noob’s Space
  - 除了列出常見的 HTTP 狀態，還收錄了一些非官方和惡搞的
  - 看了這篇知道更多 HTTP Status Code 之後，本網站正考慮支持 HTTP Status 735
- 網頁開發人員應了解的 HTTP 狀態碼 - The Will Will Web
  - 針對每個狀態有更詳細的說明，並列出了更細的 IIS 擴充狀態，例如 401.1 - 登入失敗等等
  - 強力推薦 Dotnet 相關的開發人員看個一遍有個印象

------

### 什麼是 Stateless

> 2021/5/4: 發文之後發現忘記提到無狀態了，所以這邊回來補充一下。

接續前面提到的 Restful 風格，在 API 的制定上，Restful 還有另一個要求，就是必須是 無狀態的（Stateless）。

無狀態是指：伺服器不會儲存使用者的狀態，當使用者呼叫 API 的時候，應該給予所有 API 需要的內容。

用比較的方式來說：原本的 API 設計可能會保存使用者的動作狀態，然後留到下一次呼叫的時候再接著使用，那這樣的 API 設計的時候就像是制定食譜，必須要求使用者照順序才可以正常運作。

例如必須先打Ａ，再打Ｂ，最後打Ｃ，沒有照順序打的話就會因為狀態不對而壞掉。但這樣的做法其實就是所謂的 [時序耦合](https://dotblogs.azurewebsites.net/Im_sqz777/2021/04/18/what-is-temporal-coupling)，不僅造成測試和使用上的困擾，也相當的不直覺、相當的有「味道」。

而我們在 Restful 的時候，是用資源的方式下去考慮，所以應該把重點放在資源的操作，而不是狀態的管理和流程，否則就會很奇怪。例如說你去買雞蛋，然後老闆突然跟你說：不行喔，因為你還沒買過牛奶。哇，整個就莫名其妙。

所以在 Restful 的設計上，每一次呼叫都應該要是獨立的呼叫，設計的時候就是以資源為主體，再利用這些資源互相搭配來完成功能。

例如說「登入之後跳出使用者待結帳的訂單，並且 Show 出訂單中的產品」這種情況，我們就不該要求使用者一定要照順序打，然後伺服器再來記住登入的資訊、使用者的編號、訂單的編號等等，除了記錄一堆多餘的資訊，更把 API 的使用場景給卡死了，相當不 OK。

這邊用資源的角度出發的話，應該讓「登入」、「查詢訂單（使用者呼叫時提供使用者編號）」、「查詢產品（使用者呼叫時提供訂單編號）」組合起來，從「將這些資源的操作組合在一起完成功能」的角度出發，那在別的流程就可以重複使用這些 API 來組成功能，同時也能分別對各個功能進行開發跟測試。

如此一來，就能提升彈性、自由度。同時，因為伺服器不用紀錄狀態，讓每一次呼叫都是獨立的呼叫，不只可以重複使用，聚焦在資源上也能讓操作變得簡潔。進一步來說，因為狀態不會被綁死在特定的機器上，那就可以開始搞擴大加機器做分散式啦。

> 補充一下：當然，要做到完全沒有狀態是很難的，但我們可以做到讓伺服器不要綁死、每個呼叫都是盡量獨立的，來盡可能使得服務乾淨、有彈性、可分散處理。
>
> 同時也因為這樣，為了讓使用者的狀態不會遺失（例如登入狀態），就得做到使用者的每個呼叫都要能夠證明自己的身份，所以才有了壓成 Token、把身分驗證的伺服器分離等等的驗證做法，這個部份我們有空再來填坑吧。

## 正式開工

現在，我們已經大概了解 API 以及 Restful API 的一些相關知識了，接著就讓我們來實際建立一個簡單的 API 服務吧！

### 新建 .net Core Web API 專案

首先打開我們的 Visual Studio，建立新的專案。

![img](https://i.imgur.com/tRvVsFa.png)

我們這次用 .net Core 來進行示範，並且用官方內建的 Web API 框架直接開場，所以這邊選擇 Asp.net Core Web API。

![img](https://i.imgur.com/lyjhWFS.png)

> 註：這些建立專案的畫面和選項隨著版本可能會有點不一樣，例如說可能會先選擇 .net Core 的 Web 服務之後，後續再勾選 API 的選項等等。例如之前的 [Asp.net MVC](https://igouist.github.io/post/2019/12/aspnet-connect-db) 文章中，就需要在選擇範本的時候選擇是 MVC 或 Web API 的範本。就麻煩各位再稍微見機行事一下。

![img](https://i.imgur.com/NCQj9Wf.png)

接著輸入專案名稱和選擇專案路徑，我在這邊採用 Newbie/Noob 的 N（而且 Project N 感覺很潮？），各位嘗試的時候可以自由取名，但要注意後續用到 `ProjectN` 這個名字的部分必須和你取的名字一致呦。

![img](https://i.imgur.com/Lbr3qkw.png)

這是紀錄採用的版本為長期支援的 .net Core 3.1（如果這個步驟有選擇其他版本的朋友，後續安裝套件的時候可能要注意一下版本相容性的問題）

建立之後我們的專案結構應該會長這樣：

![img](https://i.imgur.com/lGGHzDN.png)

恭喜各位，到這一步的時候，Web API 服務已經建好了！

~~直接用範本就是這麼爽，謝謝微軟把拔。~~

我們先來稍微認識一下環境設定相關的成員：

------

```
Properties/launchSettings.json
```

- 用來放我們偵錯專案時套用的環境設定，例如說我們偵錯的時候預設要打開哪個頁面（launchUrl）就是在這邊設定
- 可以參見 [launchSettings.json 的 commandName 是做什麼用的？](https://blog.poychang.net/visual-studio-launch-settings-iis-express-iis-project-executable/)

------

```
appsettings.json
```

- 用來放組態資料，像是連線字串、Log 的紀錄層級等等就會丟在這
- 以前用過 `web.config` 的朋友可能會比較熟。但在 .net Core 已經將不同職責的設定區塊拆分出去給
  `appsettings.json`、`.csproj` 等等，並且可以繫結強型別，所以更乾淨了。（感謝 Mike 和 [Sian](https://sunnyday0932.github.io/) 的說明）
- 關於兩者的差異和讀取 `appsettings.json` 的方法，可以參照余小章大大的這篇 [如何讀取 AppSettings.json 組態設定檔](https://dotblogs.com.tw/yc421206/2020/06/28/how_to_read_config_appsettings_json_via_net_core_31)

------

```
Startup.cs
```

- 設定服務的行為、註冊依賴注入相關的東西就丟在這，像之前註冊 [AutoMapper](https://igouist.github.io/post/2020/07/automapper) 服務的時候就是在這裡設定
- 我們後續還會常常過來找 Startup 玩

------

```
Program.cs
```

- 整個應用程式的進入點
- 關於服務啟動之後的順序和 `Program.cs`, `Startup.cs` 的內容，
  可以參照 [ASP.NET Core 2 系列 - 程式生命週期 (Application Lifetime) - John Wu’s Blog](https://blog.johnwu.cc/article/ironman-day02-asp-net-core-application-lifetime.html)

------

現在這個時間點，我們還不會對設定的部分動什麼手腳，只要對這些東西有個瞭解就好了。

我們把鏡頭轉到剛剛沒提到的其他檔案，可以看到還有 `WeatherForecast.cs` 和 `Controllers` 及裡面的 `WeatherForecastController.cs`。

> 補充一下，如果之前已經對 MVC 架構有點熟悉度的朋友，應該對 `Controller` 這個詞不陌生了。
>
> Web API 的範本其實也是同樣的概念，只是 `View` 的部分已經交給呼叫 Api 服務的使用者去處理了，而這邊的 `WeatherForecast.cs` 打開可以發現只是純粹的天氣資料，也就是個 `Model` 或 `ViewModel` 之類的東西。
>
> 至於 `Controller` 的職責仍然沒有什麼變化，就是個第一線的交通警察。所以先前做過 MVC 的朋友大概會覺得比較親近一些吧。大概。

這邊可以看到 `WeatherForecast.cs` 只是個用在 `WeatherForecastController` 的天氣資料類別。所以我們直接打開 `WeatherForecastController` 來觀察一下：

```csharp
[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    private static readonly string[] Summaries = new[]
    {
        "Freezing", "Bracing", "Chilly", "Cool", "Mild",
        "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

    private readonly ILogger<WeatherForecastController> _logger;

    public WeatherForecastController(ILogger<WeatherForecastController> logger)
    {
        _logger = logger;
    }

    [HttpGet]
    public IEnumerable<WeatherForecast> Get()
    {
        var rng = new Random();
        return Enumerable.Range(1, 5).Select(index => new WeatherForecast
        {
            Date = DateTime.Now.AddDays(index),
            TemperatureC = rng.Next(-20, 55),
            Summary = Summaries[rng.Next(Summaries.Length)]
        })
        .ToArray();
    }
}
```

首先在整個類別開始的地方加上了兩個屬性（Attribute）：`[ApiController]` 很明顯告訴我們這是個 Api Controller，而接著的 `[Route("[controller]")]` 用來決定我們這個 controller 的路由。

這邊要特別注意 `Route` 這個屬性，我們會在 Controller 和 Function 上用這個屬性來制定我們的 Api 的 URL，也就是我們前面 [Restful 小節](https://igouist.github.io/post/2021/05/newbie-2-webapi/#關於-restful-與-http-method) 提過的「用資源制定路由」要處理的部分。

現在可以看到 `Route` 的內容是 `[controller]`，所以會直接採用 controller 的名稱，在這邊也就會是 `/WeatherForecast/`。

如果有需要額外客製化路由的話，只要修改 `Route` 標籤就可以了，例如：改成 `Route("hello")` 的話，就會變成 `/hello/`；那如果我們接著在 Function 上掛上 `Route("world")` 的話，該方法的路由就會變成 `/hello/world/`，以此類推。

接著我們繼續往下看，可以看到放了一列不同的天氣 `string[] Summaries`，還有一些屬性與使用依賴注入的建構子範例 `WeatherForecastController()`，這個部份我們在後續的章節會再說明。

在建構式之後，我們會看到 `Get()` 方法，方法名稱並沒有什麼太大的關係，這邊要注意的重點在於：上面也掛了 `HttpGet` 的屬性，這個部份用來制定我們該方法所對應的 HTTP Method，也就是我們前面 [Restful 小節](https://igouist.github.io/post/2021/05/newbie-2-webapi/#關於-restful-與-http-method) 提過的「符合 HTTP 語意」所要處理的部分，例如 `GET`, `POST` 等等，就可以用 `[HttpGet]`, `[HttpPost]` 等屬性來標示。

最後這個 `Get()` 方法會隨機丟回天氣跟氣溫。現在就讓我們實際來呼叫看看吧！

> 備註：由於本系列還沒教到使用 Postman 或 Thunder client 這類直接呼叫 API 的方便小工具，所以呼叫的部分會使用瀏覽器或命令列進行示範，已經會使用這類工具的朋友可以用自己順手的工具嘗試就好囉。

現在讓我們直接執行看看：

![img](https://i.imgur.com/61SgLPf.png)

由於 `Properties/launchSettings.json` 裡有設定了 `launchUrl` 就是 `weatherforecast`，所以我們應該會直接看到它幫忙打開瀏覽器，並取得（`GET`）了 `https://localhost:{yourIISPort}/weatherforecast` 的結果：

![img](https://i.imgur.com/4jl7qvd.png)

> 小提示：如果瀏覽器打開沒有自動排版而是一整陀的朋友，可以先去裝個 [JsonView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) 來保護眼睛。安裝前後差異可以參見 [Json View —— 用 Chrome 打開 Json 的正確方式](https://igouist.github.io/post/2020/05/jsonview)

那如果是要用 Powershell 呼叫 API 的朋友，可以使用 `Invoke-RestMethod` 來進行呼叫，再用 `ConvertTo-Json` 轉換成比較好讀的格式，例如：`Invoke-RestMethod https://localhost:{yourIISPort}/weatherforecast | ConvertTo-Json`。注意 yourIISPort 這兒是你啟動後的 port 號，像是 `https://localhost:44304/weatherforecast`。

![img](https://i.imgur.com/QSp7VRr.png)

> 備註：Linux 的朋友就直接使用 Curl 來打就行了唄。另外，上面的 Powershell 語法特別感謝這篇 [使用 PowerShell 呼叫 Web API 請求](https://blog.poychang.net/using-powershell-call-http-request/)

到這邊我們就做完了簡單的認識，也確認我們新建的專案確實好好活著囉。

------

### 動手實作 CRUD

既然我們前面已經去逛過預設的 `WeatherForecastController` 了，現在就讓我們來自己建一個吧。

沒有脈絡就做不了事，先讓我們來訂一個情境：這是一個卡片對戰遊戲的卡片管理功能，一張卡片包含：卡片編號（ID）、卡片名稱和卡片敘述三個欄位。

因為我這個人喜歡整理、愛好整潔（？）這邊就先讓我們新增一個 `Models` 資料夾，用來存放卡片的類別

![img](https://i.imgur.com/Zoci28m.png)

建立 `Models` 資料夾之後，在 `Models` 裡面新增 `Card.cs`：

![img](https://i.imgur.com/EeAPqZv.png)

現在應該會是這個樣子：

![img](https://i.imgur.com/b6hcSaw.png)

接著讓我們打開 `Card.cs`，加上卡片的各個欄位：

```csharp
/// <summary>
/// 卡片
/// </summary>
public class Card
{
    /// <summary>
    /// 卡片編號
    /// </summary>
    public int Id { get; set; }

    /// <summary>
    /// 卡片名稱
    /// </summary>
    public string Name { get; set; }

    /// <summary>
    /// 卡片描述
    /// </summary>
    public string Description { get; set; }
}
```

完成卡片類別的建立之後，讓我們前往 `Controller`，新建一個 `CardController.cs`：

![img](https://i.imgur.com/XRbNmT4.png)

我們打開 `CardController.cs`。這個類別裡面現在應該是空空如也：

```csharp
public class CardController
{
    // 啥也沒有
}
```

接著我們就開始逐步施工吧（這邊的步驟可以去隔壁抄 `WeatherForecastController.cs` 也 OK 啦）

首先，我們要先繼承 `ControllerBase` 取得控制器該有的方法和成員。接著，我們要加上 `[ApiController]` 的屬性給這個類別，讓他知道他現在負責搞 API 了。

如果過程中跑出紅線的話，就按一下燈泡或用 `Alt + Enter` 把該 using 的東西給 using 進來。現在應該會像這樣：

```csharp
[ApiController]
public class CardController : ControllerBase
{
    // 啥也沒有
}
```

接著讓我們加上 `Route`，因為我們按照資源下去設計的話，`Route` 多半也是 `/card` 這樣子的路徑，因此我們繼續使用 `[Route("[controller]")]` 就可以了。如果各位要做的 API 資源在這邊需要客製化，再自己改成想要的字串即可。

```csharp
[ApiController]
[Route("[controller]")]
public class CardController : ControllerBase
{
    // 啥也沒有
}
```

這邊就讓我們先建立一個 `static` 並且為空的 `IEnumerable<Card>` 的私有成員，用來驗證我們後續開的功能是否可以正常運作

> 備註：我們會在下一個章節把這部分更改為連線資料庫去變更真正的資料，這邊就先用私有成員假裝一下唄。

```csharp
[ApiController]
[Route("[controller]")]
public class CardController : ControllerBase
{
    /// <summary>
    /// 測試用的資料集合
    /// </summary>
    private static List<Card> _cards = new List<Card>();
}
```

這樣事前工作已經準備完畢了，讓我們來加上操作方法吧！

首先先來一個查詢所有卡片的 Function，同樣用 `[HttpGet]` 來標明這是個 `GET` 方法，並且因為我們沒有特別指定路由，所以目前就是接著類別 `CardController` 的 `/card`，也就是 `GET /card`。

```csharp
/// <summary>
/// 查詢卡片列表
/// </summary>
/// <returns></returns>
[HttpGet]
public List<Card> GetList()
{
    return _cards;
}
```

然後讓我們加上一個單獨查詢單張卡片的方法：

```csharp
/// <summary>
/// 查詢卡片
/// </summary>
/// <param name="id">卡片編號</param>
/// <returns></returns>
[HttpGet]
[Route("{id}")]
public Card Get([FromRoute] int id)
{
    return _cards.FirstOrDefault(card => card.Id == id);
}
```

可以注意到我們用 `Route` 來指定了這個方法的 URL，並且用 `{id}` 的方式告訴 API 說這一格是參數 `int id` 所在的位置。

這樣的話這個方法的 Route 就會變成 `GET /card/1`（查詢 ID 為 1 的卡片） 這種感覺。實際使用的時候我們會很經常用 `{參數}` 這種方法來把參數加入到 Route 並制定 Function 對應的 URL，以此達到符合 Restful 的感覺。

另一個可以注意到的地方是我們在 Function 的參數上加上了 `[FromRoute]` 的屬性來告訴 API 說 `int id` 這個參數是來自於 Route 上的。

除了 `FromRoute` 以外，還有 `GET` 時很常用到的 `[FromQuery]` 或舊版本的 `[FromUri]`（指這個參數從 QueryString 也就是 ?a=1&b=2 那串裡面接收）、`POST` 和其他狀況常用到的 `[FromBody]`（指這個參數要從 Body 接收）等等，可以讓我們標明參數的來源。

> 補充說明一下，雖然也有簡單型別預設從 Uri，複雜型別預設從 Body 等等貼心的設定，但個人認為還是盡量都標明出來，對自己和後續維護的人都會比較好一點…。

接著讓我們加入新增卡片，還有編輯卡片的方法吧，在這之前我們先建立一個 `Parameter` 資料夾，用來放一些傳入的參數，並且新增一個 `CardParameter` 來當作我們新增和修改卡片的參數類別：

![img](https://i.imgur.com/fiqBwZM.png)

```csharp
/// <summary>
/// 卡片參數
/// </summary>
public class CardParameter
{
    /// <summary>
    /// 卡片名稱
    /// </summary>
    public string Name { get; set; }

    /// <summary>
    /// 卡片描述
    /// </summary>
    public string Description { get; set; }
}
```

> 補充：雖然也有建立一個對應的類別，接著就只使用這個類別的作法，像是先前的 [Asp.net MVC](https://igouist.github.io/post/2019/12/aspnet-connect-db/)，我們就只使用一個對應資料表欄位的類別來完成 CRUD 全部的操作。放到這裡來說的話，也就是只用 `Card` 類別，查詢也是用這個類別顯示，更新也是用這個類別當作參數。
>
> 但有些情況的時候，我們會希望傳進來新增或修改的參數跟類別並不一致，例如當我們新增 `Card` 的時候，並不需要 `Id` 這個欄位；又或是有些資料表中有 `CreateTime`、`UpdateTime` 這類程式自動填入、顯示的時候才有意義的欄位，就不會在新增或更新的時候對外開放；又或者是分層架構這類每一層要求的欄位並不一樣的情況等等。這些時候，我們就會採取將參數，也就是 `Parameter` 切分成一個單獨的類別進行管控。
>
> 基本上就像即使是同一張表，我們也會根據顯示的狀況來製作成不同的 `ViewModel` 一樣，我們也會根據傳入的狀況來決定 `Parameter` 的範圍。這個部份我們會在分層架構的時候再介紹一次，現在只要大致有可以把「顯示用類別」和「參數用類別」拆成不同的類別來進行出入口管制的概念就可以。

建立完參數之後，我們就可以回到 `CardController` 來加上新增和更新的方法：

```csharp
/// <summary>
/// 新增卡片
/// </summary>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPost]
public IActionResult Insert([FromBody] CardParameter parameter)
{
    _cards.Add(new Card
    {
        Id = _cards.Any() 
          ? _cards.Max(card => card.Id) + 1
          : 0, // 臨時防呆，如果沒東西就從 0 開始
        Name = parameter.Name,
        Description = parameter.Description
    });

    return Ok();
}

/// <summary>
/// 更新卡片
/// </summary>
/// <param name="id">卡片編號</param>
/// <param name="parameter">卡片參數</param>
/// <returns></returns>
[HttpPut]
[Route("{id}")]
public IActionResult Update(
    [FromRoute] int id,
    [FromBody] CardParameter parameter)
{
    var targetCard = _cards.FirstOrDefault(card => card.Id == id);
    if (targetCard is null)
    {
        return NotFound();
    }

    targetCard.Name = parameter.Name;
    targetCard.Description = parameter.Description;

    return Ok();
}
```

這邊的 `[HttpPost]`、`[HttpPut]` 以及 `[FromRpute]`、`[FromBody]` 我們在前面都已經掌握了。但在這裡我們還是可以看到 `return Ok()` 和 `return NotFound()` 這兩個新朋友。

聰明的朋友看 return 的方法名稱應該已經猜到了，這就是我們前面提過的 [HTTP Status](https://igouist.github.io/post/2021/05/newbie-2-webapi/#關於-http-status-code)。當然前面查詢成功的時候和這邊的 `Ok()` 一樣是 `200` 的狀態，此外還有代表 `400` 的 `BadRequest()`、代表 `404` 的 `NotFound()` 等等。

除此之外，我們也不是每次都會回傳 `IActionResult`，可能也會是自訂的錯誤型別等等，所以也看過使用 `Response.StatusCode` 來直接設定 Http Status Code 的做法，例如 `Response.StatusCode = 200;` 之後再進行回傳的做法，各位再視情況使用吧。

現在 CRUD 四大天王，我們已經只剩下 D 了，現在就來把刪除卡片的方法補上吧：

```csharp
/// <summary>
/// 刪除卡片
/// </summary>
/// <param name="id">卡片編號</param>
/// <returns></returns>
[HttpDelete]
[Route("{id}")]
public IActionResult Delete([FromRoute] int id)
{
    _cards.RemoveAll(card => card.Id == id);
    return Ok();
}
```

這樣四大天王（包含查詢列表通常是五個）就到齊了，現在的 `CardController` 應該是長這樣的：

```csharp
[ApiController]
[Route("[controller]")]
public class CardController : ControllerBase
{
    /// <summary>
    /// 測試用的資料集合
    /// </summary>
    private static List<Card> _cards = new List<Card>();

    /// <summary>
    /// 查詢卡片列表
    /// </summary>
    /// <returns></returns>
    [HttpGet]
    public List<Card> GetList()
    {
        return _cards;
    }

    /// <summary>
    /// 查詢卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <returns></returns>
    [HttpGet]
    [Route("{id}")]
    public Card Get([FromRoute] int id)
    {
        return _cards.FirstOrDefault(card => card.Id == id);
    }

    /// <summary>
    /// 新增卡片
    /// </summary>
    /// <param name="parameter">卡片參數</param>
    /// <returns></returns>
    [HttpPost]
    public IActionResult Insert([FromBody] CardParameter parameter)
    {
        _cards.Add(new Card
        {
            Id = _cards.Any() 
                ? _cards.Max(card => card.Id) + 1
                : 0, // 臨時防呆，如果沒東西就從 0 開始
            Name = parameter.Name,
            Description = parameter.Description
        });

        return Ok();
    }

    /// <summary>
    /// 更新卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <param name="parameter">卡片參數</param>
    /// <returns></returns>
    [HttpPut]
    [Route("{id}")]
    public IActionResult Update(
        [FromRoute] int id,
        [FromBody] CardParameter parameter)
    {
        var targetCard = _cards.FirstOrDefault(card => card.Id == id);
        if (targetCard is null)
        {
            return NotFound();
        }

        targetCard.Name = parameter.Name;
        targetCard.Description = parameter.Description;

        return Ok();
    }

    /// <summary>
    /// 刪除卡片
    /// </summary>
    /// <param name="id">卡片編號</param>
    /// <returns></returns>
    [HttpDelete]
    [Route("{id}")]
    public IActionResult Delete([FromRoute] int id)
    {
        _cards.RemoveAll(card => card.Id == id);
        return Ok();
    }
}
```

最後讓我們啟動來測試一下吧！

------

> 備註：和上面同樣地，因為這邊還沒說明到 Postman 等測試軟體，所以直接使用 Powershell 進行示範，已經有慣用軟體，或是直接寫一個腳本出來接的朋友，請用自己方便順手的測試方法去呼叫就好囉。

讓我們打開 Powershell，繼續使用 `Invoke-RestMethod` 來呼叫 API 試試看，別忘了 Port 要換成你啟動專案時 IIS 掛上去的 Port

首先讓我們新增一張卡片：

```powershell
Invoke-RestMethod https://localhost:44304/card `
 -Method 'POST' `
 -Headers @{ "Content-Type" = "application/json"; } `
 -Body "{`"name`": `"mycard`",`"description`": `"sample card`"}"
```

接著讓我們查詢看看所有卡片，看看新增的卡片在不在：

```powershell
Invoke-RestMethod https://localhost:44304/card | ConvertTo-Json
```

![img](https://i.imgur.com/IvHYdZR.png)

既然卡片已經存在了，讓我們試試看編輯，把「我的卡片」改成「我們的卡片」，~~打倒富農份子~~：

```powershell
Invoke-RestMethod https://localhost:44304/card/0 `
 -Method 'PUT' `
 -Headers @{ "Content-Type" = "application/json"; } `
 -Body "{`"name`": `"ourcard`",`"description`": `"sample card`"}"
```

並且用查詢單張卡片的方式來查詢卡片資料：

```powershell
Invoke-RestMethod https://localhost:44304/card/0 | ConvertTo-Json
```

![img](https://i.imgur.com/FjFHdSt.png)

如果編輯的卡片不存在，會噴出 404：

![img](https://i.imgur.com/j6Dom6l.png)

最後讓我們來試試刪除：

```powershell
Invoke-RestMethod https://localhost:44304/card/0 `
 -Method 'DELETE'
```

然後同樣使用查詢全部，應該要沒有任何卡片了：

```powershell
Invoke-RestMethod https://localhost:44304/card | ConvertTo-Json
```

![img](https://i.imgur.com/0WNEkAm.png)

到這邊就確認我們的 API 服務（也就是基本的 CRUD）已經 ON 起來啦！

------

## 小結

這邊我們紀錄了一些會用到的 HTTP 基礎知識，並用 Asp.net Core 的 Web API 範本新建了一個 API 服務，也加入了自己設定的 CRUD。

但要特別注意，雖然我們對外的開口已經建起來了，但這時候的 Card 還只是個用 static 變數假裝的空殼，只要站台重啟就會消失了。

正所謂「沒有連到資料庫的 CRUD，就像是沒有加醬汁的料理！」，我們在下一集就要來把我們的 Api 服務連接到資料庫啦！

那麼，我們下次見～

> 2021/5/8 補充：
>
> 範本預設的 `WeatherForecast.cs` 和 `WeatherForecastController` 在將來的文章將不會再用到，繼續下一篇實作之前可以先刪除囉～
>
> 有刪除的朋友記得要去 `launchSettings.json` 把 `launchUrl` 改成 card，下次啟動才會直接到我們這次新加的 CardController 呦！

> 本系列下一篇：[菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper)

## 本系列文章

- [菜雞新訓記 (0): 目錄](https://igouist.github.io/post/2021/04/newbie-0-menu)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git)
- [菜雞新訓記 (2): 認識 Api & 使用 .net Core 來建立簡單的 Web Api 服務吧](https://igouist.github.io/post/2021/05/newbie-2-webapi)
- [菜雞新訓記 (3): 使用 Dapper 來連線到資料庫 CRUD 吧](https://igouist.github.io/post/2021/05/newbie-3-dapper)
- [菜雞新訓記 (4): 使用 Swagger 來自動產生可互動的 API 文件吧](https://igouist.github.io/post/2021/05/newbie-4-swagger)
- [菜雞新訓記 (5): 使用 三層式架構 來切分服務的關注點和職責吧](https://igouist.github.io/post/2021/10/newbie-5-3-layer-architecture)
- [菜雞新訓記 (6): 使用 依賴注入 (Dependency Injection) 來解除強耦合吧](https://igouist.github.io/post/2021/11/newbie-6-dependency-injection)
- [菜雞新訓記 (7): 使用 FluentValidation 來驗證傳入參數吧](https://igouist.github.io/post/2022/03/newbie-7-fluent-validation)

## 參考資料

- [從傳紙條輕鬆學習基本網路概念 - huli](https://medium.com/@hulitw/learning-tcp-ip-http-via-sending-letter-5d3299203660)
- [從拉麵店的販賣機理解什麼是 API - huli](https://medium.com/@hulitw/ramen-and-api-6238437dc544)
- [API 到底是什麼？ 用白話文帶你認識 - BAR 主特調](https://medium.com/codingbar/api-到底是什麼-用白話文帶你認識-95f65a9cfc33)
- [Web API 設計 - Microsoft Docs](https://docs.microsoft.com/zh-tw/azure/architecture/best-practices/api-design)
- [休息(REST)式架構? 寧靜式(RESTful)的Web API是現在的潮流？ - 進度條](https://progressbar.tw/posts/53)
- [簡明 RESTful API 設計要點 - Twincl](https://tw.twincl.com/programming/*641y)
- [不做怎麼知道系列之Android開發者的30天後端養成故事 Day22 - 什麼是真正的 RESTful API? #RESTful API應該長什麼樣子?](https://ithelp.ithome.com.tw/articles/10230223)
- [dotnet Core WebApi實作-4 RESTful API介紹 _ Sian](https://sunnyday0932.github.io/2020/dotnet-core-webapi實作-4-restful-api介紹/)
- [CS #2 — 每每聽到工程師說 API，所以到底什麼是 API 啊？ - 萬事屋阿泰的知識海](https://medium.com/萬事屋阿泰的知識海/cs-2-每每聽到工程師說-api-所以到底什麼是-api-啊-b155662425e)
- [HTTP/1.1 — 訊息格式 (Message Format) - NotFalse](https://notfalse.net/39/http-message-format)
- [HTTP 前後端傳輸流程 - ttyy2985](https://medium.com/ttyy2985/http前後端傳輸流程-8ee40ffca1bd)
- [Postman 常見的 Content-type - hobo-engineer](https://medium.com/hobo-engineer/ricky筆記-postman-常見的-content-type-b17a75396668)
- [常見與不常見的 HTTP Status Code - Noob’s Space](https://noob.tw/http-status-code/)
- [網頁開發人員應了解的 HTTP 狀態碼 - The Will Will Web](https://blog.miniasp.com/post/2009/01/16/Web-developer-should-know-about-HTTP-Status-Code)
- [如何讀取 AppSettings.json 組態設定檔 - 余小章](https://dotblogs.com.tw/yc421206/2020/06/28/how_to_read_config_appsettings_json_via_net_core_31)
- [launchSettings.json 的 commandName 是做什麼用的？](https://blog.poychang.net/visual-studio-launch-settings-iis-express-iis-project-executable/)
- [ASP.NET Core 2 系列 - 程式生命週期 (Application Lifetime) - John Wu’s Blog](https://blog.johnwu.cc/article/ironman-day02-asp-net-core-application-lifetime.html)
- [使用 PowerShell 呼叫 Web API 請求](https://blog.poychang.net/using-powershell-call-http-request/)
- [超文本傳輸協定 - 維基百科](https://zh.wikipedia.org/wiki/超文本传输协议)

## 其他文章

- [菜雞新訓記 (0): 前言](https://igouist.github.io/post/2021/04/newbie-0-menu/)
- [菜雞新訓記 (1): 使用 Git 來進行版本控制吧](https://igouist.github.io/post/2021/04/newbie-1-hello-git/)
- [菜雞與物件導向 (Ex1): 小結](https://igouist.github.io/post/2021/01/oo-ex1-end2020/)
- [菜雞與物件導向 (15): 最少知識原則](https://igouist.github.io/post/2020/12/oo-15-least-knowledge-principle/)
- [菜雞與物件導向 (14): 依賴反轉原則](https://igouist.github.io/post/2020/12/oo-14-dependency-inversion-principle/)