# day3_linux部分

## 主机状态监控
### top命令
1. 可以通过top命令查看CPU、内存使用情况,类似Windows的任务管理器默认每5秒刷新一次  
语法:直接输入top即可,按q或ctrl+c退出
```
top - 10:29:54 up 2 min,  1 user,  load average: 1.03, 0.81, 0.34
Tasks: 337 total,   1 running, 336 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.2 us,  8.3 sy,  0.0 ni, 87.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :   3867.7 total,   2144.6 free,   1158.8 used,    819.4 buff/cache     
MiB Swap:   3517.0 total,   3517.0 free,      0.0 used.   2708.9 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND 
 3478 shitogu+  20   0   14536   5528   3352 R   9.1   0.1   0:00.02 top      
    1 root      20   0   23384  14292   9556 S   0.0   0.4   0:03.40 systemd  
    2 root      20   0       0      0      0 S   0.0   0.0   0:00.04 kthreadd 
    3 root      20   0       0      0      0 S   0.0   0.0   0:00.00 pool_wo+ 
    4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+ 
```
```bash
top - 10:29:54 up 2 min,  1 user,  load average: 1.03, 0.81, 0.34
# top:命令名称,14:39:58:当前系统时间,up6min:启动了6分钟,2 users: 2个用户登录,load: 1、5、15分钟负载
Tasks: 337 total,   1 running, 336 sleeping,   0 stopped,   0 zombie
# Tasks: 175个进程,1running:1个进程子在运行,174sleeping:174个进程睡眠,0个停止进程,0个僵尸进程
%Cpu(s):  4.2 us,  8.3 sy,  0.0 ni, 87.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
# %Cpu(s):CPU使用率,us:用户CPU使用率,sy:系统CPU使用率,ni:高优先级进程占用CPU时间百分比,id:空闲CPU率,wa:10等待CPU占用率,hi: CPU硬件中断率，si:CPU软件中断率，st:强制等待占用CPU率
MiB Mem :   3867.7 total,   2144.6 free,   1158.8 used,    819.4 buff/cache     
MiB Swap:   3517.0 total,   3517.0 free,      0.0 used.   2708.9 avail Mem 
# Kib Mem:物理内存,total: 总量,free:空闲,used: 使用,buff/cache: buff和cache占用
# Kibswap:虚拟内存(交换空间),total:总量,free:空闲,used:使用,buff/cache:buff和cache占用

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND 
 3478 shitogu+  20   0   14536   5528   3352 R   9.1   0.1   0:00.02 top      
    1 root      20   0   23384  14292   9556 S   0.0   0.4   0:03.40 systemd  
    2 root      20   0       0      0      0 S   0.0   0.0   0:00.04 kthreadd 
    3 root      20   0       0      0      0 S   0.0   0.0   0:00.00 pool_wo+ 
    4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker+ 
# PID:进程id
# USER:进程所属用户
# PR:进程优先级，越小越高
# NI:负值表示高优先级，正表示低优先级
# VIRT:进程使用虚拟内存，单位KB
# RES:进程使用物理内存，单位KB
# SHR:进程使用共享内存，单位KB
# S:进程状态(S休眠，R运行，Z僵死状态，N负数优先级，空闲状态)
# %CPU:进程占用CPU率
# %MEM:进程占用内存率
# TIME+:进程使用CPU时间总计，单位10毫秒
# COMMAND:进程的命令或名称或程序文件路径
```
2. top命令选项  
top命令也支持选项:
```bash
选项 功能 
-p  只显示某个进程的信息
-d  设置刷新时间，默认是5S
-c  显示产生进程的完整命令，默认是进程名
-n  指定刷新次数，比如 `top -n 3`，刷新输出3次后退出
-b  以非交互非全屏模式运行，以批次的方式执行top，一般配合-n指定输出几次统计信息，将输出重定向到指k定文件，比如 `top -b -n 3 > /tmp/top.tmp`
-i  不显示任何闲置(idle)或无用(zombie)的进程
-u  查找特定用户启动的进程
```
3. top交互式选项  
当top以交互式运行(非-b选项启动)，可以用以下交互式命令进行控制
```bash
按键    功能
h键     按下h键，会显示帮助画面
c键     按下c键，会显示产生进程的完整命令，等同于-c参数，再次按下c键，变为默认显示
f键     按下f键，可以选择需要展示的项目
M键     按下M键，根据驻留内存大小(RES)排序
P键     按下P键，根据CPU使用百分比大小进行排序
T键     按下T键，根据时间/累计时间进行排序
E键     按下E键，切换顶部内存显示单位
e键     按下e键，切换进程内存显示单位
l键     按下l键，切换显示平均负载和启动时间信息。
i键     按下i键，不显示闲置或无用的进程，等同于-i参数，再次按下，变为默认显示
t键     按下t键，切换显示CPU状态信息
m键     按下m键，切换显示内存信息
```

### 磁盘信息监控
#### df命令
使用df命令，可以查看硬盘的使用情况  
语法: `df [-h]`  
选项: `-h`，以更加人性化的单位显示
```bash
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ df
Filesystem     1K-blocks     Used Available Use% Mounted on
tmpfs             396056     1764    394292   1% /run
/dev/sda2       20463184 10744108   8654272  56% /
tmpfs            1980268        0   1980268   0% /dev/shm
tmpfs               5120        8      5112   1% /run/lock
tmpfs             396052      124    395928   1% /run/user/1000
/dev/sr0         6194550  6194550         0 100% /media/shitoguaji/Ubuntu 24.04.2 LTS amd64
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           387M  1.8M  386M   1% /run
/dev/sda2        20G   11G  8.3G  56% /
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           387M  124K  387M   1% /run/user/1000
/dev/sr0        6.0G  6.0G     0 100% /media/shitoguaji/Ubuntu 24.04.2 LTS amd64
```
#### iostat命令
可以使用iostat查看CPU、磁盘的相关信息  
语法: `iostat [-x] [num1] [num2]`  
选项: `-x`,显示更多信息  
`num1`:数字,刷新间隔,`num2`:数字,刷新几次  
tps: 该设备每秒的传输次数 (Indicate the number of transfers per second that were issued to the device,)。"一次传输"意思是"一次I/O请求"。多个逻辑请求可能会被合并为"一次!/O请求"。"一次传输"请求的大小是未知的。  
```
rrgm/s: 每秒这个设备相关的读取请求有多少被Merge了(当系统调用需要读取数据的时候,VF将请求发到各个FS,如果FS发现不同的读取请求读取的是相同BlocK的数据,FS会将这个请求合并Merge,提高I0利用率,避免重复调用);
wrqm/s: 每秒这个设备相关的写入请求有多少被Merge了。
rsec/s: 每秒读取的扇区数;sectors
wsec/:  每秒写入的扇区数。
rKB/s:  每秒发送到设备的读取请求数
wKB/S:  每秒发送到设备的写入请求数
avgrq-sz平均请求扇区的大小
avgqu-sz平均请求队列的长度。毫无疑问，队列长度越短越好。
await:  每一个I0请求的处理的平均时间(单位是微秒毫秒)。
svctm   表示平均每次设备1/0操作的服务时间(以毫秒为单位)
%util:  磁盘利用率
```
### 网络状态监控
可以使用sar命令查看网络的相关统计(sar命令非常复杂,这里仅简单用于统计网络)  
语法: `sar -n DEV num1 num2`  
选项: `-n`，查看网络，DEV表示查看网络接口  
`num1`:刷新间隔(不填就查看一次结束),`num2`:查看次数(不填无限次数)  
```bash
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ sar -n DEV 1 3
Linux 6.14.0-27-generic (shitoguaji-VMware-Virtual-Platform) 	08/06/2025 	_x86_64_	(2 CPU)

10:51:08 AM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
10:51:09 AM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
10:51:09 AM     ens33      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

10:51:09 AM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
10:51:10 AM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
10:51:10 AM     ens33      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

10:51:10 AM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
10:51:11 AM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
10:51:11 AM     ens33      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

Average:        IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s   %ifutil
Average:           lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
Average:        ens33      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
信息解读:  
``` 
IFACE 本地网卡接口的名称  
rxpck/s 每秒钟接受的数据包  
txpck/s 每秒钟发送的数据包  
rxKB/S 每秒钟接受的数据包大小，单位为KB  
txKB/S 每秒钟发送的数据包大小，单位为KB  
rxcmp/s 每秒钟接受的压缩数据包  
txcmp/s 每秒钟发送的压缩包  
rxmcst/s 每秒钟接收的多播数据包

## 环境变量
环境变量是操作系统(Windows、Linux、Mac)在运行的时候,记录的一些关键性信息,用以辅助系统运行。  
在Linux系统中执行:env命令即可查看当前系统中记录的  
环境变量环境变量是一种KeyValue型结构  
### 环境变量:PATH
无论当前工作目录是什么,都能执行/usr/bin/cd这个程序,这个就是借助环境变量中:PATH这个项目的值来做到的。
```bash
[itheima@centos ~]$ env | grep PATH
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/itheima/.local/bin:/home/itheima/bin
```
PATH记录了系统执行任何命令的搜索路径，如上图记录了(路径之间以:隔开):
```
/usr/local/bin
/usr/bin
/usr/local/sbin
/usr/sbin
/home/itheima/.local/bin
/home/itheima/bin
```
### $符号
在Linux系统中,`$`符号被用于取"变量"的值  
环境变量记录的信息,除了给操作系统自己使用外,如果我们想要取用,也可以使用。  
语法: `$ 环境变量名` 来取得环境变量的值  
比如:`echo $PATH`  
就可以取得PATH这个环境变量的值,并通过echo语句输出出来。  
```bash
[itheima@centos ~]$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/itheima/.local/bin:/home/itheima/bin
```
又或者:`echo ${PATH}ABC`  
```bash
[itheima@centos ~]$ echo ${PATH}ABC
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/itheima/.local/bin:/home/itheima/binABC
```
当和其它内容混合在一起的时候，可以通过{}来标注取的变量是谁  

### 自行设置环境变量
Linux环境变量可以用户自行设置，其中分为:  
1. 临时设置，语法: `export 变量名=变量值`
```bash
[itheima@centos ~]$ export ITHEIMA=666
[itheima@centos ~]$ echo $ITHEIMA
666
```
2. 永久生效  
    针对当前用户生效，配置在当前用户的:     `~/.bashrc文件中`  
    针对所有用户生效，配置在系统的:         `/etc/profile文件中`  
    并通过语法:`source配置文件`，进行立刻生效，或重新登录FinalShell生效  

#### 自定义环境变量PATH
1. 测试:  
在当前HOME目录内创建文件夹，myenv,在文件夹内创建文件mkhaha  
通过vim编辑器,在mkhaha文件内填入:echo 哈哈哈哈哈完成上述操作后，随意切换工作目录,执行mkhaha命令尝试一下,会发现无法执行  
2. 修改PATH的值  
临时修改PATH: `export PATH=$PATH:/home/itheima/myenv`,再次执行mkhaha,无论在哪里都能执行了或将`export PATH=$PATH:/home/itheima/myenv`,填入用户环境变量文件或系统环境变量文件中去

## 压缩格式
### tar命令
Linux和Mac系统常用有2种压缩格式，后缀名分别是:  
1. `.tar`,称之为`tarball`, 归档文件,即简单的将文件组装到一个.tar的文件内,并没有太多文件体积的减少,仅仅是简单的封装  
2. `.9z`,也常见为`.tar.gz,gzip`格式压缩文件,即使用gzip压缩算法将文件压缩到一个文件内,可以极大的减少压缩后的体积  
3. 针对这两种格式，使用tar命令均可以进行压缩和解压缩的操作  
语法: `tar[-c -v -x -f -z -C] 参数1 参数2...参数N`  
```
-c,创建压缩文件，用于压缩模式
-v,显示压缩、解压过程，用于查看进度
-x,解压模式
-f,要创建的文件,或要解压的文件,-f选项必须在所有选项中位置处于最后一个
-z,gzip模式，不使用-z就是普通的tarball格式
-C,选择解压的目的地,用于解压模式
```
#### tar 命令压缩  
tar的常用组合为:  
```bash
tar -cvf test.tar 1.txt 2.txt 3.txt
#将1.txt 2.txt 3.txt压缩到test.tar文件内
tar -zcvf test.tar.gz 1.txt 2.txt 3.txt
#将1.txt 2.txt 3.txt压缩到test.tar.gz文件内,使用gzip模式
```
注意:
```
-z选项如果使用的话，一般处于选项位第一个
-f选项，必须在选项位最后一个
```
#### tar 解压
常用的tar解压组合:
```bash
tar -xvf test.tar
#解压test.tar,将文件解压至当前目录
tar -xvf test.tar -C /home/itheima
#解压test.tar,将文件解压至指定目录(/home/itheima)
tar -zxvf test.tar.gz -C /home/itheima
#以Gzip模式解压test.tar.gz,将文件解压至指定目录(/home/itheima)
```
注意:
```
-f选项，必须在选项组合体的最后一位
-z选项，建议在开头位置
-C选项单独使用，和解压所需的其它参数分开
```
### zip命令
#### zip 命令压缩文件
可以使用zip命令,压缩文件为zip压缩包  
语法: `zip [-r] 参数1 参数2... 参数N`  
`-r`,被压缩的包含文件夹的时候,需要使用-r选项,和rm、cp等命令的-r效果一致  
示例:
```bash
zip test.zip a.txt b.txt c.txt
#将a.txt b.txtc.txt压缩到test.zip文件内
zip -r test.zip test itheima a.txt
#将test、itheima两个文件夹和a.txt文件，压缩到test.zip文件内
```
#### unzip 命令解压文件
使用unzip命令,可以方便的解压zip压缩包  
语法: `unzip [-d] 参数`  
`-d`,指定要解压去的位置，同tar的-C选项  
`参数`，被解压的zip压缩包文件  
示例:  
```bash
unzip test.zip
#将test.zip解压到当前目录
unzip test.zip -d /home/itheima
#将test.zip解压到指定文件夹内(/home/itheima)
```