# 第7章 - [Redmine]專案版面的規劃

------

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220913/20151950lSdwThTt9d.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950lSdwThTt9d.png)

------

### 專案與父專案

在Redmine的平台中可以建立多專案，而專案的排序就是依照筆畫順序。

如果想針對專案進行分類呢?很可惜，目前Redmine的設計並沒有這樣的功能。

不過路不轉人轉，Redmine的專案設定可以有父專案的概念，我們可以用父專案的概念來建立我們需要的版面。

------

### 本篇將學習到Redmine的功能重點

- 專案的設定：父專案
- 專案的設定：專案是否公開及成員設定
- 專案的設定：使用模組的選擇

------

### 專案分類需求

我們依據在本系列第二篇「專案管理的概念及MIS應用」提出的分類來建立專案

#### (一)日常管理：MIS日常固定業務

- 資訊服務申請
- 定期報告
- ...

#### (二)異常管理：User的問題回報及處理

- 問題回報
- 異常紀錄及蒐集
- ....

#### (三)變革管理：指MIS負責執行的專案，例如新系統的導入、現有系統的優化等都是

- 建立新專案
- 專案進度控管
- ....

#### (四)ISMS管理：資訊安全管理系統的業務。ISMS年度工作計畫

- ISMS年度計畫
- ISMS文管中心
- ....

------

### 建立專案及分類

- 在建立新專案中，若只是分類使用，可以考慮將所有模組都選擇不勾選。(圖01)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950d880PSH7hD.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950d880PSH7hD.png)
- 建立第2層，直接選上層方類的[父專案]即可。(圖02)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950osfG6Xhvms.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950osfG6Xhvms.png)
- 建立完之後[專案清單]就會依照類別分類及排序。也可以建立第三層的子專案(圖03)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950lSdwThTt9d.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950lSdwThTt9d.png)

------

### 專案公開與成員設定

- 專案的設定中要注意是否要公開?若勾選[公開]，則不需登入就可以看到專案內容。若不勾選[公開]，則必須是專案成員登入後才會看到專案。
- [繼承父專案成員]若勾選，則專案成員與父專案一致。此處的設定邏輯可以多加利用，有利於專案分類的規劃。
  (圖04)
  ![https://ithelp.ithome.com.tw/upload/images/20220913/20151950tVPkqcUDFM.png](https://ithelp.ithome.com.tw/upload/images/20220913/20151950tVPkqcUDFM.png)

------

### 關於父專案看資訊的視野

本文因為重點在用父專案的方法來建立平台版面的分類，所以建議把所有模組都取消，所以若點選分類的父專案呈現頁面資訊很乾淨，預設只有[活動]會呈現紀錄資訊。(圖5)
![https://ithelp.ithome.com.tw/upload/images/20220915/20151950LmN9fDzVCl.png](https://ithelp.ithome.com.tw/upload/images/20220915/20151950LmN9fDzVCl.png)

不過這邊讓大家知道一下，若父專案的模組有打勾，無論是父專案(分類用專案)本身否有建立Issue資料，除了可以檢視到該專案的資訊外，統計上會包含子專案的相關資訊。包含議題的統計、耗用工時的統計、以及甘特圖等資訊，如以下幾張圖的範例。
需不需要就看管理者依本身的管理需求去決定。 (圖06、07、08)
![https://ithelp.ithome.com.tw/upload/images/20220915/20151950fBooOXcyX6.png](https://ithelp.ithome.com.tw/upload/images/20220915/20151950fBooOXcyX6.png)

![https://ithelp.ithome.com.tw/upload/images/20220915/201519508fJzz7j1sp.png](https://ithelp.ithome.com.tw/upload/images/20220915/201519508fJzz7j1sp.png)

![https://ithelp.ithome.com.tw/upload/images/20220915/20151950KvMMMWspzr.png](https://ithelp.ithome.com.tw/upload/images/20220915/20151950KvMMMWspzr.png)