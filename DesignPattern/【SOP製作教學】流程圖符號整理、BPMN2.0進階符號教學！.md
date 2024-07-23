# 【SOP製作教學】流程圖符號整理、BPMN2.0進階符號教學！



## 本篇除了介紹BPMN2.0流程圖符號的進階用法，也會用流程圖來展示符號使用方法，並將流程圖符號整理給大家！



![img](https://miro.medium.com/v2/resize:fit:875/1*INaTDeCt_Fo0QgkmKAowEw.png)

## 【SOP製作教學】流程圖教學、重點範例、BPMN符號介紹！

### 本篇介紹SOP中的「流程圖製作」，除了流程圖範例、基本教學外，也會介紹BPMN的流程圖符號使用法，讓你輕鬆、快速學會標準的流程圖製作方法！

medium.com

在讀完前一篇文章後，相信你已具備畫出完整流程圖的能力了！

但是例如「同步並行任務」、「有條件地執行任務」是沒辦法用一般的流程圖符號畫出的，此時就要介紹到另外一個BPMN的重要符號：

> 「關口」（Gateway）

它是用空心的菱形符號表示，最大的用途是能**將流程分流或合併**，讓整個流程會「先經過判斷再決定做什麼」。

```
▲ 本篇是延伸技巧，因此都將直接針對符號來解釋與說明，不會畫出完整的流程圖。
```

## 唯一判斷符號－**排他關口（Exclusive Gateway）**

排他關口（Exclusive Gateway），表示流程會在此關口**分流**，而且**只能選擇一個順序流繼續走**，判斷的方式則會寫在順序流上，並且被依序判斷，如果符合，則執行該流向的活動，並且**停止判斷其他條路徑**。

它的符號，是在菱形的框框內加上「×」，或是不加任何符號保持空白。

![img](https://miro.medium.com/v2/resize:fit:1250/1*ge1TLb3bwtBMqJ8hDAklwA.png)

流程圖符號－排他關口（Exclusive Gateway）

如流程圖中展示，在排他關口（Exclusive Gateway）符號後的三條路徑，將會被由上而下地判斷，當符合判斷條件時，則會選擇該條路徑執行。

```
▲ 關口 Gateway
A Gateway is used to control the divergence and convergence of Sequence Flows in a Process and in a Choreography. Thus, it will determine branching, forking, merging, and joining of paths. Internal markers will indicate the type of behavior control.▲ 排他關口 Exclusive Gateway
A diverging Exclusive Gateway (Decision) is used to create alternative paths within a Process flow. This is basically
the “diversion point in the road” for a Process. For a given instance of the Process, only one of the paths can be taken.
```

## 多次判斷符號－包容關口（Inclusive Gateway）

包容關口 （Inclusive Gateway），則是判斷之後**雖會執行該路徑，但不會排擠其他的選擇**，也就是說可能每一條路徑都走，但也可能一條都不走。

它的符號，是在菱形的框框內加上「⚪」。

![img](https://miro.medium.com/v2/resize:fit:1250/1*H5MLFH_QLw4DeoemAFrmyw.png)

流程圖符號－包容關口（Inclusive Gateway）

上示流程圖中，當判斷為非瑕疵品時，會與客人說明瑕疵品的定義。

如果為一級瑕疵品時，則會發送維修申請。

但如是二級的瑕疵品，因為它同時滿足≥一級瑕疵品，也滿足≥二級瑕疵品，所以不但會發送維修申請，也會提供賠償。

在設計流程圖時，為了確保流程會持續進行，因此，只要使用包容關口（Inclusive Gateway）符號，都最好有一個預設路徑，或是至少有要能符合其中一個條件，不然有可能會莫名地中斷流程。

```
▲ 包容關口 Inclusive Gateway
A diverging Inclusive Gateway (Inclusive Decision) can be used to create alternative but also parallel paths within a Process flow.Unlike the Exclusive Gateway, all condition Expressions are evaluated. The true evaluation of one condition Expression does not exclude the evaluation of other condition Expressions. All Sequence Flows with a true evaluation will be traversed by a token. Since each path is considered to be independent, all combinations of the paths MAY be taken, from zero to all. However, it should be designed so that at least one path is taken.
```

## **流程圖的分流符號－並行關口（Parallel Gateway）**

並行關口（Parallel Gateway）不同於其他關口，它並不具備判斷功能，而是必須全部都做、全部滿足，它的用途就是純粹的分流、合併。

它的符號，是在菱形的框框內加上「+」。

![img](https://miro.medium.com/v2/resize:fit:1250/1*_cp_mpyIzNoeEEO8-y0Nag.png)

流程圖符號－並行關口（Parallel Gateway）

如圖中，就表示在確認訂單與產品後，就要同步並行「與客說明瑕疵品定義」、「發送檢修申請」、「發送維修申請」，三者缺一不可。

因此，並行關口（Parallel Gateway），也同時表達了這些活動沒有必須遵循的順序，是可以同時執行的。

並行關口（Parallel Gateway）還有合併的用途，也就是「只有三件事情都完成，才可以做下一步」。

```
▲ 並行關口 Parallel Gateway
A Parallel Gateway creates parallel paths without checking any conditions; each outgoing Sequence Flow receives a token upon execution of this Gateway. For incoming flows, the Parallel Gateway will wait for all incoming flows before triggering the flow through its outgoing Sequence Flows.
```

## **複雜流程的判斷－複雜關口（C**omplex **Gateway）**

複雜關口（Complex Gateway），則用於表達較為複雜的情況，它有和包容關口（Inclusive Gateway）類似的概念，也就是**只要條件符合就可以執行**。

通常，判斷較難在流程中呈現、需要額外說明、輔助文件時，就可以使用複雜關口。

它的符號，是在菱形的框框內加上類似「＊」圖案。

![img](https://miro.medium.com/v2/resize:fit:875/1*tIcxA7zUPnxIAhPM2UkAYw.png)

流程圖符號－複雜關口（Complex Gateway）

複雜關口 （Complex Gateway）也具備並行關口（Parallel Gateway）的合併特色，但它未必要所有條件滿足，可以只滿足部分條件。例如：

![img](https://miro.medium.com/v2/resize:fit:1250/1*Ie5gQjyhIw0A7sRUlYbmTg.png)

流程圖符號－複雜關口（Complex Gateway）

如上圖就是並行關口（Parallel Gateway）、複雜關口 （Complex Gateway）的綜合運用，它表達的是當客訴來的時候，就需要和客戶詢問4項資訊。

但電戶、帳戶名稱、收件地址只要有其中2項符合，再加上訂單與產品資訊，就可以執行下一步的維修申請。

也有一些其他的運用例子：

- 「３個面試官中有２位同意，即可讓面試者到下一階段」
- 「３種登入方法，只要其中一個成功，即可到達下一個畫面」

```
▲ 複雜關口 Complex Gateway
The Complex Gateway can be used to model complex synchronization behavior.
```

## 事件判斷符號－事件關口（Event-Based Gateway）

事件關口（Event-Based Gateway），雖然同樣有判斷性，但它的**判斷是來自於非流程內的項目，是以事件作為觸發點**（Trigger）。

它還具備了排他關口（Exclusive Gateway）的排他性，也就是**只執行一個路徑的項目**，但因為是以事件觸發，所以是「誰先發生，就做那一個」。

![img](https://miro.medium.com/v2/resize:fit:875/1*gkSyt3P0XgOmgD7N4qNPug.png)

流程圖符號－事件關口（Event-Based Gateway）

圖中的例子，表示當「接到同位客人的客訴」或「客訴兩天後」，才會開始處理客訴。

但如果先發生了「不同的客人、在兩天內，總共的客訴數量達到30筆」時，則是先召開部門大會，在開會之後，即便到了已經2天後，或是接到同一位客訴，也不會再回過頭處理。

另外，之前也提到過，因為事件和活動某種程度是可以互相替代的，因此「收到信件的事件」也可用「收取信件的活動」來表達。

```
▲ 事件關口（Event-Based Gateway）
The Event-Based Gateway represents a branching point in the Process where the alternative paths that follow the　Gateway are based on Events that occur, rather than the evaluation of Expressions using Process data (as with an　Exclusive or Inclusive Gateway).A specific Event, usually the receipt of a Message, determines the path that will　be taken. Basically, the decision is made by another　Participant, based on data that is not visible to Process, thus,　requiring the use of the Event-Based Gateway.
```

## 流程圖的事件（Event）延伸介紹

在第一篇介紹符號時，只說明了開始事件（Start event）、結束事件（End event），但事件關口（Event-Based Gateway）的事件卻不屬於這兩類，它屬於「流程中的事件」，也就是**中間事件（Intermediate Event）**。

所有夾在開始、結束之間的事件，都屬於中間事件（Intermediate Event）。隨著內建福號的不同，它還可以具備觸發、啟動的概念。

因此，就算沒有事件關口（Event-Based Gateway），中間事件（Intermediate Event）一樣可以獨立和其他活動一起運作，例如：

![img](https://miro.medium.com/v2/resize:fit:1250/1*k_woKSY4PgErhz0YNbsQQw.png)

流程圖符號－中間事件（Intermediate Event）

這個流程，基本上可以說是接到客訴的２天後，客服才會開始行動。

中間事件，它是用兩個細框的空心圈所組成。在圈圈內的符號，則是用來表達不同類型的中間事件，例如：

![img](https://miro.medium.com/v2/resize:fit:875/1*uXleswXQoqOHFeSeI1QgSg.png)

流程圖符號－事件特色

另外，事件除了以流程位置來定義的「開始、中間、結束」。還有以主被動來區分的**捕獲事件（Catching Event）**、**拋出事件（Throwing Event）**。

所謂**捕獲事件（Catching Event）**，代表著一種**被動的觸發機制**，也就是活動是「當會接獲某個消息、當某個情況發生後…」才要執行。因此，所有的開始事件（Start event）一定是一種捕獲事件（Catching Event），畢竟它是整個流程觸發的開關。

符號表示，是以白色為底的所有事件符號。我們在前面的舉例中，也都是以捕獲事件（Catching Event）作為例子。

反之，**拋出事件（Throwing Event）**代表隨著上一個活動完成，某個事件會隨之發生，有著**主動產生結果的意涵。**同樣地，結束事件（End event），則必定是一種拋出事件（Throwing Event）代表著在這個流程階段完成後，某件事情隨之發生（事情都做完了→結案發生、流程結束）。

通常有拋出事件（Throwing Event）時，也有捕獲事件（Catching Event）來呼應。它的符號，則是以黑色為底的所有事件符號。

以下就用實際的流程圖，舉幾個例子吧！

![img](https://miro.medium.com/v2/resize:fit:1250/1*NeZrSCHow4-wwZc6xMG5Zg.png)

流程圖符號－捕獲事件（Catching Event）、拋出事件（Throwing Event）

```
▲ 捕獲事件 Catching Event
Events that catch a trigger. All Start Events and some Intermediate Events are catching Events.▲ 拋出事件 Throwing Event
Events that throw a Result. All End Events and some Intermediate Events are throwing Events that MAY eventually be caught by another Event. Typically the trigger carries information out of the scope where the throw Event occurred into the scope of the catching Events. The throwing of a trigger MAY be either implicit as defined by this standard or an extension to it or explicit by a throw Event.
```

目前為止，已經說明了80%新手會用到的符號表示法，另外還有非常多進階用法、不同的圖示也很值得學習，在有了這些基礎後查資料會容易很多。

當然上述的說明有些是為了方便理解，因此並沒有非常精準、正確，也請大家多多包涵。

系列文到現在，大家都應該能做出很多份SOP文件、流程圖了，下一步則是要把這些流程串連、管理好，讓它們能更好地用於商場上，下一回將介紹的是基本的**ISO文件管理方法**。

```
按下「Follow」，追蹤我或我的專欄，將能定期收到優質的文章！
我會在系列完結時，製作統整表給有Follow的人喔！「1下」拍手：到此一遊，留個記錄吧。
「5下」拍手：表示喜歡這篇文章。
「15下」拍手：表示你想要知道更多相關的內容。
「50下」拍手：表示這篇文章對你非常實用！
```

## **※補充1：BPMN2.0 流程圖符號分類心智圖**

![img](https://miro.medium.com/v2/resize:fit:875/1*3GiKAcbcdHTkVCpvDeiHfw@2x.png)

# **※補充2：BPMN2.0流程圖中文符號整理**

BPMN2.0流程圖的中文符號說明Excel檔，會在本系列完結時，發送給所有Followers，有需要的話追蹤我即可！（下圖為部分精選符號）

## 流程圖符號整理 #1 事件（Event）

![img](https://miro.medium.com/v2/resize:fit:875/1*UYNVFoEWltYfM4COTo9ZKQ.png)

流程圖符號整理 #1 事件（Event）

## 流程圖符號整理 #2 活動（Activity）

![img](https://miro.medium.com/v2/resize:fit:875/1*xB4uISD8i_J6ELYYlzQTIA.png)

流程圖符號整理 #2 活動（Activity）

## 流程圖符號整理 #3 關口（Gateway）

![img](https://miro.medium.com/v2/resize:fit:804/1*RdUi4pb6FqleoGiEhnehlw.png)

流程圖符號整理 #3 關口（Gateway）