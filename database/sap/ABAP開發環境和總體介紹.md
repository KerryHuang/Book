---
kind: unknown
---

# ABAP開發環境和總體介紹

## 1. ABAP 開發環境 

ABAP開發的三種環境： 

（1）SAP正式系統環境； 

（2）SAP IDES系統環境（學習環境）； 

（3）MINISAP環境。 

三種環境中均含有大量的例子程序，事務代碼（TCODE）：Abapdocu。三種環境都能夠實現全部功能的ABAP開發（包括數據庫編程）。 

SAP正式環境含有業務功能並能進行開發，但正式環境需要經過較複雜的系統配置，才能使用業務功能。正式環境沒有任何業務數據。開發ABAP程序需要向SAP公司申請開發關鍵字。 

SAP IDES環境含有業務功能並能進行開發，而且含有一套完整演示數據，能直接使用各類業務功能，同時，對於例子程序，也有演示數據，能進行ABAP的真實業務程序開發。開發ABAP程序需要向SAP公司申請開發關鍵字。 

MINISAP沒有業務功能，只有開發和維護功能。對於例子程序，沒有演示數據。 

SAP正式環境和SAP IDES環境的後臺數據庫可以有很多種，如SQL SERVER，ORACLE等，需要很高的配置。而MINISAP需要的配置很低，需要使用Microsoft的MSDE數據庫（Microsoft SQL Server Desktop Engine）。 

關於IDES系統的安裝，本書在附錄中有較詳盡的指導。 

## 2. ABAP開發總體介紹 

在ABAP開發中,最主要的工作: 

（1） 報表的開發，主要使用到數據庫讀取、ALV、LIST等技術； 

（2） 單據的打印，主要使用到數據庫讀取、SmartForms、Form等技術； 

（3） 數據的上載，主要使用到數據庫存取、CATT、BDC等技術。 

主要ABAP相關技術見表1-1。  

表1-1 

| 簡稱           | 描述                   | 備註       |
| -------------- | ---------------------- | ---------- |
| Internal Table | 內表處理               |            |
| CATT           | 計算機輔助測試工具     | SCAT       |
| BDC            | 批量數據處理程序       | SHDB等     |
| List           | 數據列表，報表輸出使用 |            |
| Selection      | 數據選擇               |            |
| Screen         | 屏幕設計               | SE51       |
| Menu           | 菜單繪製器             | SE41       |
| Form           | 單據打印               | SE71       |
| SmartForms     | 單據打印               | SmartForms |
| Query          | 簡單查詢               | SQ01       |
| BAPI           | API接口                | BAPI       |
| ALV            | SAP List Viewer        |            |
| ALV Tree       | ALV分類彙總            |            |
| Table Control  | Screen相關             |            |
| Excel處理      | 讀入和存出             |            |
| UserExit       | 用戶出口               | CMOD，SMOD |
| Tree Control   | Tree 控件              |            |
| 數據字典       | 數據字典               | SE11       |
| 邏輯庫         | 邏輯庫                 | SE36       |
| 權限           | 用戶權限管理（BASIS）  | PFCG       |
| 測試跟蹤       | SQL跟蹤                | ST05       |
| 授權           | 授權及權限檢測         | SU21、SU20 |
| LSMW           | 數據導入工具           | LSMW       |

常用TCODE及描述見表1-2。 

表1-2 

| TCODE      | 描述                                 | 備註     |
| ---------- | ------------------------------------ | -------- |
| ABAPDOCU   | ABAP文檔和範例                       |          |
| BAPI       | BAPI瀏覽器                           |          |
| CMOD/SMOD  | 系統增強                             |          |
| LSMW       | 數據導入工具                         | 數據導入 |
| PFCG       | 權限管理                             |          |
| SA38       | 程序執行                             |          |
| SCAT       | 計算機輔助測試工具，測試，數據導入等 | 數據導入 |
| SCC1       | 集團拷貝                             |          |
| SCC4       | 顯示集團                             |          |
| SE09       | 運輸組織者，查詢傳輸請求             |          |
| SE11       | 數據字典                             |          |
| SE16       | 數據瀏覽器                           |          |
| SE32       | 文本元素設定                         |          |
| SE36       | 邏輯數據器                           |          |
| SE37       | 函數模塊                             |          |
| SE38       | ABAP編輯器                           |          |
| SE41       | 菜單製作器                           |          |
| SE51       | 屏幕製作器                           |          |
| SE55       | 生成表維護程序                       |          |
| SE71       | Form設計                             | 單據打印 |
| SE78       | Form、SmartForms使用圖片上載         |          |
| SE80       | 對象瀏覽器                           |          |
| SE90       | 對象瀏覽器                           |          |
| SE91       | 消息設定                             |          |
| SE93       | 維護事務代碼                         |          |
| SHDB       | 批輸入代碼                           | 數據導入 |
| SM04       | 顯示在線用戶                         |          |
| SM30       | 維護表視圖                           |          |
| SM35       | 批次輸入監控                             |          |
| SM50       | 進程監控                             |          |
| SMARTFORMS | SmartForms設計                       | 單據打印 |
| SNUM       | 編號對象維護                         |          |
| SO10       | 標準文本，設定Form使用的TIFF圖片等   |          |
| SPAD       | 假脫機管理                           |          |
| SQ01       | Query查詢製作                        |          |
| ST05       | SQL跟蹤                              |          |
| SU20       | 授權字段                             | 授權     |
| SU21       | 授權對象                             | 授權     |
| WE21       | IDOC處理中的端口                     | IDOC     |