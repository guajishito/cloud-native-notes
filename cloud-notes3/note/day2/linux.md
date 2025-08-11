# day2_linux部分

## 网络传输

### 下载和网络请求
1. 使用ping命令可以测试到某服务器是否可联通  
语法: `ping [-c num] ip或主机名`  
选项: `-c`,测试的次数,不使用-c选项,将无限次数持续检查  
示例:
```bash
#检查到baidu.com是否联通
ping -c baidu.com
#检查到39.156.66.10是否联通，并检查3次
ping -c 3 39.156.66.10
```
2. 使用wget命令可以进行网络文件下载  
语法: `wget [-b] url`  
选项: `-b`,后台下载  
参数: `url`, 下载链接  
示例:
```bash
#下载anache-hadoop 3.3.0版本: 
waet http://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.az
#在后台下载: 
wget -b http://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
#通过tail命令可以监控后台下载进度:
tail-fwget-log 
```
3. 使用curl命令可以发起网络请求  
语法: `curl [-0] ur1`和`curl cip.cc`  
选项: `-0`,用于下载使用  
示例:
```bash
#向cip.cc发起网络请求:
curl cip.cc
#向python.itheima.com发起网络请求:
curl python.itheima.com
#通过curl下载hadoop-3.3.0安装包:
curl -0 http://archive.apache.org/dist/hadoop/common/hadoop3.3.0/hadoop-3.3.0.tar.gz
```

### 端口
1. 端口  
端口是指计算机和外部交互的出入口，可以分为：物理端口和虚拟端口两类  
[物理端口]:USB、HDMI、DP、VGA、RJ45等  
[虚拟端口]:操作系统和外部交互的出入口IP只能确定计算机,通过端口才能锁定要交互的程序  
2. 端口的划分  
[公认端口]:1~1023,用于系统内置或常用知名软件绑定使用  
[注册端口]:1024~49151,用于松散绑定使用(用户自定义)  
[动态端口]:49152~65535,用于临时使用(多用于出口)  
3. 查看端口占用  
**nmap IP地址,查看指定IP的对外暴露端口**
```bash
#语法:
nmap 被查看的IP地址
#示例:  本机(127.0.0.1)
namp 127.0.0.1
```
**netstat -anp | grep 端口号,查看本机指定端口号的占用情况**
```bash
语法:netstat -anp | grep 端口号
[root@bogon ~]# netstat -anp l grep 6000
tcp         0       0 0.0.0.0:6000      0.0.0.0:*           LISTEN      7174/X
tcp6        0       0 :::6000           :::*                LISTEN      7174/X
```
如图，可以看到当前系统6000端口被程序(进程号7174)占用了其中,0.0.0.0:6000,表示端口绑定在0.0.0.0这个IP地址上,表示允许外部访问
```bash
[root@bogon ~]# netstat -anp l grep 12345
[root@bogon ~]#
```
可以看到，当前系统12345端口，无人使用  

## 进程管理
### 进程
进程是指程序在操作系统内运行后被注册为系统内的一个进程,并拥有独立的进程ID(进程号)
### 管理进程的命令
1. ps 查看进程信息  
语法: `ps[-e -f]`  
选项: `-e`，显示出全部的进程  
选项: `-f`,以完全格式化的形式展示信息(展示全部信息)  
一般来说，固定用法就是:ps-ef列出全部进程的全部信息  
```
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 10:21 ?        00:00:05 /sbin/init splash
root           2       0  0 10:21 ?        00:00:00 [kthreadd]
root           3       2  0 10:21 ?        00:00:00 [pool_workqueue_release]
```
从左到右分别是:  
·UD:进程所属的用户ID  
·PID:进程的进程号ID  
·PPID:进程的父ID(启动此进程的其它进程)  
·C:此进程的CPU占用率(百分比)  
·STIME:进程的启动时间  
·TTY:启动此进程的终端序号，如显示?表IME示非终端启动  
·TIME:进程占用CPU的时间  
·CMD:进程对应的名称或启动路径或启动命令  
2. 查看指定进程  
语法: `ps-ef | grep 关键字`
```bash
#准确的找到tail命令的信息
ps -ef | grep tail
```
3. 关闭进程
语法: `kill [-9] 进程ID`  
选项: `-9`,表示强制关闭进程。不使用此选项会向进程发送信号要求其关闭,但是否关闭看进程自身的处理机制。  

