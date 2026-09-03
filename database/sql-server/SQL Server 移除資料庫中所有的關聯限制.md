---
kind: original
---

# SQL Server 移除資料庫中所有的關聯限制

## 內容

不多說，直接看作法吧

```sql
-- 記得先切換到想要移除的資料庫名稱下
USE [yourDataBaseName]
GO

-- 產生移除所有 FOREIGN KEY 的語法（先檢視，確認無誤再執行輸出的結果）
SELECT
    'ALTER TABLE [' + OBJECT_SCHEMA_NAME(fk.parent_object_id) + '].[' + OBJECT_NAME(fk.parent_object_id) + '] DROP CONSTRAINT [' + fk.name + '];'
FROM sys.foreign_keys AS fk
ORDER BY 1;
```

> 注意：移除關聯限制後資料完整性不再受保護，且無法直接復原，執行前請確認資料庫名稱並備份。

可以搭配[移除所有資料表](https://shunnien.github.io/2017/05/06/delete-all-database-table/)的語法一起使用。