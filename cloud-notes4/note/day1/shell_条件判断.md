# shell_条件判断
1. **基本语法**
    (1)test condition  
    (2)[ condition ](`注意 condition 前后要有空格`)  
    注意:条件非空即为true(0)，[ atguigu ]返回 true(0),[  ]返回 false(1)。  
2. **常用判断条件**  
    (1)两个整数之间比较
```shell
    -eq 等于(equal)
    -lt 小于(less than)
    -gt 大于(greater than)
    -ne 不等于(not equal)
    -le 小于等于(less equal)
    -ge 大于等于(greater equal)
```
    注:如果是字符串之间的比较，用等号“=”判断相等；用“!=”判断不等。  
    (2)按照文件权限进行判断  
```shell
    -r 有读的权限(read)
    -w 有写的权限(write)
    -x 有执行的权限(execute)
```
    (3)按照文件类型进行判断  
```shell
    -e 文件存在(existence)
    -f 文件存在并且是一个常规的文件(fle)
    -d 文件存在并且是一个目录(directory)
```
3. **案例实操**
    (1)23是否大于等于22
```sh
[atguigu@hadoop10l shells]$ [ 23 -ge 22 ]
[atguigu@hadoop10l shells]$ echo $?
0
```
    (2)helloworld.sh是否具有写权限
```sh
[atquiqu@hadoop10l shells]$ [ -w helloworld.sh ][atquigu@hadoop10l shells]$ echo $?
1
```
    (3)/home/atguigu/cls.txt目录中的文件是否存在
```sh
[atguigu@hadoop101 shells]$ [ -e /home/atguigu/cls.txt ][atguigu@hadoop101 shells]$ echo s?
1
```
    (4)多条件判断(&&表示前一条命令执行成功时，才执行后一条命令，"表示上一条命令执行失败后，才执行下一条命令)
```sh
[atguigu@hadoop101 ~]$ [ atguigu ] && echo OK || echo notOK
OK
[atguigu@hadoop101 shells]$ [  ] && echo OK || echo notOK
notOK
[root@hadoop100 scripts]# a=15
[root@hadoop100 scripts]# [ $a -lt 20 ] && echo "$a < 20" || echo "$a >= 20"
15<20
```
    (5)基本语法
```sh
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ a=hello
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $a
hello
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ test $a = hello
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
0
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ test $a = Hello
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
1
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ [ $a = hello ]
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
0
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ [ $a = Hello ]
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
1
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ [ $a=Hello ]
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
0
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ [ asfdsffgsdg ]
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
0
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ [  ]
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
1
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ [ $a != Hello ]
shitoguaji@shitoguaji-VMware-Virtual-Platform:~$ echo $?
0
```