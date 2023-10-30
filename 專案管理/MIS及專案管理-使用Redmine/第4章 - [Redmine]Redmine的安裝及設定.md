# 第4章 - [Redmine]Redmine的安裝及設定

------

Redmine 不僅跨平台更是跨資料庫，因此我們可以很容易的安裝在各種不同的平台之上：

### 作業系統

- Unix
- Linux
- macOS
- Windows

### 支援之資料庫

- MySQL
- MariaDB
- PostgreSQL
- SQLServer
- SQLite

### 安裝的方式

安裝 Redmine 有非常多種方式可以選擇，可以選擇一步一步安裝，也可以下載預先打包好的 LXC 範本檔、Docker 容器檔加速上線試用。

過去說到Redmine的缺點，相信很多人的共識就是它在安裝和管理上並不容易，不過近年已有一鍵安裝(Bitnami Redmine Stack)、虛擬機器(Virtual Machine)或是容器(Dokcer)的安裝方式，也算是越來越便利了。

以下就用Bitnami Redmine Stack的方式，在Windows 10或Windows Server來建置 Redmine 的應用服務。

------

### 下載及安裝Redmine

(圖01)

- 安裝下載：https://bitnami.com/stack/redmine/installer
- 2023/5/1筆者更新：發現官網的一鍵更新連結頁面沒了，只剩VM包，故將直接下載連結提供如下：https://downloads.bitnami.com/files/stacks/redmine/5.0.2-1/bitnami-redmine-5.0.2-1-windows-x64-installer.exe
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950ITRweEYul8.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950ITRweEYul8.png)
- 選擇你要安裝的作業系統。本文件預計安裝於Windows 10的作業系統。(圖02、03、04)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950MTfSQZPMuS.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950MTfSQZPMuS.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950lFgaFhLyUJ.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950lFgaFhLyUJ.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950wZ0CPO7bUm.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950wZ0CPO7bUm.png)
- 執行安裝：選擇安裝的語言。(圖05、06)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950QeMZw3tli8.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950QeMZw3tli8.png)

![https://ithelp.ithome.com.tw/upload/images/20220911/20151950gH3XB1vvwZ.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950gH3XB1vvwZ.png)

- 請勾選安裝所有元件。(圖07)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950W5aI5ccJJN.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950W5aI5ccJJN.png)
- 選擇安裝的路徑、安裝後登入的帳號資訊及預設的資料語言(建議安裝時選英文，安裝後可以再設定為中文)(圖08、09、10)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950Pj0KgzexBC.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950Pj0KgzexBC.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950SoTEBW0dbZ.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950SoTEBW0dbZ.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950g3HyMYkaao.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950g3HyMYkaao.png)
- SMTP我們先跳過，安裝後再進行SMTP設定。(圖11)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/201519501HVcbeRGdY.png](https://ithelp.ithome.com.tw/upload/images/20220911/201519501HVcbeRGdY.png)
- 這個不要選。(圖12)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950FdjOTg3G9g.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950FdjOTg3G9g.png)
- 按NEXT就開始安裝了。(圖13、14)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950UTg4j5Ryuw.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950UTg4j5Ryuw.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/201519509748ddfz3t.png](https://ithelp.ithome.com.tw/upload/images/20220911/201519509748ddfz3t.png)
- 請耐心等候。筆者本次安裝從21:14按下Next後，21:46安裝完成，
- 若安裝過程出現防火牆封鎖Apache，請按【允許存取】(圖15)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/201519502lYBIFstzm.png](https://ithelp.ithome.com.tw/upload/images/20220911/201519502lYBIFstzm.png)
- 完成安裝(圖16、17、18)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950eP2r9DtPSn.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950eP2r9DtPSn.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950K8CHyVIH73.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950K8CHyVIH73.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950LTloxnakfm.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950LTloxnakfm.png)

------

### 第一次登入

- 在瀏覽器輸入[http://127.0.0.1](http://127.0.0.1/) ，在頁按面[Access Redmine ]，即進入Redmine的首頁。
  (預設網址為 http://127.0.0.1/redmine/ ) (圖19、20、21、22)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950lILBFYljCI.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950lILBFYljCI.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950WKAYgPH5ug.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950WKAYgPH5ug.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950ROrkx3tx7e.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950ROrkx3tx7e.png)
- 用安裝時設定的帳號密碼進入登入安裝好的Redmine，並進行相關設定。(圖20、21)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950gRQd45IO32.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950gRQd45IO32.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950AiNIyu2snL.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950AiNIyu2snL.png)
- 第一次登入可能是英文版，可進行相關設定。(圖22)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/201519505GHoY1i4YA.png](https://ithelp.ithome.com.tw/upload/images/20220911/201519505GHoY1i4YA.png)
- 設定登入後的預設語言
- 請按[Administrator]/[Settings]/[Display]/[Default Language] (圖23、24、25、26)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950WlKh1hkrj8.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950WlKh1hkrj8.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950NFTTlNhVqk.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950NFTTlNhVqk.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950Rr8MkkdKkC.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950Rr8MkkdKkC.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950rQF2jA8jM5.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950rQF2jA8jM5.png)
- 按[Save]後，也請設定一下你目前登入帳號的預設語言
- 右上角的[My account]/[language]，選完後按[Save]，介面立即變更成你所設定的語言。(圖27、28)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950kpSWGZMeVC.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950kpSWGZMeVC.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950ShxvBxxpSO.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950ShxvBxxpSO.png)
- 設定網站首頁標題(圖29)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/201519509xJRplW2VR.png](https://ithelp.ithome.com.tw/upload/images/20220911/201519509xJRplW2VR.png)
- [網站管理]/[設定]/[一般]/[標題]及[歡迎詞]，完成後按[儲存] (圖30、31)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950m7kOVsGSgq.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950m7kOVsGSgq.png)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950ippYKMpJ3f.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950ippYKMpJ3f.png)
- 完成後按一下[網站首頁]，首頁資訊變更了 (圖32)
  ![https://ithelp.ithome.com.tw/upload/images/20220911/20151950HtF9ReBGPS.png](https://ithelp.ithome.com.tw/upload/images/20220911/20151950HtF9ReBGPS.png)

------

以上完成Redmine的安裝及基本設定，是不是很簡單?