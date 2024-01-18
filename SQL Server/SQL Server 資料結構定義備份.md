# [SQL Server View、Function 及 Stored Procedure 定義之快速備份](https://blog.darkthread.net/blog/dump-sql-things/)



我有個快速備份 SQL 資料庫 View、Function 以及 Stored Procedure 定義的需求，顯然球又飛進 PowerShell 的守備範圍。

SQL Server 有個 [sys.sql_modules](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-sql-modules-transact-sql?WT.mc_id=DOP-MVP-37580) 資料表，包含 View、Function、Stored Procedure、Trigger、Default... 等物件定義內容，其中 definition nvarchar(max) 欄位存有定義該物件的 SQL 指令。要查詢物件名稱、類別、是否為系統物件... 等資訊則需 JOIN [sys.objects](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-objects-transact-sql?WT.mc_id=DOP-MVP-37580)。(註：在網路爬文會看到性質相似的 sysobjects、syscomments 資料表，至今雖然仍可使用，但他們是基於向前相容保留的，未來會被移除，故建議改用新版資料表。新舊系統資料表對映表在[這裡](https://docs.microsoft.com/en-us/sql/relational-databases/system-tables/mapping-system-tables-to-system-views-transact-sql?WT.mc_id=DOP-MVP-37580))

為了測試，在 SQL LocalDB 隨便建了一個 View 一個 Function 及一個 Procedure：

![img](https://blog.darkthread.net/Posts/files/Fig1_637622964448552748.png)

核心查詢實測如下，透過 type in ('V','FN','IF','P') 限定 View/Function/Procedure，is_ms_shipped = 0 則用以排除 SQL 內建物件。

```sql
select m.object_id,m.definition,o.name,o.type, o.type_desc, o.modify_date
from sys.sql_modules m join sys.objects o
on m.object_id = o.object_id
where o.type in ('V','FN','IF','P')
and o.is_ms_shipped = 0
order by o.name,o.type
```



透過以上述查詢，CREATE 指令輕鬆到手：

![img](https://blog.darkthread.net/Posts/files/Fig2_637622964450820468.png)

接下來，寫一小段 PowerShell 執行查詢，讀取 View、Function、Procedure 的 CREATE Script，以物件名稱作為檔案名，分別儲存到 Views、Funcs、SPs 子資料就大功告成。

```ps
$ErrorActionPreference = "STOP"
# 提醒：範例為求精簡明碼寫死連線字串，實務應用時應加密並另行保存
$cs = "Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=path-to-mdf;Integrated Security=True"
$cn = [System.Data.SqlClient.SqlConnection]::new($cs)
$cn.Open()
$cmd = $cn.CreateCommand()
$cmd.CommandText = @"
select m.object_id,m.definition,o.name,o.type, o.type_desc
from sys.sql_modules m join sys.objects o
on m.object_id = o.object_id
where o.type in ('V','FN','IF','P')
and o.is_ms_shipped = 0
"@
$dr = $cmd.ExecuteReader()
$workPath = Get-Location
while ($dr.Read()) {
    $type = $dr["type"].ToString().Trim()
    $subFolder = "Views"
    if ($type -eq 'P') { $subFolder = "SPs" }
    elseif ($type -eq 'FN' -or $type -eq 'IF') { $subFolder = 'Funcs' }
    $name = $dr["name"].ToString()
    $targetFolder = [System.IO.Path]::Combine($workPath, $subFolder)
    [System.IO.Directory]::CreateDirectory($targetFolder) | Out-Null
    $dr["definition"].ToString() | 
        Out-File ([System.IO.Path]::Combine($targetFolder, $name + ".sql")) -Encoding utf8
    Write-Progress -Activity "匯出資料庫檢視、函式與 SP" -Status $name
}
$cn.Dispose()
```



測試成功。

![img](https://blog.darkthread.net/Posts/files/Fig3_637622964451444388.png)