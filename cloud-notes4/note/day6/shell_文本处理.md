# shell_文本处理
## 1 cut
cut 的工作就是“剪”,具体的说就是在文件中负责剪切数据用的。cut 命令从文件的每一行剪切字节、字符和字段并将这些字节、字符和字段输出。  
1. **基本用法**  
    cut [ 选项参数 ] filename  
    说明:默认分隔符是制表符  
2. **选项参数说明**
```sh
    -f  # 列号，提取第几列
    -d  # 分隔符，按照指定分隔符分割列，默认是制表符 \t
    -c  # 按字符进行切割后加加n 表示取第几列比如 -c 1
```
3. **案例实操**
    (1)数据准备
```sh
shitoguaji@shitoguaji:~$ vim cut.txt
shitoguaji@shitoguaji:~$ cat cut.txt
dong shen
guan zhen
wo  wo
lai  lai
le  le
```
    (2)切割 cut.txt 第一列
```sh
shitoguaji@shitoguaji:~$ cut -d " " -f 1 cut.txt
dong
guan
wo
lai
le
```
    (3)切割 cut.txt第二、三列
```sh
shitoguaji@shitoguaji:~$ cut -d " " -f 2,3 cut.txt
shen
zhen
 wo
 lai
 le
```
    (4)选取系统PATH变量值，第4个“:”开始后的所有路径:
```sh
shitoguaji@shitoguaji:~$ echo $PATH
/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin:/export/server/jdk/bin

shitoguaji@shitoguaji:~$ echo $PATH | cut -d ":" -f 4-
/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin:/export/server/jdk/bin
```

## 2 awk
一个强大的文本分析工具，把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行分析处理。  
### 1. **基本用法**
    awk [ 选项参数 ] '/patternl/{actionl} /pattern2/{action2}..' filename
    pattern: 表示awk在数据中查找的内容，就是匹配模式
    action: 在找到匹配内容时所执行的一系列命令

### 2. **选项参数说明**
```sh
    -F  # 指定输入文件分隔符
    -V  # 赋值一个用户定义变量
```

### 3. **案例实操**
    (1)搜索 passwd 文件以 root 关键字开头的所有行，并输出该行的第7列。
```sh
shitoguaji@shitoguaji:~$ cat /etc/passwd | grep ^root | cut -d ":" -f 7
/bin/bash

shitoguaji@shitoguaji:~$ cat /etc/passwd | awk -F ":" '/^root/ {print $7}'
/bin/bash
```
    (2)搜索 passwd 文件以root关键字开头的所有行，并输出该行的第1列和第7列，中间以“,”号分割。
```sh
shitoguaji@shitoguaji:~$ cat /etc/passwd | awk -F ":" '/^root/ {print $1","$7}'
root,/bin/bash
```
    注意:只有匹配了pattern的行才会执行action。  
    (3)只显示/etc/passwd的第一列和第七列,以逗号分割,且在所有行前面添加列名 user,shell 在最后一行添加 "end of file"。
```sh
shitoguaji@shitoguaji:~$ cat /etc/passwd | awk -F ":" 'BEGIN{print "user, shell"}  {print $1","$7} END{print "end of file"}'
user, shell
root,/bin/bash
daemon,/usr/sbin/nologin
...
tomcat,/bin/bash
end of file
```
    注意:BEGIN 在所有数据读取行之前执行;END在所有数据执行之后执行。  
    (4)将passwd 文件中的用户id增加数值1并输出
```sh
shitoguaji@shitoguaji:~$ awk -v i=1 -F : '{print $3+i}' passwd
1
2
3
4
```
### 4. **awk的内置变量**
```sh
变量            说明
FILENAME        # 文件名
NR              # 已读的记录数(行号)
NE              # 浏览记录的域的个数(切割后，列的个数)
```
### 5. **案例实操**
    (1)统计 passwd文件名，每行的行号，每行的列数
```sh
shitoguaji@shitoguaji:~$ awk -F ":" '{print "filename:"FILENAME " nr:"NR " nf:"NF}' /etc/passwd
filename:/etc/passwd nr:1 nf:7
filename:/etc/passwd nr:2 nf:7
filename:/etc/passwd nr:3 nf:7
...
```
    (2)查询ifconfg 命令输出结果中的空行所在的行号
```sh
shitoguaji@shitoguaji:~$ ifconfig | grep -n ^$
8:
17:
26:

shitoguaji@shitoguaji:~$ ifconfig | awk '/^$/ {print NR}'
8
17
26
```

    (3)切割 IP
```sh
shitoguaji@shitoguaji:~$ ifconfig | awk '/netmask/ {print $2}'
192.168.88.101
```
