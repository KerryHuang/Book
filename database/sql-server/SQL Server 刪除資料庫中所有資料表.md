---
kind: original
---

# SQL Server 刪除資料庫中所有資料表

## 作法

```
-- 記得先切換到想要移除的資料庫名稱下
USE [yourDataBaseName]
GO

DECLARE @table_schema varchar(100)
       ,@table_name varchar(100)
       ,@constraint_schema varchar(100)
       ,@constraint_name varchar(100)
       ,@cmd nvarchar(200)

DECLARE table_cursor CURSOR FOR
  select TABLE_SCHEMA, TABLE_NAME
    from INFORMATION_SCHEMA.TABLES
   where TABLE_NAME != 'sysdiagrams'
  
OPEN table_cursor
FETCH NEXT FROM table_cursor INTO @table_schema, @table_name
  
WHILE @@FETCH_STATUS = 0 
BEGIN
     SELECT @cmd = 'DROP TABLE [' + @table_schema + '].[' + @table_name + ']'
     --select @cmd
     EXEC sp_executesql @cmd
  
  
     FETCH NEXT FROM table_cursor INTO @table_schema, @table_name
END
  
CLOSE table_cursor 
DEALLOCATE table_cursor
```

補充說明一下，這版假如在移除有關聯資料表的時候，會因為 **FOREIGN KEY constraint** 而失敗，要先移除所有的關聯限制喔。