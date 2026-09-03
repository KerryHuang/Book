---
kind: original
---

# C# 集合, List<> 取交集、差集、聯集的方法

```c#
// using System.Linq;
static void Main(string[] args)
{
    // Intersect 交集
    // Except 差集
    // Union 聯集
    List<int> list1 = new List<int> { 1, 2, 3, 4, 5 };
    List<int> list2 = new List<int> { 3, 4, 5, 6, 8 };
 
    // 取交集, 即兩個集合中相同的元素
    // 輸出: 3, 4, 5
    var intersect = list1.Intersect(list2).ToList();
    Console.WriteLine("交集: {0}", string.Join(",", intersect));
 
    // 取差集, list1中哪些元素是list2中不存在的
    // 輸出: 1, 2
    var except1 = list1.Except(list2).ToList();
    Console.WriteLine("差集: {0}", string.Join(",", except1));
 
    // 取差集, list2中哪些元素是list1中不存在的
    // 輸出: 6, 8
    var except2 = list2.Except(list1).ToList();
    Console.WriteLine("差集: {0}", string.Join(",", except2));
 
    // 取聯集, list1集合與list2集合合併, 如果有相同元素只保留一個
    // 輸出: 1, 2, 3, 4, 5, 6, 8
    var union = list1.Union(list2).ToList();
    Console.WriteLine("聯集: {0}", string.Join(",", union));
 
    Console.Read();
}
```

