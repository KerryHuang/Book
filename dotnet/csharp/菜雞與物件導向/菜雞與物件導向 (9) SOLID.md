---
kind: reprint
source: https://igouist.github.io/post/2020/09/oo-9-solid
author: igouist
---

# 菜雞與物件導向 (9): SOLID



![img](https://i.imgur.com/U7iWMT9.png)

終於進入了原則篇，接下來的幾篇我們會介紹幾個物件導向的原則（基本上就是指 SOLID 原則）。因此這篇就讓我 水一下 當成後半段的目錄，方便之後可以把相關的部分整理進來。

## 為什麼我們需要這些原則？

我們在前面的章節已經說明了一些物件導向的特性，例如繼承和多型等等。然而我們並沒有討論到怎麼運用、或是怎樣設計才能算是更好的、更優雅的、更符合物件導向精神的；我們並沒有提到一個評估的標準，或是指引一個更好的方向。

然而，混亂的使用物件導向對整個專案的毀滅性甚至比乾脆不使用物件導向還高。

這些特性使用起來很簡單，大多數語言只需要一個符號或標示就能完成繼承，把一堆東西全部塞在一起就可以說我在封裝。但怎麼使用得好，又該什麼時候使用呢？這就是難的地方吧。

例如說濫用繼承，或是封裝時完全不隱藏複雜度一路 Puuuuublic 到底，又或者是類別之間過於相互依賴，全部耦合成一團等等。如果隨便地使用物件導向的各項特性，就會讓整個架構變得僵化、脆弱、危險、充滿臭味。

更可怕的是，這個發臭的過程是每一次設計、每一次修改都會有所影響，所謂「持續發生，腐敗成真」，隨著物件導向的亂用、誤用、無腦用，軟體就會逐漸腐化。一組腐化的軟體可能會有以下特徵：大量的依賴使得修改變得困難、修改後看似不相干的各個地方發生問題、或是修改時沒辦法依循原本的設計、到處出現不必要的複雜性和不必要的重複，模組也變得難以理解等等。

阻止程式碼的腐化、追求更好的架構和設計、寫出更好的代碼，當然是我輩所追求的目標。儘管面對的可能是不同的問題和不同的環境，那些優質、穩固、具有反脆弱特質的程式碼也必然會有些共通之處。例如說：需要具有面對改變的能力、具有方便管理的能力、具有隱藏複雜性的能力。

因此，大前輩們整理並提出了一些可以致力的方向，也就是所謂的「原則」。如同心法、教義一般，只要實作的同時將其牢記在心，就能讓我們作為一些行動的準則和依據。

所謂練拳不練功，到老一場空。我們可不能看了招式就無腦用，先讓我們看一下這些 SOLID 原則的目標是什麼。

在 [Clean Architecture](https://www.books.com.tw/products/0010786994) 裡是這樣說明的：

> 這些原則的目標是建立中層級的軟體結構，這樣的結構包含：
>
> - 能容忍變化
> - 容易理解
> - 在許多軟體系統中能夠使用的元件的基礎
>
> 「中層級」是指這些原則是程式設計師在模組層級工作時應用的原則。它們應用在程式碼層級之上，並且有助於定義模組和元件內使用的軟體結構類型。

我們應用這些原則的場景，應該是在所謂的「中層級」發生。也就是並非小到一行程式碼，也並非是一整個專案，而是其中的各個「模組」。不論是類別、介面又或是其他名稱的任何東西，凡是具有函式或資料的中層級，我們就可以運用這些原則來處理。

而我們之所以要用這些原則，就是為了達到 能容忍變化、容易理解、能讓模組和元件使用 這些目標。

這些目標可以當作一個良好的程式碼模組該有的特徵。你的類別必須能容忍變化，必須具備可擴展性和可修改性，畢竟軟體的需求大多時候都是擴展跟修改。更進一步說，功能和彈性之間甚至應該先選擇彈性，畢竟為了功能犧牲彈性的話，一但面對變化，整個程式就碎了；但優先選擇彈性的話，至少你還有機會能把它修改得更符合功能，所以對這些原則而言，能容忍變化是相當重要的。甚至，整個 SOLID 就是面對變化的作戰策略。

而容易理解就更重要了。Clean Code 裡有提過，閱讀程式碼和實際開工打字的時間大約是佔 10 : 1，因此是否容易理解，是否乾淨好懂就是相當重要的一環。看得快，就寫得快；寫得越快，心越慢。

如同我們在首篇所說，物件導向就是在替我們把概念抽象化，而這抽象過程所使用的這些特性，就是為了減少複雜性、提高可理解度而存在的。因此，一組優良的程式碼，容易理解是絕對必要的。

另外關於為什麼我們需要這些原則，我個人推薦可以先閱讀這幾篇，對我個人來說很有收穫：

- [淺談物件導向 SOLID 原則對工程師的好處與如何影響能力 - WadeHuang的學習迷航記](https://wadehuanglearning.blogspot.com/2019/10/solid.html)
- [再談 SOLID 原則，Why SOLID? - WadeHuang的學習迷航記](https://wadehuanglearning.blogspot.com/2019/10/solid-why-solid.html)
- [SOLID：五則皆變 - 搞笑談軟工](http://teddy-chen-tw.blogspot.com/2014/04/solid.html)

## 說那麼多，所以到底有哪些原則？

現在我們已經了解到，因為軟體會逐漸腐化，所以我們要找出原則；這些原則的目標，就在於設計出可變化可理解的優質模組。現在，是時候公布我們 SOLID 五大天王的名諱了：

- 單一職責原則 Single Responsibility Principle (SRP)
- 開放封閉原則 Open-Closed Principle (OCP)
- 里氏替換原則 Liskov Substitution Principle (LSP)
- 介面隔離原則 Interface Segregation Principle (ISP)
- 依賴反轉原則 Dependency Inversion Principle (DIP)

> 註：大多時候 L 的位置也會多一個 Law of Demeter 迪米特法則（= Least Knowledge Principle 最少知識原則），畢竟也挺重要的，而且四大天王都有五個人了，五大原則有六個也是剛剛好。

而它們的首字合起來就是 `SOLID`，表達出那種穩固的、可靠的感覺！順便一提，順序沒有任何關係，會排成 SOLID 純粹只是作者朋友當時覺得這樣比較好記。

那麼從[下一篇](https://igouist.github.io/post/2020/10/oo-10-single-responsibility-principle)開始，我們就按照 SOLID 的順序，從單一職責開始介紹。我們下次見～

> 本系列下一篇：[菜雞與物件導向 (10): 單一職責原則](https://igouist.github.io/post/2020/10/oo-10-single-responsibility-principle)

## 參考資料

- [淺談物件導向 SOLID 原則對工程師的好處與如何影響能力 - WadeHuang的學習迷航記](https://wadehuanglearning.blogspot.com/2019/10/solid.html)
- [再談 SOLID 原則，Why SOLID? - WadeHuang的學習迷航記](https://wadehuanglearning.blogspot.com/2019/10/solid-why-solid.html)
- [SOLID：五則皆變 - 搞笑談軟工](http://teddy-chen-tw.blogspot.com/2014/04/solid.html)
- [使人瘋狂的 SOLID 原則：目錄 - YC](https://medium.com/@ChunYeung/使人瘋狂的-solid-原則-目錄-b33fdfc983ca)
- [我該學會SOLID嗎? - Finn](https://medium.com/@f40507777/我該學會solid嗎-4e73887c9156)
- [物件導向武功秘笈（3）：內功篇 — 物件導向指導原則SOLID - YC Chen](https://www.ycc.idv.tw/introduction-object-oriented-programming_3.html)
- [Fred 聊聊 SOLID 設計原則](https://youtu.be/e0UOuQ_lCUY)
- [第 1 章 無瑕的程式碼 | Clean Code - 手寫筆記](https://medium.com/手寫筆記/clean-code-b45a89ea8c66)
- [《無瑕的程式碼：整潔的軟體設計與架構篇》](https://www.books.com.tw/products/0010786994)

## 同系列文章

- [菜雞與物件導向 (0): 前言](https://igouist.github.io/post/2020/07/oo-0-object-oriented)
- [菜雞與物件導向 (1): 類別、物件](https://igouist.github.io/post/2020/07/oo-1-class-object)
- [菜雞與物件導向 (2): 建構式、多載](https://igouist.github.io/post/2020/07/oo-2-constructor-overload)
- [菜雞與物件導向 (3): 封裝](https://igouist.github.io/post/2020/07/oo-3-encapsulation)
- [菜雞與物件導向 (4): 繼承](https://igouist.github.io/post/2020/07/oo-4-inheritance)
- [菜雞與物件導向 (5): 多型](https://igouist.github.io/post/2020/07/oo-5-polymorphism)
- [菜雞與物件導向 (6): 抽象、覆寫](https://igouist.github.io/post/2020/07/oo-6-abstract-override)
- [菜雞與物件導向 (7): 介面](https://igouist.github.io/post/2020/07/oo-7-interface)
- [菜雞與物件導向 (8): 內聚、耦合](https://igouist.github.io/post/2020/09/oo-8-cohesion-and-coupling)
- [菜雞與物件導向 (9): SOLID](https://igouist.github.io/post/2020/09/oo-9-solid)
- [菜雞與物件導向 (10): 單一職責原則](https://igouist.github.io/post/2020/10/oo-10-single-responsibility-principle)
- [菜雞與物件導向 (11): 開放封閉原則](https://igouist.github.io/post/2020/10/oo-11-open-closed-principle)
- [菜雞與物件導向 (12): 里氏替換原則](https://igouist.github.io/post/2020/11/oo-12-liskov-substitution-principle)
- [菜雞與物件導向 (13): 介面隔離原則](https://igouist.github.io/post/2020/11/oo-13-interface-segregation-principle)
- [菜雞與物件導向 (14): 依賴反轉原則](https://igouist.github.io/post/2020/12/oo-14-dependency-inversion-principle)
- [菜雞與物件導向 (15): 最少知識原則](https://igouist.github.io/post/2020/12/oo-15-least-knowledge-principle)
- [菜雞與物件導向 (Ex1): 小結](https://igouist.github.io/post/2021/01/oo-ex1-end2020)

## 其他文章

- [菜雞與物件導向 (8): 內聚、耦合](https://igouist.github.io/post/2020/09/oo-8-cohesion-and-coupling/)
- [菜雞與物件導向 (7): 介面](https://igouist.github.io/post/2020/07/oo-7-interface/)
- [菜雞與物件導向 (6): 抽象、覆寫](https://igouist.github.io/post/2020/07/oo-6-abstract-override/)
- [菜雞與物件導向 (5): 多型](https://igouist.github.io/post/2020/07/oo-5-polymorphism/)
- [菜雞與物件導向 (4): 繼承](https://igouist.github.io/post/2020/07/oo-4-inheritance/)