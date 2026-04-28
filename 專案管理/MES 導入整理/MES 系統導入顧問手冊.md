# MES 系統導入顧問手冊

客戶：精工機械股份有限公司
 產業：精密 CNC 加工
 顧問單位：Waydo MES Consulting
 版本：1.0

------

# 目錄

1. 導入概述
2. 客戶現況分析
3. 專案治理
4. 導入策略
5. AS-IS 現況流程
6. TO-BE 未來流程
7. Master Data 模型
8. 系統架構
9. 系統整合設計
10. MES 系統設定
11. 客製需求與開發
12. 資料轉換
13. 系統測試
14. 使用者驗收測試
15. 教育訓練
16. Go-Live 策略
17. 變革管理
18. KPI 管理
19. 持續改善
20. 導入成果

------

# 第一章 導入概述

MES（Manufacturing Execution System）是連接 ERP 與生產現場的核心系統。

MES 在企業系統架構中的位置：

```
ERP
 ↓
MES
 ↓
Shopfloor
```

MES 主要功能：

| 功能     | 說明 |
| -------- | ---- |
| 生產管理 | 工單 |
| 現場管理 | 報工 |
| 品質管理 | 檢驗 |
| 設備管理 | OEE  |
| 物料管理 | WIP  |

------

# 第二章 客戶現況分析

## 2.1 客戶背景

精工機械股份有限公司主要製造：

- CNC 精密零件
- 鋁合金外殼
- 機械支架

客戶主要市場：

| 市場       | 比例 |
| ---------- | ---- |
| 自動化設備 | 40%  |
| 半導體設備 | 35%  |
| 機器人設備 | 25%  |

------

## 2.2 生產設備

| 類型     | 數量 |
| -------- | ---- |
| CNC 車床 | 12   |
| CNC 銑床 | 8    |
| 鑽攻機   | 6    |
| 研磨機   | 4    |

------

## 2.3 現有 IT 系統

| 系統  | 功能 |
| ----- | ---- |
| ERP   | 訂單 |
| Excel | 排程 |
| 紙本  | 報工 |

------

## 2.4 客戶痛點

| 問題         | 說明       |
| ------------ | ---------- |
| 生產不透明   | 無即時進度 |
| 報工不準確   | 紙本       |
| 品質追溯困難 | 無 Lot     |

------

# 第三章 專案治理

## 專案組織

| 角色            | 人員     |
| --------------- | -------- |
| Sponsor         | 總經理   |
| Project Manager | IT 經理  |
| MES Consultant  | 顧問     |
| Production Lead | 生產主管 |

------

# 第四章 導入策略

導入模式：

**Pilot → Rollout**

```
CNC 車床產線
      ↓
CNC 銑床產線
      ↓
全廠
```

------

# 第五章 AS-IS 現況流程

## 訂單流程

```
Customer Order
       ↓
ERP Order
       ↓
Excel Production Plan
       ↓
Paper Work Order
```

問題：

- 排程混亂
- 無法追蹤進度

------

## 報工流程

```
Operator
  ↓
Paper Sheet
  ↓
Supervisor Excel
```

問題：

- 延遲
- 不準確

------

# 第六章 TO-BE 未來流程

MES 流程：

```
ERP Order
     ↓
MES Work Order
     ↓
Dispatch
     ↓
Production
     ↓
Report
     ↓
Quality
     ↓
Inventory
```

------

# 第七章 Master Data 模型

## Machine

| Machine ID | Name        | Workcenter |
| ---------- | ----------- | ---------- |
| MC-01      | Mazak CNC   | Turning    |
| MC-02      | Okuma CNC   | Turning    |
| MC-03      | DMG Milling | Milling    |

------

## Employee

| ID   | Name   | Role     |
| ---- | ------ | -------- |
| E001 | 陳建宏 | Operator |
| E002 | 林志豪 | Operator |

------

## Item

| Item   | Name       |
| ------ | ---------- |
| P-1001 | 鋁合金外殼 |
| P-1002 | 馬達支架   |

------

## Routing

| Item   | Operation | Machine |
| ------ | --------- | ------- |
| P-1001 | Turning   | MC-01   |
| P-1001 | Milling   | MC-03   |

------

# 第八章 系統架構

MES 系統架構：

```
Tablet / PC
      ↓
MES Web
      ↓
Application Server
      ↓
SQL Database
```

------

# 第九章 系統整合

MES 整合：

| 系統  | 整合方式 |
| ----- | -------- |
| ERP   | API      |
| WMS   | API      |
| SCADA | OPC      |

------

# 第十章 系統設定

主要設定：

| 設定       | 範例     |
| ---------- | -------- |
| Factory    | 精工機械 |
| Workcenter | CNC Line |
| Machine    | MC-01    |

------

# 第十一章 客製開發

客戶需求：

| 功能           | 說明     |
| -------------- | -------- |
| Dashboard      | 即時生產 |
| OEE            | 設備效率 |
| Quality Report | 品質     |

------

# 第十二章 資料轉換

資料來源：

| 來源  | 類型  |
| ----- | ----- |
| Excel | BOM   |
| ERP   | Order |

ETL：

```
Extract
Transform
Load
```

------

# 第十三章 系統測試

| 測試        | 說明 |
| ----------- | ---- |
| Unit        | 功能 |
| Integration | API  |
| Performance | 壓力 |

------

# 第十四章 UAT

測試案例：

| Case              | 結果 |
| ----------------- | ---- |
| Create Work Order | Pass |
| Report Production | Pass |

------

# 第十五章 教育訓練

| 對象   | 訓練 |
| ------ | ---- |
| 生管   | 排程 |
| 作業員 | 報工 |
| 品保   | 檢驗 |

------

# 第十六章 Go-Live

Go-Live 模式：

Pilot Line

第一條產線：

CNC 車床

------

# 第十七章 變革管理

MES 導入變革：

| 項目 | 改變            |
| ---- | --------------- |
| 工單 | 紙本 → 電子     |
| 報工 | 手寫 → Terminal |

------

# 第十八章 KPI

MES KPI：

| KPI   | 目標    |
| ----- | ------- |
| OEE   | 75%     |
| Yield | 98%     |
| WIP   | 降低20% |

------

# 第十九章 持續改善

MES 上線後：

- OEE 分析
- AI 排程
- Predictive Maintenance

------

# 第二十章 導入成果

MES 上線三個月後：

| 指標       | 改善 |
| ---------- | ---- |
| 生產效率   | +18% |
| 交期準確率 | +25% |
| 不良率     | -12% |

------

# 附錄

## MES 導入時程

| Week  | Task    |
| ----- | ------- |
| Week1 | Kickoff |
| Week2 | Process |
| Week3 | Design  |
| Week4 | Build   |
| Week5 | Test    |
| Week6 | Go-Live |

------

## MES 成功關鍵

| 因素        | 說明   |
| ----------- | ------ |
| 管理支持    | 高層   |
| 流程標準    | SOP    |
| Master Data | 高品質 |

