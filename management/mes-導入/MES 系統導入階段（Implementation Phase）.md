---
kind: original
---

#  **MES 系統導入階段（Implementation Phase）**

# MES 導入階段細項規劃

導入階段可拆為 **12 大階段**：

1. 專案啟動
2. 現況流程盤點
3. 未來流程設計
4. Master Data 建置
5. 系統環境建置
6. 系統設定
7. 系統整合
8. 系統測試
9. 使用者驗收測試
10. 上線準備
11. 系統上線
12. 上線後支援

------

# Phase 1 專案啟動（Project Kickoff）

目的：建立導入共識與專案治理。

## 工作項目

| 編號 | 項目            | 說明          | 負責 |
| ---- | --------------- | ------------- | ---- |
| 1.1  | Kickoff Meeting | 專案啟動會議  | PM   |
| 1.2  | 專案範圍確認    | 確認導入模組  | 顧問 |
| 1.3  | 專案組織建立    | 專案角色      | PM   |
| 1.4  | 導入時程規劃    | 建立計畫      | PM   |
| 1.5  | 導入風險評估    | Risk Register | 顧問 |

產出文件：

- Project Charter
- Implementation Plan

------

# Phase 2 現況流程盤點（AS-IS Analysis）

目的：了解客戶現場流程。

## 工作項目

| 編號 | 項目         | 說明            |
| ---- | ------------ | --------------- |
| 2.1  | 訂單流程訪談 | Order Flow      |
| 2.2  | 生產流程訪談 | Production Flow |
| 2.3  | 報工流程訪談 | Shopfloor       |
| 2.4  | 品質流程訪談 | QC Flow         |
| 2.5  | 物料流程訪談 | Material Flow   |

顧問工具：

- 訪談問卷
- 現場觀察
- 文件收集

產出文件：

- AS-IS Process Map
- Pain Point List

------

# Phase 3 未來流程設計（TO-BE Design）

目的：設計 MES 流程。

## 工作項目

| 編號 | 項目         | 說明       |
| ---- | ------------ | ---------- |
| 3.1  | 設計工單流程 | Work Order |
| 3.2  | 設計派工流程 | Dispatch   |
| 3.3  | 設計報工流程 | Reporting  |
| 3.4  | 設計品質流程 | Quality    |
| 3.5  | 設計物料流程 | Material   |

TO-BE 流程：

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

產出文件：

- TO-BE Process Map
- MES Functional Design

------

# Phase 4 Master Data 建置

MES 成功關鍵。

## 工作項目

| 編號 | 資料     | 說明       |
| ---- | -------- | ---------- |
| 4.1  | 組織資料 | 部門       |
| 4.2  | 員工資料 | 操作員     |
| 4.3  | 機台資料 | Equipment  |
| 4.4  | 工作中心 | Workcenter |
| 4.5  | 產品資料 | Item       |
| 4.6  | BOM      | 物料       |
| 4.7  | Routing  | 製程       |

產出：

- Master Data Template
- Data Migration File

------

# Phase 5 系統環境建置

目的：建立 MES 系統環境。

## 工作項目

| 編號 | 項目          | 說明     |
| ---- | ------------- | -------- |
| 5.1  | Server 建置   | 安裝     |
| 5.2  | Database 建置 | SQL      |
| 5.3  | Network 設定  | LAN      |
| 5.4  | Client Setup  | Terminal |

架構：

```
Operator Tablet
      ↓
MES Web Server
      ↓
Database Server
```

------

# Phase 6 系統設定（System Configuration）

## 工作項目

| 編號 | 設定       | 說明     |
| ---- | ---------- | -------- |
| 6.1  | Factory    | 工廠     |
| 6.2  | Workcenter | 工作中心 |
| 6.3  | Machine    | 機台     |
| 6.4  | Operation  | 工序     |
| 6.5  | User       | 使用者   |
| 6.6  | Role       | 權限     |

產出：

- System Configuration Document

------

# Phase 7 系統整合（Integration）

MES 需整合外部系統。

| 系統  | 整合內容 |
| ----- | -------- |
| ERP   | 訂單     |
| WMS   | 庫存     |
| PLM   | BOM      |
| SCADA | 機台     |

整合方式：

- REST API
- File Import
- OPC

------

# Phase 8 系統測試（Testing）

測試分為三階段：

| 測試             | 說明 |
| ---------------- | ---- |
| Unit Test        | 功能 |
| Integration Test | API  |
| Performance Test | 壓力 |

------

# Phase 9 使用者驗收測試（UAT）

客戶進行驗收。

測試案例：

| Case     | 步驟 |
| -------- | ---- |
| 建立工單 | 建立 |
| 派工     | 指派 |
| 報工     | 完成 |

產出：

- UAT Report

------

# Phase 10 上線準備（Go-Live Preparation）

## 工作項目

| 編號 | 項目              |
| ---- | ----------------- |
| 10.1 | 教育訓練          |
| 10.2 | Master Data Final |
| 10.3 | 系統備份          |
| 10.4 | 上線計畫          |

------

# Phase 11 系統上線（Go-Live）

Go-Live 模式：

Pilot Line

```
CNC Line
 ↓
Factory Rollout
```

------

# Phase 12 上線後支援

| 支援         | 說明     |
| ------------ | -------- |
| Hypercare    | 上線支援 |
| Issue Fix    | 問題     |
| Optimization | 改善     |

------

# 導入 WBS 總覽

```
Kickoff
 ↓
AS-IS
 ↓
TO-BE
 ↓
Master Data
 ↓
System Setup
 ↓
Integration
 ↓
Testing
 ↓
UAT
 ↓
Go-Live
```

