將 Windows Forms 專案打包成安裝檔，是發佈給更多使用者執行比較好的方法。
可控制安裝目錄檔案，保留舊版本使用者設定檔，也可以避免使用者個人電腦環境的差異，造成程式無法執行。

在過去我要將程式丟給客戶執行的時候，比較方便快速的方法是將 \Debug 裡面的所有檔案壓縮打包給客戶，客戶再解壓縮後去執行裡面的執行檔。

可是隨著專案慢慢變複雜，程式裡面多了一些使用者設定檔，當客戶每次取得新檔案後，都要重新設定一次，造成客戶時間的浪費。

如果改用安裝檔的方法，將專案打包成「setup.exe」安裝檔給客戶安裝，就可以保留客戶電腦上的使用者設定檔。

如果所開發的專案將來是公開給更多人下載使用時，建立安裝檔再放至網路上給所有人下載，也是最好的方式。

接下來我會分享如何在 Visual Studio 2019 建立 Windows Forms App 專案的程式安裝檔。

### 目錄
[建立測試專案](#Step1)


### 建立測試專案
這裡我新建一個 Windows Forms App (.NET Framework) 的專案來測試。
![img1](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-1.png)
測試專案名稱為 “WinFormSetup”。
![img2](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-2.png)


### 安裝 Installer Projects
VS 的安裝檔模組功能是需要另外下載的，下載連結：VS2017, VS2019，VS2022 。
或是在 VS 的功能列上開啟「延伸模組 > 管理延伸模組」。
![img3](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-3.png)
搜尋「Installer Project」，找到「Microsoft Visual Studio Installer Projects」，點擊「下載」。
![img4](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-4.png)
下載後需要關閉 Visual Studio 才會執行安裝。
![img5](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-5.png)
安裝完成。
![img6](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-6.png)

### 安裝檔專案設定
#### 加入 Setup Project 專案
重新開啟專案後，在「解決方案」按右鍵選「加入 > 新增專案」。
![img7](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-7.png)
在上方搜尋「Setup Project」，找到「Setup Project」專案加入。
![img8](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-8.png)
輸入專案名稱。
![img9](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-9.png)
加入專案後，在主畫面上會出現 3 種安裝檔目錄內容。
![img10](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-10.png)
Application Folder: 安裝完成後會新增到使用者電腦裡的檔案。
User’s Desktop: 安裝後會新增至使用者桌面的檔案。
User’s Programs Menu: 安裝後會新增至使用者程式集的檔案。

#### 加入專案輸出
在「Application Folder」按右鍵選「Add > 專案輸出」。
![img11](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-11.png)
選擇要輸出的專案，再點擊「主要輸出」。
![img12](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-12.png)
會出現 Windows Forms 專案輸出的執行檔及必要 .dll。
![img13](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-13.png)

#### 建立使用者桌面捷徑
點左邊的目錄「User’s Desktop」，在右邊的內容按右鍵選「建立新捷徑」。
![img14](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-14.png)
選「Application Folder」。
![img15](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-15.png)
再選擇「主要輸出」。
![img16](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-16.png)
建立好的捷徑再更換捷徑名稱，按右鍵選「重新命名」修改即可。
![img17](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-17.png)
建議改跟專案名稱一樣，這是會出現在使用者桌面上的名稱。
![img18](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-18.png)
要修改捷徑圖示，就按右鍵選「屬性視窗」。
![img19](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-19-1.png)
在「icon」選擇「(Browse)」，接著再選擇 .ico 的圖檔就行。
![img20](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-20.png)
在選擇 .ico 圖檔時，要一起將圖示放在「Application Folder」目錄裡面，可以按「Add File」，將 .ico圖檔放進來。
![img21](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-21.png)

#### 建立使用者程式集捷徑
在左邊點「User’s Programs Menu」，在右邊空白處按右鍵選「建立新捷徑」。
![img22](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-22.png)
接下來作法跟建立桌面捷徑一樣，這裡我就貼出完成後的畫面。
![img23](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-23.png)


### 設定安裝專案屬性
點擊安裝檔專案的屬性，可以調整安裝設定。
可以依圖示內說明，調整正式發佈的專案描述。
![img24](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-24.png)


### 輸出安裝檔
一切設定完後，在專案按右鍵選「建置」，VS 會建立此安裝檔。
![img25](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-25.png)
建置後，在專案底下的「\Debug」目錄就會出現安裝檔。
![img26](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-26.png)
執行安裝。
![img27](https://blog.hungwin.com.tw/wp-content/uploads/2021/09/visual-studio-2019-winform-setup-27.png)
安裝後就會在桌面或程式集上面出現捷徑，執行後會開啟你的 Windows Forms 執行檔。


### 重點整理
* 將 WinForm 打包成安裝檔，是發佈程式最好的方式
* 安裝 Installer Projects 模組來建立專案
* 加入 Setup Project 專案來設定安裝檔
* 加入專案輸出，將執行檔放至安裝包裡面
* 建立捷徑方便執行
* 專案建置後輸出 Setup.exe 安裝檔
