---
kind: reprint
---

# [SQL SERVER]撰寫Stored Procedure小細節

[SQL SERVER][Memo]撰寫Stored Procedure小細節

這篇筆記一下Stored Procedure有那些小細節，也順便提醒自己。

**1.不要忘記 set nocount on:**

SQL Server會針對每個Select 和 DML 回傳訊息給用戶端，

當有設定 nocount on時就可以關閉SQL Server 回傳訊息的行為，

這樣對效能會有不錯的改善，因為網路的傳輸量會降低不少。

**2.如果查詢陳述句太過複雜，請使用SP:**

如果你的商業邏輯複雜導致查詢陳述句過長又龐大，

建議可以使用SP來撰寫，因為用戶端(client)只會傳SP Name給SQL Server(而不是一長串的TSQL)，

所以網路的傳輸量也會降低不少。

**3.請使用兩節式命名:**

相關的物件請都使用兩節式(schema name+object name)命名，

因為這可以直接且明確找到該物件和編譯過的執行計畫，

而省下搜尋其他schema底下可能的object所浪費的資源和時間。

```
-- 兩節式命名
select * from dbo.test
exec dbo.myproc
-- 避免
select * from test
exec myproc
```

4.stored procedure命名勿使用 sp_ 開頭: 如果stored procedure使用sp_開頭，那SQL Server 會先搜尋master database完後， 在搜尋現階段連線的database，

這不僅浪費時間和資源，也增加出錯的機率(如果master database有相同的stored procedure名稱)

```
--usp開頭
create proc dbo.usp_xxx
--避免
create proc dbo.sp_xxx
```

**5.如果你要執行字串，請使用sp_executesql取代Execute(Exec) 陳述式**

![img](https://miro.medium.com/max/831/0*auVxrF2Gn5fxjmEK.png)

**(擷取線上叢書..我太懶了XD)，下面附上測試過程。**

```
declare @myquery nvarchar(4000);
set @myquery = 'SELECT * from dbo.test2 where c1 = @id';
--第一次
execute sp_executesql @myquery,N'@id int', @id = 1;
--第二次
execute sp_executesql @myquery,N'@id int', @id = 2;
--查看執行計畫
SELECT cap.usecounts as '使用次數',objtype as '快取類型',st.text
FROM sys.dm_exec_cached_plans cap
CROSS APPLY sys.dm_exec_sql_text(plan_handle) AS st
WHERE st.text not like '%sys%'
and st.text like '%dbo.test2%'
```

**使用sp_executesql**

![img](https://miro.medium.com/max/480/0*PVifclkq1S8T6se-.png)

**參數:1和2**

![img](https://miro.medium.com/max/481/0*uxlKmvoGs6YUboTn.png)

**參數:5和6**

**結果:我在SSMS查詢視窗中執行 sp_executesql 總共4次查詢，**

**可以看到只產生一個執行計畫且重複使用該執行計畫。**

```
DECLARE @myquery VARCHAR(8000)
,@myid int;
set @myid = 5;
set @myquery = 'select * from dbo.test2 where c1 = '+ CAST( @myid as varchar);
--第一次
exec (@myquery) 
set @myid = 6; 
set @myquery = 'select * from dbo.test2 where c1 = '+ CAST(@myid as varchar );
--第二次
exec (@myquery) 
SELECT cap.usecounts as '使用次數',objtype as '快取類型',st.text            
FROM sys.dm_exec_cached_plans cap
CROSS APPLY sys.dm_exec_sql_text(plan_handle) AS st
WHERE st.text not like '%sys%'
and st.text like '%dbo.test2%'
```

**使用exec(Execute)**

![img](https://miro.medium.com/max/370/0*GRXArJLzgBQgM_j3.png)

**參數:1和2**

![img](https://miro.medium.com/max/351/0*tYb4aUs0d9ZkfOiS.png)

**參數:5和6**

**結果:我在SSMS查詢視窗中執行 exec 總共4次查詢，可以看到產生4個執行計畫且個別使用次數為1次。**

**當然!這裡我只是提個大概，因為開發上還是有許多要注意的地方，**

**例如**[**盡量少使用Cursor**](http://www.dotblogs.com.tw/ricochen/archive/2010/11/09/19323.aspx)**，交易處理時請盡量縮短交易…等。**