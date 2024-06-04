# 使用SSIS創建同步資料庫數據任務

SSIS（SQL Server Integration Services）是用於生成企業級數據集成和數據轉換解決方案的平臺。使用 Integration Services 可解決複雜的業務問題，具體表現為：複製或下載文件，發送電子郵件以響應事件，更新數據倉庫，清除和挖掘數據以及管理 SQL Server 對象和數據。這些包可以獨立使用，也可以與其他包一起使用以滿足複雜的業務需求。Integration Services 可以提取和轉換來自多種源（如 XML 數據文件、平面文件和關係數據源）的數據，然後將這些數據載入到一個或多個目標。（摘自MSDN，更多詳細信息可參考：http://technet.microsoft.com/zh-cn/library/ms141026(v=sql.105).aspx）

 

下麵我使用SSIS來演示一個實際例子。比如我有一個資料庫，出於備份數據或者其它的目的，會定期的對這個資料庫的數據遷移到其它的資料庫去。遷移的時候，有些新增的欄位會被插入備份資料庫，而有些被修改過的欄位也會在備份資料庫被修改。現在我們就用SSIS來完成這項任務。

首先在我源資料庫db_source和目標資料庫db_destination中運行以下SQL創建好需要的表，就以這一個表test_1來進行示範。

```
CREATE TABLE [dbo].[test_1](
    [Id] [int] IDENTITY(1,1) NOT NULL primary key,
    [Name] [varchar](50) NULL,
    [Age] [int] NULL
)
```

 

建好表好在源數據表中可以隨便加幾條記錄，目標資料庫暫時留空。

現在我們打開VS，創建一個Intergration Services Project。（註意：如果SQL Server 裝的是Express版的話是沒有這個項目工程模板的）

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_1.png)

 

創建好工程後，在Control Flow這個Tab下拖入一個Data Flow Task，如下圖：

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_2.png)

 

雙擊這個Data Flow Task，我們就會進入Data Flow這個Tab標簽中。

 

然後我們在左邊工具欄里找到OLE DB Source，繼續拖兩個OLE DB Source出來。分別給它們命名為Source DB和Destination DB。

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_3.png)

 

將數據源拖出來後，雙擊它，可以對它進行一些設置，主要就是鏈接資料庫及選擇你要進行遷移的表或者視圖等設置，這裡我就不詳細說明瞭。註意一點的是就像上圖所示，如果一個圖形上出現一個紅X的話說明設置有錯誤。

再來就是拖兩個Sort及一個Merge Join出來，將之前的數據源箭頭分別指向兩個Sort，最後兩個Sort出來的數據同時輸入Merge Join中。

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_4_1.png)

 

分別雙擊兩個Sort，鉤選表中的ID，對ID這個欄位進行一次排序。因為Merge Join這個流程要求輸入的數據是已排序好的。這個排序也可以直接在數據源中對它們的輸出欄位設置SortKeyPosition這個屬性來排序。（詳見：http://msdn.microsoft.com/zh-cn/library/ms137653.aspx）

這裡我們第一次從Sort拉箭頭到Merge Join的時候，會讓我們選擇這個輸入的數據是作為左輸入還是右輸入，我們按照圖示的那樣，左邊的作為左輸入，右邊的作為右輸入。然後我們雙擊Merge Join，按照如下圖所示設置：

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_5.png)

 

這裡打鉤的是這個流程之後輸出的數據，Join Type需要選擇為Left outer join，因為左邊是我們的原始數據表，右邊是我們備份的表，右表可以看成是一個左表的一個子集，如果左表有的數據，右表沒有的，那些就是需要新插入備份資料庫的數據。

現在我們需要一個分支，即新的數據需要插入備份資料庫中，而已有的數據需要更新為新的值。我們從工具欄中拖入一個Conditional Split來進行這樣的分支處理。我們將Merge Sort中的輸出指向Conditional Split，然後雙擊Conditional Split，如下圖所示設置（註意條件一個是ISNULL，一個是非ISNULL）。

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_6.png)

 

這時它們的輸入值就被分成兩種條件輸出，最後我們再拖入一個OLE DB Destination來插入數據和一個OLE DB Command來更新資料庫，最終流程如下圖：

 

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_7.png)

 

雙擊設置OLE DB Destionation，選擇好數據導入的目標資料庫中的表，這裡需要註意的就是要鉤選Keep identity這個選項，因為我創建表的時候對ID欄位使用了自增屬性。

雙擊設置OLE DB Command，首先在Connection Managers這個Tab中選擇好鏈接對象，然後在Component Properties這個選項卡中，設置你的SqlCommand屬性。如下圖：

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_8.png)

 

這裡的參數值都是用？號來代替，之後在Column Mappings這個Tab中設置代替值實際代替的列，如下圖：

![img](http://www.zendei.com/js/img.php?url=http://images.cnblogs.com/cnblogs_com/heqichang/256112/o_20120919_9.png)

 

至此，任務就創建完畢了，沒有編寫任何代碼，直接拖拉完成了。現在可以直接在VS中按F5運行看下效果，我們的目標數據表將插入源數據表中的值。然後我們修改一下原數據表，再來運行一下上面這個任務，就可以在目標資料庫中看到更改了。

 

那麼如何去定時完成任務哩？這裡可以用SQL Server Agent去調用上面我們寫好的包， 或者在Windows計劃任務中使用DTExec.exe去執行上面的任務。