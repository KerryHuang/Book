# Docker - 第五章 | 安裝 Redis

## Redis介紹

Redis官網：https://redis.io/
https://zh.wikipedia.org/zh-tw/Redis
Redis是一個非關聯式資料庫(No-SQL)，因為主要是用In-memory的方式儲存資料，所以非常適合用來儲存短時間大量資料的使用場景，也就是拿來當快取cache使用。
由於Redis官方並不建議在Windows環境中使用Redis，所以官方也沒有提供Windows版本的安裝檔。若要在Windows環境中使用Redis，有兩種方式，第一個是用非官方發佈版本，這是由微軟團隊維護的版本，但目前最新版本只有3.2.100，若要使用，可至以下網址進行下載
https://github.com/MicrosoftArchive/redis/releases
安裝方式步驟，可參考以下文章：
https://www.dotblogs.com.tw/YiruAtStudio/2021/01/13/111530
另一個方式是，在Windows上，透過WSL下載並執行Redis的Docker。以下將介紹此種方式。



## 下載Reids的Docker Image及設定

接著開啟PowerShell，並輸入「docker pull redis」下載redis的docker image
```
docker pull redis
```
![https://ithelp.ithome.com.tw/upload/images/20211004/20140827UmFWtfRg8g.png](https://ithelp.ithome.com.tw/upload/images/20211004/20140827UmFWtfRg8g.png)
下載完成後，開啟Docker Desktop，在Image中就可以看到redis。接著按右邊的「run」啟動redis
另一個方法：啓動redis鏡像 無配置文件啓動
```
docker run -p 6379:6379 -d redis:latest redis-server
```
![https://ithelp.ithome.com.tw/upload/images/20211004/201408277aSKkcfsib.png](https://ithelp.ithome.com.tw/upload/images/20211004/201408277aSKkcfsib.png)
輸入Container Name及Local Host的Port，這裡Port我們直接輸入預設的6379，最後按下「Run」
![https://ithelp.ithome.com.tw/upload/images/20211004/201408272SiWmTHqjW.png](https://ithelp.ithome.com.tw/upload/images/20211004/201408272SiWmTHqjW.png)
就可以看到剛才建立的redis-sj已經在執行中
![https://ithelp.ithome.com.tw/upload/images/20211004/20140827Xam99Jk4xf.png](https://ithelp.ithome.com.tw/upload/images/20211004/20140827Xam99Jk4xf.png)

## 測試Redis是否正常運作

首先，在console中輸入「pip install redis」安裝redis套件
![https://ithelp.ithome.com.tw/upload/images/20211004/20140827a1KdGIkVQZ.png](https://ithelp.ithome.com.tw/upload/images/20211004/20140827a1KdGIkVQZ.png)
接著，建立測試程式碼，範例如下：

```python
import redis
#建立連線，port指定剛才在Docker中所設定的port，並將decode_responses設為True，讓取得資料時自動decode
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
r.set('myName', 'Mike') #存入key及value
r.set('中文的key', '中文的value') #存入資料，key可以是中文
print(r)
print(r.get('myName')) #輸入key值來取得剛
print(r.get('中文的key'))
```

redis儲存方式為key和value，用set的方式來增加或更新value，用get的方式來取得所儲存的value。若上述程式可以正常執行並取得所存入的value，就表示Redis已正常執行。



## 安裝 RedisInsight on Docker
```
docker pull redislabs/redisinsight
docker run -v redisinsight:/db -p 8001:8001 redislabs/redisinsight:latest
```

參考
[Install RedisInsight on Docker](https://docs.redis.com/latest/ri/installing/install-docker/)


## Redis監控工具：redmon

```
docker pull vieux/redmon
docker run -d --link redis:redis -p 4567:4567 vieux/redmon -r redis://redis:6379
```
