想要快速開發一個 Bootstrap 網頁設計樣版的網站，可以利用網路上已經設計好的網頁樣版下載套用在自己的網站。
Bootstrap 提供非常好用的前端設計框架，包含 HTML, CSS 及 JavaScript 的模組可使用。
Bootstrap 支援 RWD 響應式網頁設計，依行動裝置及電腦桌面瀏覽器大小自動調整頁面。
想了解更多 Bootstrap 說明可至官網: [Bootstrap](https://getbootstrap.com/)

接下來我會介紹一款網路上免費的 Bootstrap 樣版: [SB Admin 2](https://startbootstrap.com/theme/sb-admin-2) 此樣版很適合做為管理介面使用。
樣版已經有基本美編視覺設計，專案開發時可以取得樣版上的樣式原始碼來使用。
這次的範例我會說明如何將 SB Admin 2 網頁樣版搬到 ASP.NET MVC 專案上，最下方有附上此次修改結果範例檔下載

##### 目錄

[1 下載 SB Admin 2 樣版](#Step1)
[2 建立 ASP.NET MVC 專案](#Step1)
[3 複製資源檔案](#Step1)
[3.1 複製 CSS](#Step1)
[3.2 複製 Javascript](#Step1)
[3.3 複製 Image](#Step1)
[4 修改佈局頁](#Step1)
[4.1 修改 CSS 引用來源](#Step1)
[4.2 修改 JavaScript 引用來源](#Step1)
[4.3 修改圖檔路徑](#Step1)
[4.4 修改內容區塊為 @RenderBody()](#Step1)
[5 修改首頁](#Step1)
[6 新增 Buttons 頁面](#Step1)
[6.1 建立Controller 頁面](#Step1)
[6.2 建立 View 頁面](#Step1)
[6.3 修改選單連結](#Step1)
[7 重點整理](#Step1)
[7.1 範例下載](#Step1)

<a name="Step1"/>
## 下載 SB Admin 2 樣版

![img1](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-1.jpg)
可以點左下角的「Live Preview」預覽網頁。
此樣版提供常用的選單、卡片、圖表、按鈕、進度條、登入、註冊等視覺設計。

點擊「Free Download」下載檔案，解壓縮可看到原始碼。
![Img2](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-2.jpg)

## 建立 ASP.NET MVC 專案
我新增一個範例專案，說明如何將 SB Admin 2 網頁增加至 ASP.NET MVC 專案裡面。
選擇 ASP.NET Web 應用程式 (.Net Framework)
![img3](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-3.jpg)

輸入專案名稱、路徑，按下建立
![img4](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-4.jpg)

專案類型選「MVC」
![img5](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-5.jpg)
按下「建立」專案就完成了

## 複製資源檔案

這裡我們要將下載 SB Admin 2 檔案裡面，資源檔(CSS, Javascript, Image) 放到專案裡面。

### 複製 CSS
專案目錄 \Content 先清空原有的檔案
將樣版檔案 startbootstrap-sb-admin-2-gh-pages\css 複製貼上至 \Content
![img6](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-6.jpg)

### 複製 Javascript
專案目錄 \Scripts 先清空原有檔案
將樣版檔案 startbootstrap-sb-admin-2-gh-pages\js 及 startbootstrap-sb-admin-2-gh-pages\vendor 複製貼上至 \Scripts
![img7](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-7.jpg)

### 複製 Image
將樣版檔案 startbootstrap-sb-admin-2-gh-pages\img 複製貼上至主目錄 \
![img8](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-8.jpg)
![img9](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-9.jpg)

## 修改佈局頁
佈局頁 (Views\Shared\_Layout.cshtml) 是設計網頁整體的樣式、排版及引用資源檔的頁面。
網頁設計常有固定式的標題、選單、註腳等設計，將固定式的設計放在佈局頁，就可以使每一頁都顯示，當要修改時也只需要修改一個地方即可。

將下載樣版頁的 index.html 全部內容複製到 _Layout.cshtml 裡面
![img10](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-10.jpg)

### 修改 CSS 引用來源
修改在 <head> 區的 CSS 引用來源，主目錄用 ~/ 代替。
```javascript
<!-- Custom fonts for this template-->
<link href="~/Scripts/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
	  rel="stylesheet">

<!-- Custom styles for this template-->
<link href="~/Content/sb-admin-2.min.css" rel="stylesheet">
```

所引用的檔案在上一步都要先放至專案目錄下才行喔。

### 修改 JavaScript 引用來源
修改在 <body> 最下面的引用部份，主目錄用 ~/ 代替。
```javascript
<!-- Bootstrap core JavaScript-->
<script src="~/Scripts/vendor/jquery/jquery.min.js"></script>
<script src="~/Scripts/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

<!-- Core plugin JavaScript-->
<script src="~/Scripts/vendor/jquery-easing/jquery.easing.min.js"></script>

<!-- Custom scripts for all pages-->
<script src="~/Scripts/js/sb-admin-2.min.js"></script>

<!-- Page level plugins -->
<script src="~/Scripts/vendor/chart.js/Chart.min.js"></script>

<!-- Page level custom scripts -->
<script src="~/Scripts/js/demo/chart-area-demo.js"></script>
<script src="~/Scripts/js/demo/chart-pie-demo.js"></script>
```
所引用的檔案在上一步都要先放至專案目錄下才行喔。

### 修改圖檔路徑
樣版上有使用到的圖檔路徑也需要修改，不然就會找不到圖片。

搜尋 「src="img/」 會找到所有使用圖檔，
將「src="img/」取代為「src="~/img/」
![img11](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-11.jpg)
這樣圖檔就會抓主目錄底下的 img 目錄圖檔。

### 修改內容區塊為 @RenderBody()
搜尋程式碼 「<div class="container-fluid">」，找到完整區段的程式碼(從 <div class="container-fluid"> 到結束的 </div>)
![img12](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-12.jpg)
將此段程式碼移除並換成 @RenderBody()
![img13](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-13.jpg)
註: @RenderBody() 指的是內容頁的語法將會放在這位置

## 修改首頁
Views\Home\Index.cshtml 是我們打開網站的首頁。
回到下載樣版頁的 index.html 找到 <div class="container-fluid"> 至結束 </div> 區段的程式碼複製再貼上至 Views\Home\Index.cshtml
![img14](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-14.jpg)
按 <F5> 運行網頁看一下首頁結果
![img15](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-15.jpg)
可以看到首頁已經完成了。

## 新增 Buttons 頁面
在下載樣版裡面有一個 buttons.html 頁，這裡展示的是各種按鈕的樣式。
![img16](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-16.jpg)
接下來我只示範一次如何增加內容頁，因為增加內容頁的動作都差不多，所以我只示範一個 Buttons 頁面就好。
實際上不太需要新增一樣的內容頁，樣版上的內容都是依需求而取出原始碼使用就好。

### 建立Controller 頁面
在 Controllers 按右鍵 > 加入 > 控制器
![img17](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-17.jpg)

輸入 Controller 名稱，需保留後面的 Controller 關鍵字。
![img18](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-18.jpg)
類型選 MVC 5 控制器，按「加入」。
![img19](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-19.jpg)

### 建立 View 頁面
在 Controller 內的 Index() 內按右鍵 -> 新增檢視。
![img20](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-20.jpg)
類型選 MVC 5 檢視，按「加入」
![img21](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-21.jpg)
要勾選「使用版面配置頁」就是使用剛剛的 _Layout.cshtml 為佈局頁。按「加入」。
![img22](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-22.jpg)
打開下載樣版的 buttons.html，找到 <div class=”container-fluid”> 至結束 </div> 區段的程式碼複製
![img23](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-23.jpg)
這裡複製的內容就是網頁上內容的部份。

再貼上至 Views\Buttons\Index.cshtml
![img24](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-24.jpg)
因為我們在上一步已經將網頁的佈局放在 _Layout.cshtml 裡面了，這裡只要複製內容貼上即可。

### 修改選單連結
打開 Views\Shared\_Layout.cshtml，搜尋「href=”buttons.html”」找到選單的連結。
將 「href=”buttons.html”」改為「href=”Buttons”」
![img25](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-25.jpg)
按 <F5> 運行網頁，然後將左邊選單打開 Components > Buttons 看一下結果
![img26](https://blog.hungwin.com.tw/wp-content/uploads/2021/05/asp.net-mvc-bootstrap-sb-admin-2-template-26.jpg)

Buttons 頁面已經完成了。
這次的範例完成了首頁及 Buttons 頁面。
做到這裡大概理解如何把 Bootstrap 的樣版搬到 ASP.NET MVC 上面了。
有了好看的樣版，就可以依此樣版繼續開發專案功能。

## 重點整理
1. SB Admin 2 很適合用在後台管理
2. 複製樣版資源到專案裡面
3. 佈局頁引用資源檔及顯示頁首頁尾
4. 內容頁只要貼上內容語法即可