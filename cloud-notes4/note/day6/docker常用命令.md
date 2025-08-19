# Docker的常用命令
## 帮助命令
```sh
docker version      # 显示docker的版本信息
docker info         # 显示docker的系统信息，包括镜像和容器的数量
docker 命令 --help   # 帮助命令
```
帮助文档的地址：https://docs.docker.com/engine/reference/commandline/

## 镜像命令
### **docker images**
```sh
shitoguaji@shitoguaji:~$ docker images
REPOSITORY              TAG             IMAGE ID            CREATED             SIZE
he11o-world             latest          bf756fb1ae65        4 months ago        13.3kB
# 解释
REPOSITORY  镜像的仓库源
TAG         镜像的标签
IMAGE ID    镜像的id
CREATED     镜像的创建时间
SIZE        镜像的大小
# 可选项
    -a，--all               # 列出所有镜像
    -9，--quiet             # 只显示镜像的id
```

### **docker search 搜索镜像**
```sh
shitoguaji@shitoguaji:~$ docker search mysql
NAME                                            DESCRIPTION                                         STARS                                       OFFICIAL                                            AUTOMATED
mysql                                           MySQL is a widely used,open-source relation...      9494
[OK]
mariadb                                         MariaDB is acommunity-developed fork of Mys...      3441
[OK]


# 可选项，通过搜藏来过滤
--filter=STARS=5000     # 搜索出繫寘个来的镜像就是STARS大于5000的
shitoguaji@shitoguaji:~$ docker search mysql --filter=STARS=5000
NAME                                            DESCRIPTION                                         STARS                                       OFFICIAL                                            AUTOMATED
mysql                                           MySOL is a widely used,open-source relation...      9494
[OK]
```

### **docker pull 下载镜像**
```sh
# 下载镜像 docker pu1] 镜像名[:tag]
shitoguaji@shitoguaji:~$ docker pull mysql
Using default tag:latest    # 如果不写 tag，默认就是 latest
latest: Pulling from library/mysql
10aec8a104c7: Pull complete   # 分层下载，docker iamge的核心 联合文件系统
c81e70a25040: Pull complete 
b9916866e45f: Pull complete 
cac9e6e2c9d6: Pull complete 
5d2f76605aa7: Pull complete 
31f7d8dc4024: Pull complete 
f15cc21449ca: Pull complete 
a22f87a7c498: Pull complete 
e55b6f427ac7: Pull complete 
fcb1221d0ce3: Pull complete 
Digest: sha256:a776e89aad2d425c248ccfb840115aaa52883499ff36512db4d503b11aae455a # 签名
Status: Downloaded newer image for mysql:latest
docker.io/library/mysq:latest   #真实地址

# 等价于它
docker pull mysq1
docker pull docker.io/library/mysql:latest
#指定版本下载
shitoguaji@shitoguaji\:~$ docker pull mysql:8.0
8.0: Pulling from library/mysql
10aec8a104c7: Already exists 
eb4c833f6ac8: Pull complete 
ac1d09b99a58: Pull complete 
d90a2df7273a: Pull complete 
29def2d20dd4: Pull complete 
21c02f1ef6a5: Pull complete 
227c621e92bf: Pull complete 
0dd51a1cf370: Pull complete 
c17e5ae8443e: Pull complete 
6ae00a88a906: Pull complete 
13ecfab825f5: Pull complete 
Digest: sha256:f483084b37081f1574c8d4e4485cd9028abcb022973c44c079a520eb01801d55
Status: Downloaded newer image for mysql:8.0
docker.io/library/mysql:8.0
```
```sh
shitoguaji@shitoguaji:~$ docker images
REPOSITORY     TAG       IMAGE ID       CREATED        SIZE
mysql          8.0       9340b388320f   3 weeks ago    781MB
mysql          latest    e829314b93fd   3 weeks ago    921MB
hello-world    latest    74cc54e27dc4   6 months ago   10.1kB
```

### **docker rmi 删除镜像**
```sh
shitoguaji@shitoguaji:~$ docker rmi -f 镜像id   # 删除指定的镜像
shitoguaji@shitoguaji:~$ docker rmi -f 镜像id 镜像id 镜像id 镜像id  # 删除多个镜像
shitoguaji@shitoguaji:~$ docker rmi -f $(docker images -ag)  # 删除全部的镜像
```

## 容器命令
### **说明:有了镜像才可以创建容器，linux，下载一个 centos 镜像来测试**
```sh
docker pull centos
```

### **新建容器并启动**
```sh
docker run [可选参数] image

# 参数说明
--name="Name"      容器名字  tomcat01  tomcat02，用来区分容器
-d                  后台方式运行
-it                 使用交互方式运行，进入容器查看内容
-p                  指定容器的端口 -p 8080:8080
    -p ip:主机端口:容器端口
    -p 主机端口:容器端口 (常用)
    -p 容器端口
    容器端口
-p                  随机指定端口


# 测试，启动并进入容器
shitoguaji@shitoguaji:~$ docker run -it centos:centos7 /bin/bash
[root@f162b7bc05e4 /]# ls   # 查看容器内的centos，基础版本，很多命令都是不完善的!
anaconda-post.log  dev  home  lib64  mnt  proc  run   srv  tmp  var
bin                etc  lib   media  opt  root  sbin  sys  usr

# 从容器中退回主机
[root@f162b7bc05e4 /]# exit
exit
```

### **列出所有的运行的容器**
```sh
# docker ps 命令
        # 列出当前正在运行的容器
-a      # 列出当前正在运行的容器+带出历史运行过的容器
-n=?    # 显詎示最近最
-q      # 只显示容器的编号

shitoguaji@shitoguaji:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

shitoguaji@shitoguaji:~$ docker ps -a
CONTAINER ID   IMAGE            COMMAND       CREATED              STATUS                      PORTS     NAMES
f162b7bc05e4   centos:centos7   "/bin/bash"   About a minute ago   Exited (0) 53 seconds ago             ecstatic_davinci
5f5b0277ec6e   hello-world      "/hello"      3 days ago           Exited (0) 3 days ago                 lucid_lamport

shitoguaji@shitoguaji:~$ docker ps -a -n=1
CONTAINER ID   IMAGE            COMMAND       CREATED         STATUS                     PORTS     NAMES
f162b7bc05e4   centos:centos7   "/bin/bash"   3 minutes ago   Exited (0) 2 minutes ago             ecstatic_davinci

shitoguaji@shitoguaji:~$ docker ps -aq
f162b7bc05e4
5f5b0277ec6e
```

### **退出容器**
```sh
exit    # 直接容器停止并退出
Ctrl + P + Q    # 容不停止退出
```

### **删除容器**
```sh
docker rm 容器id                    # 删除指定的容器，不能删除正在运行的容器，如果要强制删除 rm -f
docker rm -f $(docker ps -ag)       # 删除所有的容器
docker ps -a -q|xargs docker rm     # 删除所有的容器
```

### **启动和停止容器的操作**
```sh
docker start 容器id         # 启动容器
docker restart 容器id       # 重启容器
docker stop 容器id          # 停止当前正在运行的容器
docker ki1] 容器id          # 强制停止当前容器
```
## 常用的其他命令
### **后台启动容器**
```sh
# 命令 docker run -d 镜像名!
shitoguaji@shitoguaji:~$ docker run -d centos:centos7

# 问题docker ps，发现 centos 停止了

# 常见的坑：docker 容器使用后台运行，就必须要有要一个前台进程，docker发现没有应用，就会自动停止
# nginx，容器启动后，发现自己没有提供服务，就会立刻停止，就是没有程序了
```

### **查看日志**
```sh
docker logs -f -t --tail 容器，没有日志

#自己编写一段she11脚本
shitoguaji@shitoguaji:~$ docker run -d centos:centos7 /bin/bash -c "while true;do echo kuangshen;sleep 1;done"
e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff

shitoguaji@shitoguaji:~$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED        STATUS                      PORTS     NAMES
e108e803560d   centos:centos7   "/bin/bash -c 'while…"   2 seconds ago  Up 2 seconds                          eloquent_villani

# 显示日志
 -tf            # 显示日志
 --tail number  # 要显示日志条数
shitoguaji@shitoguaji:~$ docker logs -tf --tail 10 e108e803560d
```
### **查看容器中进程信息**
```sh
# 命令 docker top 容器id
shitoguaji@shitoguaji:~$ docker top e108e803560d
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                5427                5404                0                   14:18               ?                   00:00:00            /bin/bash -c while true;do echo kuangshen;sleep 1;done
root                5974                5427                0                   14:26               ?                   00:00:00            sleep 1
```

### **查看镜像的元数据**
```sh
#命冬
docker inspect 容器id

# 测试
shitoguaji@shitoguaji:~$ docker inspect e108e803560d
[
    {
        "Id": "e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff",
        "Created": "2025-08-14T06:18:59.350811177Z",
        "Path": "/bin/bash",
        "Args": [
            "-c",
            "while true;do echo kuangshen;sleep 1;done"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 5427,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2025-08-14T06:18:59.383155078Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9",
        "ResolvConfPath": "/var/lib/docker/containers/e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff/hostname",
        "HostsPath": "/var/lib/docker/containers/e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff/hosts",
        "LogPath": "/var/lib/docker/containers/e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff/e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff-json.log",
        "Name": "/eloquent_villani",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                25,
                91
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/interrupts",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "ID": "e108e803560de2af38146feda9caffd3d5f93bf24d1d425b1186d753586110ff",
                "LowerDir": "/var/lib/docker/overlay2/102a2ab92d4d28096c9d5d556e993a313d5ba3e5a32ebda80dfa0dfc518c0c94-init/diff:/var/lib/docker/overlay2/f35274d21f07f3936623bf4f929af60007595d69fe4618d0b902fecebf7b5771/diff",
                "MergedDir": "/var/lib/docker/overlay2/102a2ab92d4d28096c9d5d556e993a313d5ba3e5a32ebda80dfa0dfc518c0c94/merged",
                "UpperDir": "/var/lib/docker/overlay2/102a2ab92d4d28096c9d5d556e993a313d5ba3e5a32ebda80dfa0dfc518c0c94/diff",
                "WorkDir": "/var/lib/docker/overlay2/102a2ab92d4d28096c9d5d556e993a313d5ba3e5a32ebda80dfa0dfc518c0c94/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "e108e803560d",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash",
                "-c",
                "while true;do echo kuangshen;sleep 1;done"
            ],
            "Image": "centos:centos7",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20201113",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS",
                "org.opencontainers.image.created": "2020-11-13 00:00:00+00:00",
                "org.opencontainers.image.licenses": "GPL-2.0-only",
                "org.opencontainers.image.title": "CentOS Base Image",
                "org.opencontainers.image.vendor": "CentOS"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "2e28c76a3584cee359a16bc43fc5bfa6d2d6e1cad3d88ab40def0922c840e249",
            "SandboxKey": "/var/run/docker/netns/2e28c76a3584",
            "Ports": {},
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "222bb93dc2d71086ccb80ea8ba24c07d1244424d804c016a6697f70e0db01b62",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "62:a0:09:c0:c5:36",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "62:a0:09:c0:c5:36",
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "242a7d69e3c29cd8aea8fe9e9b297aa2512c908ae59d4dc83550713332d3813b",
                    "EndpointID": "222bb93dc2d71086ccb80ea8ba24c07d1244424d804c016a6697f70e0db01b62",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
    }
]
```

### **进入当前正在运行的容器**
```sh
# 通常容器都是使用后台方式运行的，需要进入容器，修改一些配置
# 命令
docker exec -it 容器id bashshell

# 测试
shitoguaji@shitoguaji:~$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED        STATUS                      PORTS     NAMES
e108e803560d   centos:centos7   "/bin/bash -c 'while…"   2 seconds ago  Up 2 seconds                          eloquent_villani
shitoguaji@shitoguaji:~$ docker exec -it e108e803560d /bin/bash
[root@f162b7bc05e4 /]# ls
anaconda-post.log  dev  home  lib64  mnt  proc  run   srv  tmp  var
bin                etc  lib   media  opt  root  sbin  sys  usr

[root@f162b7bc05e4 /]# ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 10:21 ?        00:00:05 /bin/sh-c while true;do echo kuangshen;sleep l;done
root         505       0  0 10:21 pts/0    00:00:00 /bin/bash
root         530       1  0 10:21 ?        00:00:00 /usr/bin/coreuti1s --coreutils-prog-shebang=sleep
/usr/bin/sleep 1
root         531     505  0 10:21 pts/0    00:00:00 ps -ef

# 方式二
docker attach 容器id
#测试
shitoguaji@shitoguaji:~$ docker attach e108e803560d
正在执行当前的代码...

# docker exec       # 进入容器后开启一个新的终端，可以在里面操作(常用)
# docker attach     # 进入容器正在执行的终端，不会启动新的进程!
```
### **从容器内拷贝文件到主机上**
docker cp 容器:容器路径 目的的主机路径
```sh
# 查看当前主机目录下
root@shitoguaji-VMware-Virtual-Platform:/home# ls
shitoguaji  tomcat
root@shitoguaji-VMware-Virtual-Platform:/home# docker ps
CONTAINER ID   IMAGE            COMMAND       CREATED         STATUS         PORTS     NAMES
7463fae73c93   centos:centos7   "/bin/bash"   4 minutes ago   Up 4 minutes             serene_meninsky

# 进入docker 内部容器
root@shitoguaji-VMware-Virtual-Platform:/home# docker attach 7463fae73c93
[root@7463fae73c93 /]# cd /home
[root@7463fae73c93 home]# ls
# 在容器内新建一个文件
[root@7463fae73c93 home]# touch test.java
[root@7463fae73c93 home]# exit
exit
root@shitoguaji-VMware-Virtual-Platform:/home# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
root@shitoguaji-VMware-Virtual-Platform:/home# docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS                      PORTS     NAMES
7463fae73c93   centos:centos7   "/bin/bash"              5 minutes ago   Exited (0) 24 seconds ago             serene_meninsky

# 将这文件拷贝出来到主机上
root@shitoguaji-VMware-Virtual-Platform:/home# docker cp 7463fae73c93:/home/test.java /home
Successfully copied 1.54kB to /home
root@shitoguaji-VMware-Virtual-Platform:/home# ls
shitoguaji  test.java  tomcat
```

## 小结
```sh
attach      Attach to a running container                   # 当前 she11下 attach 连接指定运行镜像
build       Build an image from a Dockerfile                # 通过 Dockerfile 定制镜像  
commit      Create a new image from a container changes     # 提交当前容器为新的镜像  
cp          Copy files/folders from the containers filesystem to the host path    #从容器中拷贝指定文件或者目录到宿主机中  
events      Get real time events from the server            # 从 docker 服务获取容器实时事件  
exec        Run a command in an existing container          # 在已存在的容器上运行命令  
export      Stream the contents of a container as a tar archive    # 导出容器的内容流作为一个 tar 归档文件[对应 import ]  
history     Show the history of an image                    # 展示一个镜像形成历史  
images      List images                                     # 列出系统当前镜像  
import      Create a new filesystem image from the contents of a tarball # 从tar包中的内容创建一个新的文件系统映像[对应export]  
info        Display system-wide information                 # 显示系统相关信息  
inspect     Return low-level information on a container     # 查看容器详细信息  
kill        Kill a running container                        # kill 指定 docker 容器  
load        Load an image from a tar archive                # 从一个 tar 包中加载一个镜像[对应 save]  
login       Register or Login to the docker registry server    # 注册或者登陆一个 docker 源服务器  
logout      Log out from a Docker registry server           # 从当前 Docker registry 退出  
logs        Fetch the logs of a container                   # 输出当前容器日志信息  
port        Lookup the public-facing port which is NAT-ed to PRIVATE_PORT    # 查看映射端口对应的容器内部源端口  
pause       Pause all processes within a container          # 暂停容器  
ps          List containers                                 # 列出容器列表  
pull        Pull an image or a repository from the docker registry server    # 从docker镜像源服务器拉取指定镜像或者库镜像  
push        Push an image or a repository to the docker registry server    # 推送指定镜像或者库镜像至docker源服务器  
restart     Restart a running container                     # 重启运行的容器  
rm          Remove one or more containers                   # 移除一个或者多个容器  
rmi         Remove one or more images               # 移除一个或多个镜像[无容器使用该镜像才可删除，否则需删除相关容器才可继续或 -f 强制删除]  
run         Run a command in a new container                # 创建一个新的容器并运行一个命令  
save        Save an image to a tar archive                  # 保存一个镜像为一个 tar 包[对应 load]  
search      Search for an image on the Docker Hub           # 在 docker hub 中搜索镜像  
start       Start a stopped containers                      # 启动容器  
stop        Stop a running containers                       # 停止容器  
tag         Tag an image into a repository                  # 给源中镜像打标签  
top         Lookup the running processes of a container     # 查看容器中运行的进程信息  
unpause     Unpause a paused container                      # 取消暂停容器  
version     Show the docker version information             # 查看 docker 版本号  
wait        Block until a container stops, then print its exit code   # 截取容器停止时的退出状态值
create      Create a new container                          # 创建一个新的容器，同 run，但不启动容器  
diff        Inspect changes on a container's filesystem     # 查看 docker 容器变化  
```