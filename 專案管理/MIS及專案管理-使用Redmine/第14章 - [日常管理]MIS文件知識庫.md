# 第14章 - [日常管理]MIS文件知識庫

---

## 本篇預期成果畫面

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950nQ6UE4v3Ne.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950nQ6UE4v3Ne.png)

------

### 管理議題

![/images/emoticon/emoticon56.gif](https://ithelp.ithome.com.tw/images/emoticon/emoticon56.gif) ***檔案在哪裡？***

- MIS的文件在哪?
- MIS的合約檔案在哪?
- 資訊管理程序書最後一版是哪一版?

![/images/emoticon/emoticon56.gif](https://ithelp.ithome.com.tw/images/emoticon/emoticon56.gif)***檔案要分享要放在哪裡?***

- 放到X槽?哪個路徑?
- 用Mail?哪一天的Mail?

![/images/emoticon/emoticon56.gif](https://ithelp.ithome.com.tw/images/emoticon/emoticon56.gif)***MIS內部有沒有比較好的方式知識討論及分享?***

- Line群組? 但如何公司分開? 如何留下之前交換的訊息?
- 有沒有適合部門內同仁針對特定主題的討論、分享，並可以留下紀錄當成MIS知識庫的?

![/images/emoticon/emoticon28.gif](https://ithelp.ithome.com.tw/images/emoticon/emoticon28.gif)
其實KM是老議題，而且可以選擇的工具多如牛毛，也不是甚麼新鮮話題。
既然我們選擇了Redmine當部門的管理平台，就用Redmine的系統功能建立屬於MIS部門的文件知識庫。

------

### 本篇將學習到Redmine的功能重點

- 文件
- 檔案清單
- 新聞
- 論壇
- 舊的Redmine知識回顧
  - 模組的設定：請參考系列文Day 7-[[Redmine\]專案版面的規劃](https://ithelp.ithome.com.tw/articles/10290131)
  - 自訂欄位清單：請參考系列文Day 6-[[Redmine\]自行建立及維護表單](https://ithelp.ithome.com.tw/articles/10289889)
  - 專案建立基本邏輯：請參考系列文Day 5-[[Redmine\]Redime系統邏輯說明](https://ithelp.ithome.com.tw/articles/10289859)
  - 其餘本文有完成功能但沒做進行詳細畫面說明的：請參考系列Day 8開始的每篇文章的「本篇將學習到Redmine的功能重點」。每篇分享文都有當篇文章要新學習的Redmine某項功能的應用及設定方法的示範重點。
- 觀念交流：**知識庫，不該是X槽**(本文最後)

------

### 管理資訊需求

- 【需求名稱】：MIS文件知識庫
- 【權限需求】：MIS同仁有權限閱讀及更新
- 【適用場合】：MIS所有文件及知識交流
- 【模組需求】：
  - (X)議題追蹤
  - (X)工時追蹤
  - (O)新聞
  - (O)文件
  - (O)檔案
  - (O)Wiki
  - (O)版本控管
  - (O)討論區
  - (X)日曆
  - (X)甘特圖

------

### 專案設定

先建立一個新專案，把不需要用到的模組取消選取，並在[概述]中說明主要的用途。
圖01、02
![https://ithelp.ithome.com.tw/upload/images/20220917/20151950Re39yDqxI4.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950Re39yDqxI4.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950DUk5rje42a.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950DUk5rje42a.png)

------

### 文件

- 預設的文件分類需要修改一下
- [文件]/[分類]
  圖03、04、05、06
  ![https://ithelp.ithome.com.tw/upload/images/20220917/20151950e3rTi4BHjA.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950e3rTi4BHjA.png)
- [網站管理]/[列舉值清單]/[文件分類]：我們直接用修改及新增的方式建立我們需要的文件分類：
  - 操作手冊
  - 廠商合約
  - 公文存檔
  - 文件歸檔

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950IGoY88yfKs.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950IGoY88yfKs.png)

- 文件分類設定完成後，就可以在[文件]中，建立文件歸檔的清單

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950Xo3QdSecuV.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950Xo3QdSecuV.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950v2IBiEu00q.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950v2IBiEu00q.png)

------

### 檔案清單

- 檔案清單是可上傳不分類的檔案，可作為檔案下載的用途，例如空白申請單
  圖07、08
  ![https://ithelp.ithome.com.tw/upload/images/20220917/20151950onRzsSf7HY.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950onRzsSf7HY.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950UriNtBN4Sq.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950UriNtBN4Sq.png)

------

### 新聞

- [新聞]其實比較像最新消息，PO完之後會呈現在首頁。
- 當然也可以作為知識文件的分享。
  (圖09、10)
  ![https://ithelp.ithome.com.tw/upload/images/20220917/20151950GsrhJ5pAda.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950GsrhJ5pAda.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950cu7sMhuImI.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950cu7sMhuImI.png)

- 新聞會呈現在首頁，可以當最新消息使用(部門公告會重要是發佈) (圖11)
  ![https://ithelp.ithome.com.tw/upload/images/20220917/20151950nQ6UE4v3Ne.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950nQ6UE4v3Ne.png)

------

### 論壇

- 論壇要先設定：[設定]/[論壇]
  圖12、13、14

![https://ithelp.ithome.com.tw/upload/images/20220917/20151950SbQKfSQFrI.png](https://ithelp.ithome.com.tw/upload/images/20220917/20151950SbQKfSQFrI.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/201519505QwsZvqfGz.png](https://ithelp.ithome.com.tw/upload/images/20220917/201519505QwsZvqfGz.png)

![https://ithelp.ithome.com.tw/upload/images/20220917/201519504IFCDSF0iN.png](https://ithelp.ithome.com.tw/upload/images/20220917/201519504IFCDSF0iN.png)

------

### 知識庫，不該是X槽

- 知識要經過分類。
- 知識要經過編碼。
- 知識要經過機密等級及被授權使用的概念，機密的資料不該輕易被移動到公共資料開放區。
- 知識要有專人在管理。

以上都不是X槽做得到的!

很多公司有X槽。

所謂的X槽，其實就是讓同仁可以放資料、交換資料的磁碟空間。有可能是File Server，可能是NAS，使用網路磁碟設定的方式依公司權限、部門權限、專案權限在網路磁碟存取公共資料夾。

從我個人的角度，X槽就是一個大型垃圾場的集合：

- 網路磁碟的檔案數量只會無限制地長大，而且重複、沒用的的資我估計至少60%，而且MIS還得天天備份這60%的垃圾。
- 網路磁碟的權限設計無法對有權限的人員的去追查存取紀錄
- 網路磁碟任意交換，不經意未被授權的人也可以看到資料，是公司營業秘密洩漏及資安一個大漏洞
- 有些中小企業公司的總務特別喜歡在網路磁碟中放一個Excel請人員填寫那些不是太重要也不是機密的的行政申請，例如加班的便當登記、交通車登記...很原始的作業模式，只因X槽的Excel最方便作業。
- X槽最怕有權限的胖手指事件，尤其是高權限的MIS網管人員...結果會很慘!

好啦，我只是想說，知識庫就應該透過系統管理才叫知識庫。

Redmine是專案管理平台，並不是一個KM平台。但本系列文章是想要用Redmine建立MIS部門的管理平台，所以這邊講的是一個管理的概念，Redmine也提供文件管理基本需要的管理功能。

很容易使用，就，參考參考囉!
