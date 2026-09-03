---
kind: reprint
source: http://kenychen.logdown.com/posts/153722-ms-sql-how-to-use-database-mail-to-send-mail
author: kenychen
---

## [[MS SQL\]如何透過Database Mail進行郵件發送](http://kenychen.logdown.com/posts/153722-ms-sql-how-to-use-database-mail-to-send-mail)

Microsoft SQL Server裡提供了Database Mail可以用來設定外部的email，當主機有問題或是有發送Email需求時,就可以透過Database Mail來進行發送，設定方法如下:

開啟SQL Server Management Studio並連到SQL Server上，點開`管理`選項找到Database Mail，在Database Mail選項上按右鍵開啟選單，選擇`設定Database Mail`

![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/fXRyVOsgRFOJmOKQpOUA_dbmail1.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/To3EbRaQQd2VPC1AiZVH_dbmail2.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/DyRqbxYIS12JYy3MlWYZ_dbmail3.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/7HmwoTw5R2rKRJCij0Ki_dbmail4.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/a3C6FLKjQamis35NTBeC_dbmail5.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/K6QdRQzSQKwHvLYmRqxg_dbmail6.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/BiOrS7rYSiemrcIMOYWB_dbmail7.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/PLKgkBP3SDergJNAeWXX_dbmail8.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/XDSsms9T2WEAaserAGPX_dbmail9.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/IbbHl3RtSluuUDWJyNi9_dbmail10.png)



![img](http://user-image.logdown.io/user/3379/blog/3423/post/153722/W8KTqUWSx2SrVGnj7n4C_dbmail11.png)

如果有收到Email表示Database Mail設定成功囉~~

------

### 那要如何在用SQL進行Email發送呢?

直接執行下面的SQL指令

Send Email From Database Email

``` sql
EXEC msdb.dbo.sp_send_dbmail
  @profile_name = 'mail sender',            --這裡輸入Database Mail設定檔的名稱
  @recipients = 'kenychen99@gmail.com',         --要發送的Email
  @body = 'Email本文內容',                   --Email的本內容    
  @body_format = 'HTML',                    --本文的格式,設定為HTML,在Email的本文內可以使用HTML語法
  @subject = 'Email主旨' ;                       --這裡設定Email 主旨
```

這樣就可以發送Email了，是不是很簡單呢?
如果要在網頁程式或應用程式中發送Email，可以直接在程式中EXECUTE上面的SQL語法，就可以把Email發送出去了，用Database Mail這種做法發送Email還有一個優點,就是可以查到Email發送的記錄，只要執行下面的SQL就可以查詢到Email的發送記錄

查詢Database Mail發送記錄

``` sql
   SELECT * FROM [msdb].[dbo].[sysmail_mailitems]
```

send_status 狀態
0:「未傳送」
1:「已傳送」
2:「失敗」
3:「正在重試」



### 刪除三個月前的所有電子郵件

``` sql
DECLARE @GETDATE datetime  
SET @GETDATE = DATEADD(MONTH, -3, GETDATE());  
EXECUTE msdb.dbo.sysmail_delete_mailitems_sp @sent_before = @GETDATE;  
GO  
```

