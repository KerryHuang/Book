# 【GitHub Copilot】自動從 SQL 生成 UML

 Posted on 2025-03-17 Edited on 2025-03-18 In [GitHub Copilot](https://estellacoding.github.io/blog/categories/GitHub-Copilot/)

將完整展示如何透過 GitHub Copilot 自動解析 SQL JOIN 語法，逐步生成專業的 UML 圖表流程。從環境建置到最終視覺化呈現，帶大家再次體驗 AI 輔助開發的高效工作流。



# 安裝套件

關於如何安裝套件的方式，請看 [【GitHub Copilot】用 VS Code 解鎖 AI 寫扣超能力 - Mermaid](https://estellacoding.github.io/blog/github-copilot-vscode-ai-coding/#Mermaid)。

# 準備SQL

以製造業 ERP 系統的 Shop Floor Management 模組為例，設計一個多表連接查詢。(專治表格設計架構都不清楚就要上場寫SQL的小苦手)

這張報表需求是要查詢 WIP 工單進度、成本核算，以及生產交易記錄。

- WIP 工單追蹤報表 – 顯示工單進度、物料流動情況。
- WIP 成本核算報表 – 彙總工單對應的會計科目。
- 生產交易記錄報表 – 查詢所有 WIP 交易記錄。

```
SELECT 
  we.WIP_ENTITY_ID,
  we.WIP_ENTITY_NAME,
  wd.JOB_TYPE,
  wd.COMPLETION_SUBINVENTORY,
  wm.TRANSACTION_DATE,
  wm.TRANSACTION_ID,
  mm.INVENTORY_ITEM_ID,
  ms.DESCRIPTION AS ITEM_DESCRIPTION,
  wm.TRANSACTION_QUANTITY,
  wta.REFERENCE_ACCOUNT AS ACCOUNT_ID,
  wor.RESOURCE_SEQ_NUM AS RESOURCE_SEQ
FROM WIP_ENTITIES we
JOIN WIP_DISCRETE_JOBS wd ON we.WIP_ENTITY_ID = wd.WIP_ENTITY_ID
JOIN WIP_MOVE_TRANSACTIONS wm ON we.WIP_ENTITY_ID = wm.WIP_ENTITY_ID
JOIN MTL_MATERIAL_TRANSACTIONS mm ON wm.TRANSACTION_ID = mm.TRANSACTION_ID
JOIN MTL_SYSTEM_ITEMS_B ms ON mm.INVENTORY_ITEM_ID = ms.INVENTORY_ITEM_ID
JOIN WSM_SPLIT_MERGE_TRANSACTIONS wsm ON mm.TRANSACTION_ID = wsm.TRANSACTION_ID
JOIN WIP_TRANSACTION_ACCOUNTS wta ON we.WIP_ENTITY_ID = wta.WIP_ENTITY_ID
JOIN WIP_OPERATION_RESOURCES wor ON we.WIP_ENTITY_ID = wor.WIP_ENTITY_ID
```

(資料來源: [Shop Floor Management ER Diagram)](https://www.triniti.com/shop-floor-management-er-diagram)

# Copilot Edits

使用套件 vscode-mermAId 來自動生成 UML，記得要將sql檔案加入提示詞中。

```
@mermAId /uml 請根據所有的JOIN仔細畫出每個表的關聯的UML圖
```

![github-copilot-mermAId-uml-1](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-mermaid-uml%2Fgithub-copilot-mermAId-uml-1.jpg?alt=media&token=50bb427d-749e-4727-9bf7-e04deda7f745)

點擊View Markdown Source，可以看到 Copilot 幫我們生成的 Markdown 語法囉。
![github-copilot-mermAId-uml-2](https://firebasestorage.googleapis.com/v0/b/stellacoding1111.appspot.com/o/article%2Fgithub-copilot-vscode-ai-mermaid-uml%2Fgithub-copilot-mermAId-uml-2.jpg?alt=media&token=7e11bf9f-93f8-4431-8571-97c97e3407f0)

# 生成UML

生成的 Markdown 語法的 UML 後，即可在支援 Markdown 的平台上呈現。

(每次看還是會想wow一下XD)

```
classDiagram
    class WIP_ENTITIES {
        WIP_ENTITY_ID
        WIP_ENTITY_NAME
    }
    class WIP_DISCRETE_JOBS {
        WIP_ENTITY_ID
        JOB_TYPE
        COMPLETION_SUBINVENTORY
    }
    class WIP_MOVE_TRANSACTIONS {
        WIP_ENTITY_ID
        TRANSACTION_DATE
        TRANSACTION_ID
        TRANSACTION_QUANTITY
    }
    class MTL_MATERIAL_TRANSACTIONS {
        TRANSACTION_ID
        INVENTORY_ITEM_ID
    }
    class MTL_SYSTEM_ITEMS_B {
        INVENTORY_ITEM_ID
        DESCRIPTION
    }
    class WSM_SPLIT_MERGE_TRANSACTIONS {
        TRANSACTION_ID
    }
    class WIP_TRANSACTION_ACCOUNTS {
        WIP_ENTITY_ID
        REFERENCE_ACCOUNT
    }
    class WIP_OPERATION_RESOURCES {
        WIP_ENTITY_ID
        RESOURCE_SEQ_NUM
    }

    WIP_ENTITIES --> WIP_DISCRETE_JOBS : WIP_ENTITY_ID
    WIP_ENTITIES --> WIP_MOVE_TRANSACTIONS : WIP_ENTITY_ID
    WIP_MOVE_TRANSACTIONS --> MTL_MATERIAL_TRANSACTIONS : TRANSACTION_ID
    MTL_MATERIAL_TRANSACTIONS --> MTL_SYSTEM_ITEMS_B : INVENTORY_ITEM_ID
    MTL_MATERIAL_TRANSACTIONS --> WSM_SPLIT_MERGE_TRANSACTIONS : TRANSACTION_ID
    WIP_ENTITIES --> WIP_TRANSACTION_ACCOUNTS : WIP_ENTITY_ID
    WIP_ENTITIES --> WIP_OPERATION_RESOURCES : WIP_ENTITY_ID
```

# 結論

透過 GitHub Copilot 自動化解析與 vscode-mermAId 插件，讓我們能將複雜的 SQL JOIN 關係快速轉換為視覺化 UML 圖表，特別適合在以下情境:

- 幫助成員快速理解系統架構。
- 分析資料庫結構變更的潛在影響。
- 強化技術文件的視覺化表達。