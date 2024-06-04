# SSMS v18 清除登入畫面中，下拉選單歷史紀錄

SSMS v18 清除登入畫面中，下拉選單歷史紀錄
tags: MSSQL
PS: 以上是在 Windows 10 下操作進行，如果不同作業系統，有可能 UserSettings.xml 所在目錄不同，就請自行找找

假設想要刪除登入的帳號「IRSAuth」


按下 Win+R 輸入「appdata\Roaming\Microsoft\SQL Server Management Studio\18.0」,再按下 Enter，就會進到 C:\Users[使用者名稱]\AppData\Roaming\Microsoft\SQL Server Management Studio\18.0 的目錄下

編輯 UserSettings.xml 檔，搜尋IRSAuth，找到其所在區段，將<Element>與</Element>之間的內容刪除(含<Element>本身也要刪掉喔!)


這樣 IRSAuth 就不見囉！


清除特定伺服器名稱歷史清單：
方式與上面大致相同，以此類推，也就是搜尋想要刪除的伺服器IP位置，然後找到IP前面<ServerTypeItem><Servers>下的<Element>這層，將此<Element>與下方相對應的</Element>之間的所有內容刪除(含<Element>本身



Reference ：
Removing the remembered login and password list in SQL Server Management Studio