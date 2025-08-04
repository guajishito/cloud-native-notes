# day4

# linux部分

## 快捷键
1. ctrl+c 强制停止
2. ctrl+d 退出登出
3. history 查看历史命令
4. ! 命令前缀,自动匹配上一个命令
5. ctrl+r ,搜索历史命令
6. ctrl+ae ,光标移动到命令开始或结束
7. ctrl+←|→ ,左右跳单词
8. ctrl+l 或 clear命令 清屏

## systemctl命令
Linux系统很多软件(内置或第三方)均支持使用systemctl命令控制:启动、停止、开机自启能够被systemctl管理的软件，一般也称之为:`服务`
[语法]:systemctl start | stop | status | enable | disable 服务名
    start 启动
    stop 关闭
    status 查看状态
    enable 开启开机自启
    disable 关闭开机自启
1. 系统内置的服务比较多，比如:
NetworkManager，主网络服务
network,副网络服务
firewalld,防火墙服务
sshd,ssh服务(Finalshell远程登录Linux使用的就是这个服务)
2. 部分第三方软件安装后也可以以systemctl进行控制
yum install -y ntp,安装ntp软件可以通过ntpd服务名，配合systemctl进行控制

## ln命令 创建软连接
在系统中创建软链接，可以将文件、文件夹链接到其它位置。类似Windows系统中的《快捷方式》[语法]:ln -s 参数1 参数2
`-s`选项，创建软连接
`参数1`:被链接的文件或文件夹
`参数2`:要链接去的目的地
**实例:**
ln -s /etc/yum.conf ~/yum.conf
ln -s /etc/yum ~/yum
~:HOME目录

## date 查看系统的时间
通过date命令可以在命令行中查看系统的时间
[语法]: date [-d] [+格式化字符串]
`-d`按照给定的字符串显示日期，一般用于日期计算
`格式化字符串`:通过特定的字符串标记，来控制显示的日期格式
    %Y 年
    %y 年份后两位数字(00.99)
    %m 月份(0112)
    %d 日(0131)
    %H 小时(00.23)
    %M 分钟(00.59)
    %S 秒(00.60)
    %s 自1970-01-0100:00:00UTC 到现在的秒数
```bash
**示例：**
date                                # 使用date命令本体,无选项，直接查看时间
2022年10月08日 星期六 00:45:45 PDT
date +Y-%m-%d                       # 按照2022-01-01的格式
2022-10-08
date "+%Y-%m-%d %H:%M:%S"           # 按照2022-01-01 10:00:00的格式
2022-10-08 00:48:12
**date命令进行日期加减**
`-d`选项，可以按照给定的字符串显示日期，一般用于日期计算
date -d "+1 day"+%Y%m%d              # 显示后一天的日期
date -d "-1 day" +%Y%m%d             # 显示前一天的日期
date -d "-1 month" +%Y%m%d           # 显示上一月的日期
其中支持的时间标记为:
    year    年
    Month   月
    day     天
    hour    小时
    Minute  分 钟
    second  秒
```

## 修改Linux时区
使用root权限,执行如下命令,修改时区为东八区时区
```bash
rm -f /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

## ntp程序
1. 启动并设置开机自启:
```bash
    systemctl start ntpd
    systemctl enable ntpd
```
当ntpd启动后会定期的联网校准系统的时间
2. 手动校准(需root权限):
```bash
ntpdate -untp.aliyun.com
```

通过阿里云提供的服务网址配合ntpdate(安装ntp后会附带这个命令)命令自动校准
