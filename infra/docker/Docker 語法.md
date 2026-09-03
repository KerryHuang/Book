---
kind: original
---

# Docker指令大全

## Docker Service

查看Docker版本資訊

```
$ docker version
```

查看Docker目前狀態

```
$ service docker status
```

啟動Docker Service

```
$ service docker start
```

將Docker Service重啟

```
$ service docker restart
```

將Docker Service停止

```
$ service docker stop
```

## Image

查看某Image資訊 （例如查看Cassandra Image的資訊）

```
$ docker inspect cassandra
```

利用關鍵字搜尋image (例如搜尋cassandra)，會顯示所有跟cassandra相關的image

```
$ docker search cassandra
```

利用Dockerfile建立映像檔 (repository:tag為tiangolo/nginx_flask)

```
$ docker build -t "tiangolo/nginx_flask" .
```

利用Dockerfile建立映像檔，且不用暫存的cache (repository:tag為tiangolo/nginx_flask)

```
$ docker build --no-cache -t "tiangolo/nginx_flask" .
```

映像檔刪除舊的Tag

```
$ docker rmi {old tag}
```

映像檔新增Tag

```
$ docker tag {old tag} {new tag}
```

同一個映像檔可以有多個tag，例如，`cutejaneii/pythonapp3` 和 `cutejaneii/pythonapp3_new` 同時指向 `e0cbc38a4b19`這個映像檔

```
root@vm:/home/jennifer# docker images
REPOSITORY                                    TAG                 IMAGE ID            CREATED             SIZE
cutejaneii/pythonapp3                         latest              e0cbc38a4b19        3 weeks ago         79.7MB

root@vm:/home/jennifer# docker tag cutejaneii/pythonapp3 cutejaneii/pythonapp3_new
root@vm:/home/jennifer# docker images
REPOSITORY                                    TAG                 IMAGE ID            CREATED             SIZE
cutejaneii/pythonapp3                         latest              e0cbc38a4b19        3 weeks ago         79.7MB
cutejaneii/pythonapp3_new                     latest              e0cbc38a4b19        3 weeks ago         79.7MB
```

儲存Image (將tiangolo/nginx_flask這個Image，另存新檔，檔名:imgFlask)

```
$ docker save -o imgFlask tiangolo/nginx_flask
```

將映像檔 LOAD到Docker

```
$ docker load -i imgFlask
```

映像檔上傳至儲存庫

```
$ docker push cutejaneii/docker.uwsgi-nginx-flask-emperor
```

更改registry為不需SSL

```
$ vim /etc/default/docker
DOCKER_OPTS="$DOCKER_OPTS --insecure-registry=192.168.0.1:5500"
```

## Container

匯出Container

```
$ docker export -o xxx.tar [ContainerID]
$ docker export [ContainerID] > xxx.tar
```

接續上個指令，將上個指令產生的xxx.tar匯入成新的映像檔

```
$ cat xxx.tar | docker import - cutejaneii/xxx
```

停止Container

```
$ docker stop [container id]
```

刪除Container

```
$ docker rm [container id]
```

列出目前運作的docker container

```
$ docker ps
```

列出目前所有的(包含運作中及停止運作的的)docker container

```
$ docker ps -a
```

啟動container

```
$ docker start [container id]
```

查看container的log

```
$ docker logs [container id]
```

查看container的資訊

```
$ docker inspect [container id]
```

進到某個container後，執行bash

```
$ docker exec -i -t [ContainerID] bash
```

用tiangolo/nginx_flask這個Image，啟動container，並對應container port 80 = host port 8080

```
$ docker run -d -p 8080:80 --name ContainerName tiangolo/nginx_flask
```

用tiangolo/nginx_flask這個Image，啟動container，並對應container port 80 = host port 8080，並將container內的時區設成跟HOST一樣

```
$ docker run -d -p 8080:80 --name ContainerName -v /etc/localtime:/etc/localtime:ro tiangolo/nginx_flask
```

同上，如需對應多個port，可用下列語法

```
$ docker run -d -p 8080:80 -p 8181:81 --name ContainerName tiangolo/nginx_flask
```

建立container，並對應container folder = host folder (container folder此時可被修改)

```
$ docker run -d --name ContainerName -v /{folder}/app:/app tiangolo/nginx_flask
```

建立container，並對應container folder = host folder (container folder設為唯讀)

```
$ docker run -d --name ContainerName -v /{folder}/app:/app:ro tiangolo/nginx_flask
```

建立container，並設定使用host的網路

```
$ docker run -d --net=host --restart=always cutejaneii/imgID
```

建立container，並設定Timezone=Taipei

```
$ docker run -d --net=host -e "TZ=Asia/Taipei" cutejaneii/docker.nginx-flask-python-pandas
```

建立container，並設定Python Encoding = UTF-8

```
$ docker run -d --net=host --restart=always -e PYTHONIOENCODING=UTF-8 [image]
```

在container內查詢HOST的IP

```
$ cd /sbin
$ ip route|awk '/default/ {print $3}'
```

刪除所有container的log

```
$ truncate -s 0 /var/lib/docker/containers/*/*-json.log
```

複製檔案 (container -> HOST)

```
$ docker cp [ContainerID]:/etc/cassandra/cassandra.yaml cassandra.yaml
```

複製檔案 (HOST -> container)

```
$ docker cp cassandra.yaml [ContainerID]:/etc/cassandra/cassandra.yaml
```

移除Docker

```
$ sudo apt-get purge docker-ce
$ sudo rm -rf /var/lib/docker
```

建立與nfs同步的data volume

```
docker volume create --driver local \
      --opt type=nfs \
      --opt o=nfsvers=3,addr=192.168.0.55,rw \
      --opt device=:/nfsfolder \
      volume_nfs
```

---

docker build -t mywebapi-image -f MyWebAPI/Dockerfile .
docker run -d -p 8080:80 --name mywebapi-container mywebapi-image
docker run --rm -it -p 8000:8080 <my-app>
docker logs mywebapi-container
docker stop mywebapi-container
docker rm mywebapi-container