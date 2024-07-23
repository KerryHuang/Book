# 【SOP製作教學】流程圖教學、重點範例、BPMN符號介紹！

## 本篇介紹SOP中的「流程圖製作」，除了流程圖範例、基本教學外，也會介紹BPMN的流程圖符號使用法，讓你輕鬆、快速學會標準的流程圖製作方法！



![img](https://miro.medium.com/v2/resize:fit:875/1*sTyxZkmbRljtrFPvgAz7sQ.jpeg)

[**【SOP製作教學】新手適用，SOP範例、流程圖、製作流程全公開！**](https://medium.com/doflowy/sop製作教學-新手適用-sop範例-流程圖-製作流程全公開-baaf6e90c578)，就有介紹到SOP的大致架構。這次我們將詳細說明怎樣畫出正確的流程圖，讓你可以更好的梳理SOP。

# 為什麼選擇BPMN的流程圖？

首先，我認為需要流程圖的原因，是因為我們的**思考通常是一步接著一步**，但**實務上的工作卻是很繁瑣、交錯並行、需要跨部門合作**的，所以才需要流程圖來幫助我們把複雜的工作梳理好。

而流程圖符號有很多派系，規則也會稍有不同，不過要表達的內容共通性是很高的，而我選的是「BPMN」這個派系的符號來製作流程圖範例。

會選擇BPMN，是因為它不僅能用在一般的行政業務流程，就連系統開發、API串接服務也很多共通性，再加上有官方機構認證，可說是正式且運用廣泛的體系，但同時也能是一個輕巧、適合新手的流程圖製作方法。

本文的流程圖範例，都是用免費線上軟體 [cawemo](https://cawemo.com/) 畫的，用於練習、新創公司的流程圖，我認為非常綽綽有餘！

```
BPMN(Business Process Model and Notation)是由一個國際組織OMG (Object Management Group)所創立的一個「企業流程模型標準」，以提供「企業流程圖的圖形化表示方法」。本次介紹會採用BPMN最新版本2011年發布的BPMN2.0來說明。不用擔心你使用其他派別，因為BPMN和其他派系要表達的內容很類似，只是符號和部分規則有一些變化罷了。另外，因為網路上太少繁體中文的翻譯，所以本篇的中文用法沒辦法非常正式，建議用英文來和其他內容對照。而每個類別都還有更細的分類、定義，因篇幅關係，都只會用最基本的方式說明，如果想要更精準的定義、圖示法，建議先讀完這系列之後，再用相關詞彙去找原文。BPMN官方英文手冊→https://www.omg.org/spec/BPMN/2.0/PDF
```

# 流程圖上的「起點與終點」

![img](https://miro.medium.com/v2/resize:fit:875/1*wKeUkCPXSPRdQtTe9nYViA.png)

上一回有提到，SOP要先定義範圍才不會無止盡地延伸，也就是流程上的「1.選擇情境」、「2.定義範圍」。而在這次的範例中，我把它們統一為「邊界」，也就是流程圖中的起點與終點。

例如：

- 起點－「接到瑕疵品客訴」
- 終點－「客人收到回覆」

兩者在BPMN裡都被歸類為事件（Event）分別為開始事件（Start event）、結束事件（End event）。「事件」是以空心圈圈的符號來表示。

![img](https://miro.medium.com/v2/resize:fit:1250/1*Mxt4LRQ0C0WUdaf2F7f7Uw.jpeg)

流程圖範例-開始、結束事件

「事件」代表著一種「狀態」，如果對一件事情的中文描述可以用「發生了」、「出現了」、「完成了」、「送達了」、「收到了」，在流程圖上就會被歸類為事件。

例如：「瑕疵品客訴出現了」、「產品製作完成了」、「貨物送達了」。

因此事件也常是一個訊號，代表在流程圖上，會有另外一件事要被觸發（收到消息，接著要做），所以也常說事件是一個觸發機制（Trigger）

```
▲ Event 事件
An Event is something that “happens” during the course of a Process or a　Choreography. These Events affect the flow of the model and usually have a cause (trigger) or an impact (result).
```

# 「執行任務」的流程圖表示法

![img](https://miro.medium.com/v2/resize:fit:875/1*-LY2xjhDuTFtpudTDPXg-A.png)

起點要到終點，中間會有很多事情要做，在BPMN中，只要你想在流程圖上表達「執行任務」、「做事情」、「從事工作」都是一種活動（Activity）。

例如：「確認訂單編號」、「說明處理方式」都可以是活動，在中文描述上會以「動詞+受詞（名詞）」的語句呈現。而活動（Activity）的符號則是長方形的框框。

．

我們不必太講究活動的大小，當一個活動不適合被拆解得更細，在BPMN流程圖中就會用任務（Task）以表達較小的活動，同時也是流程圖、各種範例文件中最常出現的圖案。

相對的，如果任務很大，不適合在當前的流程中展現細節，就會用子流程（Sub-Process）來表示。

![img](https://miro.medium.com/v2/resize:fit:1250/1*q3gb0_bcQM_rioPg3GVD1w.jpeg)

流程圖範例-任務、子流程

```
▲ Activity 活動
An Activity is a generic term for work that company performs in a Process. An Activity can be atomic or non-atomic(compound).▲ Task 任務
A Task is an atomic Activity that is included within a Process. A Task is used when the work in the Process is not broken down to a finer level of Process detail.▲ Sub-Process 子流程
A Sub-Process is a compound Activity that is included within a Process or Choreography. It is compound in that it can be broken down into a finer level of detail (a Process or Choreography) through a set of sub-Activities.
```

# 在流程圖上「區分單位」

![img](https://miro.medium.com/v2/resize:fit:875/1*Y2IzgUUxvsBFJe1cHoK0tw.png)

當任務（Task）是由不同單位執行、事件（Event）要觸發的對象也不同，在流程圖中則以用池（Pool）來區隔（例如不同人、部門、公司、職位）。

相對活動（Activity），池（Pool）裡面的單位則是參加者（Participant）。

例如，分別有「客服部門」、「維修部門」在執行任務時，則以大型的長方框符號，將所有該單位相關的物件都放進去。

![img](https://miro.medium.com/v2/resize:fit:1250/1*pxKdXGXJHEEeEAEsj-ztkA.jpeg)

流程圖範例-池、參與者

其中，當

1. 兩個單位緊密結合，但又需要表示他們的不同（如，同公司﹑不同部門）
2. 想要把相同部門，做更細部的區隔（如，同單位﹑不同職稱）

則可再把**池（Pool）**切分成**道（Lane）**

![img](https://miro.medium.com/v2/resize:fit:1250/1*414OytaY3xWNUIM6gsd-Yg.jpeg)

流程圖範例-池、道

規則上會是先有池（Pool）再分道（Lane），而怎樣的單位需要切分成池（Pool）、怎樣要成為道（Lane），則依據組織的特性而定，通常會看溝通的方便程度來區隔。
（池可以單獨存在；道需要在池內，並同時有2個以上）

```
▲ Pool　池
A Pool is the graphical representation of a Participant in a Collaboration. It also acts as a “Swimlane” and a graphical container for partitioning a set of Activities from other Pools, usually in the context of B2B situations. A Pool MAY have internal details, in the form of the Process that will be executed. Or a Pool MAY have no internal details, i.e., it can be a "black box."▲ Lane　道
A Lane is a sub-partition within a Pool and will extend the entire length of the Pool, either vertically or horizontally. Lanes are used to organize and categorize Activities.
```

# 將流程圖的「任務排序」

![img](https://miro.medium.com/v2/resize:fit:875/1*Sp_mchbtLhK7npV43EMigw.png)

最後終於來到重頭戲了，就是運用順序流（Sequence Flow）把流程圖上所有的事件、活動串聯起來，符號則是常見的線段加上箭頭。

順序流（Sequence Flow）表達的是流程的先、後關係，但只有在**同池**（Pool）內才可以用順序流，**跨池**則需要用訊息流（Message Flow）。

要理解也不難，就像部門內的事情，可以馬上請同事幫忙，但跨部門合作就需要比較正式的通知，這就屬於訊息流（Message Flow）。

．

另外，訊息流（Message Flow）的傳遞可以用任務（Task）來表示發訊息，如「發送信件」。相對的，對方也可以用「收取信件」的任務（Task）來表示收到訊息；當然也可以用事件（Event）來表達收到訊息。

串聯完畢後，流程圖就正式完成了！

![img](https://miro.medium.com/v2/resize:fit:1250/1*y8H8uV8-izGBAxHn7KRh-g.jpeg)

流程圖範例-順序流、訊息流

```
▲ Sequence Flow　順序流
A Sequence Flow is used to show the order that Activities will be performed in a Process and in a Choreography.▲ Message Flow　訊息流
A Message Flow is used to show the flow of Messages between two Participants that are prepared to send and receive them. In BPMN, two separate Pools in a Collaboration Diagram will represent the two Participants (e.g., PartnerEntities and/or PartnerRoles).
```

# BPMN2.0，流程圖符號大整理

目前為止，我們已經講了BPMN裡面四大類別，運用這些符號，只要熟練度高，就能很快速地用圖像化的方式，完成流程圖製作。

![img](https://miro.medium.com/v2/resize:fit:1250/1*a-Ufx9QBTs8BKoWZKcFRgA.png)

BPMN2.0流程圖符號整理

但其實還些事無法用這些符號來解決，像是「同步並行任務」、「有條件地執行任務」、「有條件地中斷任務」。

所以下一回，就要講到流程圖中能順利串起複雜流程的關口（Gateways），綜合運用後將能用簡易的符號，描繪出複雜的流程！