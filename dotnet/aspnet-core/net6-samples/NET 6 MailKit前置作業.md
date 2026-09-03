---
kind: reprint
source: site:github.com/CI-YU/2022-ITHelp
author: CI-YU
---

# .NET 6 MailKit前置作業

### 目的

前往google帳號設定OAuth，才能使用google帳號寄信

### 點擊連結

到 [google帳號管理](https://console.cloud.google.com/cloud-resource-manager?organizationId=0&supportedpurview=project)

### 新增專案

點擊如圖按鈕建立新專案
![建立專案](https://user-images.githubusercontent.com/19286751/166645232-6a453bbe-f093-4df6-9128-629b0f3cbd3d.png)

命名你的專案名稱，並點擊建立
![專案命名](https://user-images.githubusercontent.com/19286751/166645841-6e7eb854-e443-4589-a698-3cd44d1c4f59.png)

### 設定OAuth

跟著紅框處點擊到OAuth同意畫面
![OAuth同意畫面](https://user-images.githubusercontent.com/19286751/166651058-7047b678-5cab-4ca7-9a7b-f80bcb461eca.png)

點擊剛剛建立的專案
![點擊專案](https://user-images.githubusercontent.com/19286751/166651647-9b246135-5d93-4305-bacf-5046487831de.png)

選擇外部，並點擊建立
![點擊外部](https://user-images.githubusercontent.com/19286751/166651858-7483c970-bb75-45a7-896f-c0bbbcdd8682.png)

### 編輯應用程式註冊申請畫面

將所有必填欄位填完![OAuth同意畫面](https://user-images.githubusercontent.com/19286751/166652165-9d91feea-ccac-44c5-ba72-b750633cf1e9.png)

第二步直接下一步
![範圍](https://user-images.githubusercontent.com/19286751/166652632-ee75a4fb-0343-40bf-bda2-3416cacb7f3a.png)

新增使用者，要建立你要使用的帳號
![測試使用者](https://user-images.githubusercontent.com/19286751/166652883-a546181d-c8aa-4bc2-a395-2ad1b43708d1.png)

摘要直接下一步
![摘要](https://user-images.githubusercontent.com/19286751/166654331-76ba7e10-d766-4f7f-b741-0ae21a5c7847.png)

### 憑證

點建立憑證
![建立憑證](https://user-images.githubusercontent.com/19286751/166655558-2ceb57eb-ac5f-49cc-a37a-3e7881cdd8b6.png)

點擊OAuth用戶端ID
![OAuth用戶端ID](https://user-images.githubusercontent.com/19286751/166655969-a09a8d3b-e63e-426b-8395-26dff49dac1e.png)

應用程式類型選擇電腦版應用程式，填入名稱後點擊建立
![選擇電腦版應用程式](https://user-images.githubusercontent.com/19286751/166656521-dd177cb0-bfbe-4a02-af92-1694479f39c6.png)

最後會取得用戶端ID與用戶端密碼
![結論](https://user-images.githubusercontent.com/19286751/166656884-36807911-acc0-4405-9232-a92e6b13a85b.png)

### 結論

最後就可以進行MailKit的使用了，下一篇就可以使用ＭailKit