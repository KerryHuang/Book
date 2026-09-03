---
kind: original
---

# [SQL SERVER] Like in

之前如有查詢需求為co開頭 或 erry 結尾 或包含 vi...等，

我會先在AP端組好 like name co% or like name %erry or like name %vi%字串後送到後端SP中，

今天忽然覺得這樣的處理方法不夠好，隨後google找到一個不錯的方法，特此紀錄

--查詢 jobtitle 是 des 開頭 or ing 結尾 or 包含 Development

``` sql
select distinct *
from HumanResources.Employee t1
join
(
    select 'des%' as [filter]
    union all
    select '%ing'
    union all
    select '%Development%'
) t2 on t1.JobTitle like t2.filter
```