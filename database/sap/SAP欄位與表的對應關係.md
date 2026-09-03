---
kind: unknown
---

# SAP欄位與表的對應關係

MASTER DATA－主資料

Customer Master

KNA1 Customer Basic Data

KNB1 Customer Company Level Data客戶的公司資料

KNVV Customer Sales Level Data 客戶的銷售資料

KNVP Customer Partnering Data客戶合作伙伴

KNKA Customer Credit Data - Centralized

KNKK Customer Credit Data - Control Area Level

KNBK Customer Bank Details

KNVH Customer Hierarchies

KNVL Customer Licenses

KNMT Customer - Material Info Record，客戶-物料資訊記錄資料表

KNMTK Customer - Material Info Record - Header

KNVK 聯絡人(供應商，客戶)

Material Master

MARA Material Basic Data(物料型別,)

MARC Material MRP (Plant) Data(工廠的MRP檢視)

MARD Material Storage Data (檢視總庫存)（物料的倉儲位置資料）

MARDH Material Storege Data His. 檢視庫存的歷史庫存（月度的庫存）

MARM 物料計量單位

MBEW Material Valuation Data(檢視財務檢視-)成本價格) 沒有工廠欄位，但有評估範圍欄位；

MKAL Material Production Version Data(生產版本)

MAKT Material Descriptions/Short Texts(物料描述)

MARM Material Units of Measure(物料主單位的轉換數量)

MVKE Material Sales Level Data （銷售檢視）

MSKU Special Stocks with Customer ( 客戶寄售庫存 )

MLGN Material Warehouse Data

MVKE Material Sales Data

MTXH Material Long Text

MCHA Batch management table（批次管理）

MCHB 批次庫存

MSKA SalesOrder Stock（銷售庫存）

MAPL 分配任務清單到物料，物料所建的工藝路線（Q型別為檢驗計劃）

MAST 分配BOM到物料

MVKE 物料銷售資料(查詢銷售單位)

MLAN 物料的稅分類

MDLV 定製 MRP 執行區域(與MDLG是明細) MRP範圍

MDLG

MDMA 物料與MRP AREA的關聯關係；

T023 物料組

T023T

Vendor Master 供應商

LFA1 Vendor Master – General Data

LFB1 Vendor Master – Company Code Data（公司，財務檢視）

LFM1 Vendor Master – Purchasing Org. Data(採購組織)

LFB5 Vendor Master – Dunning Data

LFBK Vendor Master – Bank Details((銀行資訊)-àBNKA銀行表

LFBW Vendor Master – Withholding Tax Types

LFC1 Vendor Master – Transaction Figures

LFM2 Vendor Master – Purchasing Data

LFMC Vendor Master – Condition Type Short Text

LFMH Vendor Hierarchy

KNVK 聯絡人(供應商，客戶)

WYT3 合夥人資訊；

PP MASTER DATA (cont.)

Factory Calendar

TFACD Factory Calendar Definition

TFACS Factory Calendar Display (days/month)

TFACT Factory Calendar Texts

TFAIN Factory Calendar – Special Rules

TFAIT Text for Factory Calendar Intervals

THOC Public Holiday Calendar ID’s

THOCD Public Holiday Link to Holiday Calendar

THOL Public Holiday Definition

THOLT Public Holiday Texts

Line Design

LDLH Line Hierarchy Header

LDLP Line Hierarchy Items

LDLT Line Hierarchy Takt Times

LDLBC Takts/No. Individual Capacities per Line

LDLBH Line Balance Header

LDLBP Line Balance Items

LDLBT Line Hierarchy Entry and Exit Takts

PRT’s

CRFH PRT Master Data

CRVD\_A Link of PRT to Document

CRVD\_B Link of Document to PRT

CRVE\_A Assignment of PRT data to Equipment

CRVE\_B Assignment of equipment to PRT data

CRVM\_A Link of PRT data to Material

CRVM\_B Link of Material to PRT data

CRVS\_A Link of PRT Internal number to PRT External number

CRVS\_B Link of PRT External number to PRT Internal number

Class & Characteristic

CABN, "Characteristic

RMCLM. "Classification

(PP) PRODUCTION PLANNING

Work Center

CRHD Work Center Header Data

CRCA Work Center Capacity Allocation

CRCO Work Center Cost Center Assignment(通過物件號與CRHD關聯)包含了作業型別

CRHH Hierarchy Header

CRHS Hierarchy Structure

CRTX Work Center Text(工作中心描述)

KAKO Capacity Header

KAZY Intervals of Capacity

CRC 邏輯資料庫

ROUTING

MAPL Routing Link to Material(查到工藝路線的產品描述，物料、組號、組計數器之間的關係)

PLPO Routing OperationDetails（通過PLPO的ARBID和CRHD的OBJECTID關聯獲得具體使用哪個工作中心，標準值也在這個表格裡儲存）

PLKO Routing Header Details（需要與MAPL關聯，PLNTY，PLNNR）

PLAB Relationships - Standard Network

PLAS Task List - Selection ofOperations（PLPO,PLAS,PLKO三者互相關聯才能獲得工作中心描述資訊）

(plpo~~plnnr = plas~~plnnr and plpo~~zaehl = plas~~zaehl andplpo~~plnkn = plas~~plnkn)

PLMZ Component Allocation（元件分配）（是記錄分配BOM到ROUTING）

PLPH CAPP Sub-operations

PLFH PRT Allocation

PLWP Maintenance Package Allocation

PLMK Inspection Characteristics

T435T 工藝路線標準文字

PNM 邏輯資料庫

BOM (物料清單)

STPO BOM Item Details(明細項)

STKO BOM Header Details(擡頭項) （找STAS->再找STOP，這是由於STOP中無可選項欄位）

MAST BOM Group to Material（通過【物料單】欄位與STPO、STKO關聯）

STZU BOM History Records

STAS BOM Item Selection（有可選項欄位）

STPF BOM Explosion Structure

MAST 分配BOM到物料

BOM 使用邏輯資料庫的是CMC

ProductionVersion(生產版本)

MKAL Material Production Version Data (生產版本)

Demand Management

PBED Independent Requirements Data

PBIM Independent Requirements by Material（與PBED通過BDZEI關聯）

PBHI Independent Requirements History（與PBIM，通過BDZEI關聯）

PBID Plannedindependent requirements index: MRP area

Repetitive Manufacturing

SAFK RS Header Master Data

S025 LIS – Run Schedule Quantities

S026 LIS – Material Usage

S028 LIS – Reporting Point Statistics

BLPK 憑證日誌標題（儲存了【參考數量】）沖銷型別----P，在這裡通過【處理型別】來查詢相關的報告點的操作，報告點的處理型別為Z。

CEZP Reporting Point Document Logs（行專案）

CPZP Reporting Points – Periodic Totals(產看某期間的報告點)物件號與AFKO訂單號關聯；

MRP Records

MDKP MRP Document Header Data

MDKPDB

PLSC Planning Scenario (Long-term Planning)

MDFD MRP Firming Dates(涉及到長期計劃中的計劃方案)

MDVM Planning File Entries

S094 LIS – Stock/Requirements Analysis(動態生成)

MDTB MD04/MD05介面的資料表 DTNUM，只是一份計劃條目清單；

UMD01 儲存MRP的介面引數

Reservations

RKPF Reservations Header

RESB Reservations/Dependent Requirements（保留相關的溯源）

Planned Orders

PLAF Planned Orders

OPIT 計劃訂單排程記錄

T457P 計劃訂單中訂單型別的文字表格

T460C 計劃訂單的訂單/採購訂單型別

T460D 計劃訂單的訂單/採購訂單型別

DPM 計劃訂單邏輯資料庫

Discrete Production（生產訂單）

從CAUFV找AUFRL

AFKO OrderHeader（包含有BOM和ROUTING的組資訊）(工序確認,上級訂單號)(不要關聯該表的物料號，經常會丟失。如果關聯則關聯AFPO)

AFPO Order Item Detail(訂單類別【DAUTY】－5產品收集器，訂單型別【DAUAT】－RM01，有入庫數【WEMNG】)

RESB OrderBOM（訂單裡的實際BOM清單，通過AUFPL與AFVC關聯，包含了訂單的元件分配）

AFFL Order Sequence Details

AFFH Order PRT Assignment

AFBP Order Batch Print Requests

AFVC Order Operations Detail (與通過“組”和“計數器”關聯AFKO，應該是AUFPL \[訂單中工序的工藝路線號] 與AFKO關聯)（訂單裡的實際工序）

ARBID—資源的物件ID

AFRU Order Completion Confirmations（實際值）

(生產訂單確認量及所有相關的確認的資料（重複製造），物件號與CRCO查詢作業類新描述，通過訂單號和AFPO關聯)得到計劃工藝路線號，然後和AFVC關聯(訂單號，作業編號)，再通過AFVC的活動型別到表CSLA獲得具體成本要素號;\[AFRU的訂單＆作業與AFVC相關聯]

AFFW Confirmations – Goods Movements withErrors（COGI錯誤庫存列表）

AFRC Confirmations – Incorrect CostCalculations(COGI) 確認不正確的成本核算

AFRD Confirmations – Defaults for CollectiveConfirmation

AFRH Confirmations – Header Info for ConfirmationPool

AUFM 儲存訂單的貨物移動內容（只儲存DAUTY-10，也就是儲存有生產訂單，重複製造的內容不放在該表）

AFVV Operationdetails（生產訂單的定額－標準值/理論值）

AFRV Confirmation Pool

AFWI Confirmations – Subsequently Posted GoodsMovements(確認的物料移動)

AUFK 訂單主資料(包含訂單的刪除標誌)（有PP與CO的訂單號的對照表，也就是包含了“OR0000….”）

CKMLMV001 儲存了，按照物料＋版本號，找到生產過程號，然後通過AUFK生產過程號。

CKMLMV013 儲存了訂單和生產版本的資訊；一般來說，一個訂單AUFNR就是一個版本VERID；

AUFK->JEST->TJ02T Orderstatus(通過AUFK OBJNR關聯) for example:OR000002014014

\->JSTO 查詢到相應的訂單狀態(具體

TJ02T 具體描述相應的狀態：

系統狀態

語言

狀態

狀態

I0001

E

CRTD

Created

I0002

E

REL

Released

I0009

E

CNF

Confirmed

I0010

E

PCNF

Partially confirmed

I0012

E

DLV

Delivered

I0013

E

DLT

Deletion indicator

I0045

E

TECO

Technically completed

I0046

E

CLSD

Closed(取消，清空)

TJ02T SYSTEM STATUS

JEST,JSTO PO STATUS(

TJ30 USERSTATUS

JCDO ChangeDocuments for Status Object (Table)

JCDS ChangeDocuments for System/User Statuses

COBRB 結算規則表

Classification

KLAH Class Detail

CABN Characteristic Detail

AUSP Characteristic Values

CAWN Characteristic Values

CAWNT Characteristic Value Texts

KSML Characteristic Allocation to Class

KSSK Material Allocation to Class

（QM）Quality Management

主資料

檢驗批

檢驗結果

QADB\_SCOPE Scope from ASAP QADB

QAES 取樣單位表

QAKL 數值分類的結果表

QALS 檢驗批記錄（檢視檢驗批的狀態：。。。。）

QALT 部分批量

QAMB QM：檢驗批和物料憑證的連線(參考型別－，STAT35－代表有結論；STAT34－Q庫存釋放是否完全釋放

QAMR 檢驗處理中的特性結果

QAMV 檢驗處理的特性說明

QAMVRMS 多重說明的檢驗說明/評估

QAOBJMS 多個說明 - 物件

QAPP 檢驗點

QASE 取樣單元的結果表

QASH 控制圖表

QASR 檢驗特性的取樣結果

QASRMS 多重說明樣品的確認資料

QAST 控制圖表跟蹤

QASV 檢驗處理的取樣說明

QAVE 檢驗處理：使用決策（取得檢驗批的結果，識別符號KZART＝L，UD程式碼＝P003）

QPMK 主檢驗特性

(MM) MATERIALS MANAGEMENT

Master Data

EINA Purchasing Info Record – General Data（採購資訊記錄）

EINE Purchasing Info Record – Purchasing Org. Data(採購資訊記錄-採購檢視)；與EINA是一對多的；

EQUK Quota Arrangement Header(配額)

EQUP Quota Arrangement Item Detail

EORD Source Lists 貨源清單

KOMV Header Conditions（通訊表）

KONP Item Conditions（通訊表）， A017是採購價格的資料表，然後通過欄位KNUMH；A017不能用於QUERY；

T024 採購組 邏輯資料表：IFM-採購資訊記錄；

邏輯資料庫：ILM----可以顯示採購價格等級資料

T001L 庫存地點

Purchasing

PO

EKKO Purchasing DocumentHeader詢報價(憑證型別＝A)；採購合同(憑證型別＝K)

EKPO Purchasing Document Item Detail

EKBE 採購訂單歷史

EBAN 採購申請（行專案）

EBKN 採購申請

BAM 採購申請邏輯資料庫

EKET 採購訂單delivery schedule

EKES 採購訂單與內向交貨單的關係；

S011 LIS – Purchasing Groups

S012 LIS – Purchasing

S013 LIS – Vendor Evaluation

S080 LIS – Purchasing - Movements

S081 LIS – Purchasing - Stock

S082 LIS – Purchasing - Movements & Stock

EKBZ (發票校驗和採購訂單關聯的表)

審批表

採購訂單的審批 CEKKO

採購申請 CEBAN

Batch Management

MCHA Batches

S038 LIS – Inventory Controlling - Batches

Inventory Management

MSLB Special Stocks with Vendor供應商特殊庫存(外協，委外)

MSKU Special Stocks with Customer

IKPF Physical Inventory Header(盤點憑證)

ISEG Physical Inventory Document Item Detail

S032 LIS – Statistics Table - Current Stocks

S039 LIS – Inventory Controlling

MSKA Sales Order Stock

MCHA 批次庫存

MCHB 批次庫存

Material Documents

MKPF Material Document Header

MSEG Material Document Item Detail

Warehouse Management

LTAK Transfer Order Header

LTAP Transfer Order Item Detail

LTBK Transfer Requirement Header

LTBP Transfer Requirement Item Detail

LAGP Storage Bin Master

Invoice verify

BKPF

BSEG

(SD) SALES AND DISTRIBUTION

Sales Documents

VBAK Sales Document - Header Data

VBAP Sales Document - Detail Data （儲存了）

VBEP 銷售憑證:計劃行資料

VBBE 銷售需求（拖延訂單或者斷貨）

VBUK 銷售憑證：擡頭狀態和管理資料（也可以看到DN單的狀態）

VBFA 銷售憑證流，【先前的銷售和分銷憑證】VBELV欄位就是在VA01裡看到訂單的最頂層；

VBPA 售達方、收貨方－>再根據【地址號碼】ADRNR查詢【ADRC】表找到相應的地址;

VBAK-VBELN 關聯VBPA-VBELN；

如何查詢電子郵件地址？ADR6

KONV 銷售訂單價格表：Condition Procedures(含有內容比較多)（通過VBAK的KNUMV和KPOSN兩個欄位）

Delivery Documents

LIKP Delivery Document - Header Data

l (包含售達方，送達方內容)，可以通過LIKP找到VBPA，然後再找ADRC

l LIKP- LFART（交貨單型別）

l 也包含了內向交貨單

LIPS Delivery Document - Detail Data ；

Billing Documents

VBRK Billing Document - Header Data

VBRP Billing Document - Detail Data

ConditionTables（價格）

KONH Condition Header（通訊表）

KONP Condition Detail

KONV Condition Procedures(是代表銷售訂單的價格資料)（通過VBAK的KNUMV和KPOSN兩個欄位）

KOTE\* Rebate（回扣） Condition Tables – many

_966 966是條件表，如果不會則前面加_查詢一下；

KOTN\* 買贈（VBN1建立的）

A8\* 打折表

(FI) FINANCIAL ACCOUNTING

Accounting Documents

BKPF Accounting Document Header

BSEG Accounting Document Detail

(CO) CONTROLLING

CO-PC

COAS

COSS

COSP 包括所有的數量

COVP 儲存工序確認後的數值與COBK進行關聯(通過物件號，憑證編號)，\[業務事務]＝COIN，一般情況下與AFRU相同。(COVP的參考憑證號碼,參照組織單位與AFRU 的確認號和計數器)，AFKO的定單號與COBK關聯，

COBK 包含相關的憑證號

COEP

COVP COEP與COBK關聯VIEWER

CO-PA

CE10010 ABC Operating Concern - Details

CE20010 ABC Operating Concern - Summary

CE30010 ABC Operating Concern - Summary

主資料

CSKS 成本中心

CSKA 成本要素

CSKU

CSKB

CSLA 作業型別（擡頭）

CSLT 作業型別文字

批次主資料

MCHA 工廠下的批次資料表

MCH1 集團下的批次資料表

MISC（系統表）

TSTC SAP Transactions Codes

CDHDR Change documentheader

CDPOS Change document items

Material Ledger物料分類帳

MLCD 物料分類帳: 彙總記錄 (從憑證0

MLCR 物料分類帳憑證：貨幣和值

MLCRF 物料分類帳檔案：欄位組(貨幣)

MLCRP 物料分類帳憑證: 價格更改(貨幣,

MLFG 物料分類帳檔案：欄位組

MLGN 每一倉庫號物料資料

MLGN\_TMP 直接輸入的糾正資料的檔案

MLGT 每一儲存型別的物料資料

MLGT\_TMP 直接輸入的糾正資料的檔案

MLHD 物料總帳憑證：標題

MLIB 提供給供應商的物料

MLIT 物料分類帳憑證:專案

MLKEPH 物料分類帳憑證: 價值成本元件分

MLMST 物料分類帳憑證: 成本核算執行標

MLPP 物料分類帳憑證：記帳期間和數量

MLPPF 物料分類帳檔案：欄位組(記帳期間

MLPRKEKO ML 憑證: 價格的成本元件分割(擡

MLPRKEPH ML 憑證: 價格的成本元件分割(組

MLST 重大事件

MLTX 重大事件描述

MLWERE 採購和物料分類帳之間的轉換表

MLWIPCOREF 物料分類帳中的 WIP 憑證 - 參考

MLWIPHD 物料分類帳中的 WIP 憑證 - 標題

CKMLPP 物料分類帳期間彙總記錄數量

PS（Project System）

Projects

IMAK Appropriationrequests - general data IMAV Appropriationrequest variant IMPR InvestmentProgram Positions IMPU Textsfor cap. inv. programpositions IMTP Investmentprograms IMZO AssignmentTable- CO Object - Capital InvestmentProg.Pos. PMCO Coststructure of maintenanceorder PRHI WorkBreakdown Structure, Edges (HierarchyPointer) （WBS的結構） PROJ Projectdefinition （專案定義） PRPS WBS(Work Breakdown Structure) Element Master Data （WBS的具體內容） RPSCO Project info database: Costs, revenues, finances（專案資訊資料庫: 成本, 銷售收入,財務）
