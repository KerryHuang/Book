# architecture

架構與設計：設計模式、認證授權、微服務、DDD/CQRS

[← 回總目錄](../README.md)

- **auth/**
  - [OAuth 與 SSO](<auth/OAuth 與 SSO.md>)
  - [Single Sign On 實作方式介紹 (CAS)](<auth/Single Sign On 實作方式介紹 (CAS).md>) — 轉貼：Yu-Jack
- **ddd-cqrs/**
  - [DDD + CQRS + MediatR 專案架構](<ddd-cqrs/DDD + CQRS + MediatR 專案架構.md>)
  - [MediatR Notification (Publish) 與 Behaviors 範例](<ddd-cqrs/MediatR Notification (Publish) 與 Behaviors 範例.md>)
- **design-patterns/**
  - [Repository 模式 (Repository Pattern)](<design-patterns/Repository 模式 (Repository Pattern).md>) — [轉貼：Ray Chiu](https://raychiutw.github.io/2019/隨手-Design-Pattern-4-Repository-模式-Repository-Pattern/)
  - [單例模式 (Singleton Pattern)](<design-patterns/單例模式 (Singleton Pattern).md>) — 轉貼：Ray Chiu
  - [軟體分層設計模式 (Software Layered Architecture Pattern)](<design-patterns/軟體分層設計模式 (Software Layered Architecture Pattern).md>) — [轉貼：Ray Chiu](https://raychiutw.github.io/2019/隨手-Design-Pattern-2-軟體分層設計模式-Software-Layered-Architecture-Pattern/)
  - [雙重檢查鎖定模式 (Double-Checked Locking Pattern)](<design-patterns/雙重檢查鎖定模式 (Double-Checked Locking Pattern).md>) — 轉貼：Ray Chiu
- **microservices/**
  - [微服務架構 #2, 按照架構，重構系統](<microservices/微服務架構 %232, 按照架構，重構系統.md>) — 轉貼：Andrew Wu
  - [微服務架構 - 從狀態圖來驅動 API 的設計](<microservices/微服務架構 - 從狀態圖來驅動 API 的設計.md>) — 轉貼：Andrew Wu
  - [淺談微服務與網站架構的發展史](<microservices/淺談微服務與網站架構的發展史.md>)
  - **API First Workshop 設計概念與實做案例/**
    - [API First #1 架構師觀點 - API First 的開發策略 - 觀念篇](<microservices/API First Workshop 設計概念與實做案例/API First %231 架構師觀點 - API First 的開發策略 - 觀念篇.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2022/10/26/apifirst/)
    - [API First #2 架構師觀點 - API First 的開發策略 - 設計實做篇](<microservices/API First Workshop 設計概念與實做案例/API First %232 架構師觀點 - API First 的開發策略 - 設計實做篇.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2023/01/01/api-design-workshop/)
  - **基礎建設 - 建立微服務的執行環境/**
    - [Part #1 微服務基礎建設 - Service Discovery](<microservices/基礎建設 - 建立微服務的執行環境/Part %231 微服務基礎建設 - Service Discovery.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2017/12/31/microservice9-servicediscovery/)
    - [Part #2 微服務基礎建設 - 服務負載的控制](<microservices/基礎建設 - 建立微服務的執行環境/Part %232 微服務基礎建設 - 服務負載的控制.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2018/06/10/microservice10-throttle/)
    - [Part #3 微服務基礎建設 - 排隊機制設計](<microservices/基礎建設 - 建立微服務的執行環境/Part %233 微服務基礎建設 - 排隊機制設計.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2018/12/12/microservice11-lineup/)
    - [Part #4 可靠的微服務通訊 - Message Queue Based RPC](<microservices/基礎建設 - 建立微服務的執行環境/Part %234 可靠的微服務通訊 - Message Queue Based RPC.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2019/01/01/microservice12-mqrpc/)
    - [Part #5 非同步任務的處理機制 - Process Pool](<microservices/基礎建設 - 建立微服務的執行環境/Part %235 非同步任務的處理機制 - Process Pool.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2020/02/09/process-pool/)
  - **實做基礎技術 API & SDK Design/**
    - [API & SDK Design #1, 資料分頁的處理方式](<microservices/實做基礎技術 API & SDK Design/API & SDK Design %231, 資料分頁的處理方式.md>) — 轉貼：Andrew Wu
    - [API & SDK Design #2, 設計專屬的 SDK](<microservices/實做基礎技術 API & SDK Design/API & SDK Design %232, 設計專屬的 SDK.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2016/10/10/microservice3/)
    - [API & SDK Design #3, API 的向前相容機制](<microservices/實做基礎技術 API & SDK Design/API & SDK Design %233, API 的向前相容機制.md>) — 轉貼：Andrew Wu
    - [API & SDK Design #4, API 上線前的準備 - Swagger + Azure API Apps](<microservices/實做基礎技術 API & SDK Design/API & SDK Design %234, API 上線前的準備 - Swagger + Azure API Apps.md>) — 轉貼：Andrew Wu
    - [API & SDK Design #5 如何強化微服務的安全性 API Token  JWT 的應用](<microservices/實做基礎技術 API & SDK Design/API & SDK Design %235 如何強化微服務的安全性 API Token  JWT 的應用.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2016/12/01/microservice7-apitoken/)
  - **建構微服務開發團隊/**
    - [架構面試題 #1, 線上交易的正確性](<microservices/建構微服務開發團隊/架構面試題 %231, 線上交易的正確性.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2018/03/25/interview01-transaction/)
    - [架構面試題 #2, 連續資料的統計方式](<microservices/建構微服務開發團隊/架構面試題 %232, 連續資料的統計方式.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2018/04/01/interview02-stream-statistic/)
    - [架構面試題 #3, RDBMS 處理樹狀結構的技巧](<microservices/建構微服務開發團隊/架構面試題 %233, RDBMS 處理樹狀結構的技巧.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2019/06/01/nested-query/)
    - [架構面試題 #4 - 抽象化設計；折扣規則的設計機制](<microservices/建構微服務開發團隊/架構面試題 %234 - 抽象化設計；折扣規則的設計機制.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2020/03/10/interview-abstraction/)
  - **架構師觀點 - 轉移到微服務架構的經驗分享/**
    - [Part #1 改變架構的動機](<microservices/架構師觀點 - 轉移到微服務架構的經驗分享/Part %231 改變架構的動機.md>) — 轉貼：Andrew Wu
    - [Part #2 實際改變的架構案例](<microservices/架構師觀點 - 轉移到微服務架構的經驗分享/Part %232 實際改變的架構案例.md>) — 轉貼：Andrew Wu
  - **案例實作 - IP 查詢服務的開發與設計/**
    - [容器化的微服務開發 #1 架構與開發範例](<microservices/案例實作 - IP 查詢服務的開發與設計/容器化的微服務開發 %231 架構與開發範例.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2017/05/28/aspnet-msa-labs1/)
    - [容器化的微服務開發 #2 IIS or Self Host](<microservices/案例實作 - IP 查詢服務的開發與設計/容器化的微服務開發 %232 IIS or Self Host.md>) — [轉貼：Andrew Wu](https://columns.chicken-house.net/2018/05/12/msa-labs2-selfhost/)
