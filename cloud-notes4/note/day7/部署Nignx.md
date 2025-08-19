# Docker 安装 Nginx
```sh
# 1、搜索镜像(去docker搜索，可以看到帮助文档search)
# 2、下载镜像 pu11
# 3、运行测试
shitoguaji@shitoguaji:~$ docker images
REPOSITORY     TAG       IMAGE ID       CREATED        SIZE
nginx          latest    ad5708199ec7   3 days ago     192MB
mysql          8.0       9340b388320f   3 weeks ago    781MB

#-d  后台运行
#--name  给容器命名
#-p  宿主机端口:容器内部端口
shitoguaji@shitoguaji:~$ docker run -d --name nginx01 -p 3344:80 nginx
da044a695994585538c73782df134dd203b7a9c68018a1007def36eb1ed487cb
shitoguaji@shitoguaji:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                     NAMES
da044a695994   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 6 seconds   0.0.0.0:3344->80/tcp, [::]:3344->80/tcp   nginx01
shitoguaji@shitoguaji:~$ curl localhost:3344
<!DOCTYPE html>
<html>
<head>
...

#网页搜索：IP:3344
#http://192.168.88.101:3344/

# 进入容器
shitoguaji@shitoguaji:~$ docker exec -it nginx01 /bin/bash
root@da044a695994:/# whereis nginx
nginx: /usr/sbin/nginx /usr/lib/nginx /etc/nginx /usr/share/nginx
root@da044a695994:/# cd /etc/nginx
root@da044a695994:/etc/nginx# ls
conf.d	fastcgi_params	mime.types  modules  nginx.conf  scgi_params  uwsgi_params
root@da044a695994:/etc/nginx# exit
exit
shitoguaji@shitoguaji:~$
```