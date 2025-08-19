# shell_流程控制(重点)
## if判断
1. **基本语法**
    (1)单分支
```sh
if [ 条件判断式 ];thenf
    程序
fi
```
    或者
```sh
if [ 条件判断式 ]
then 
    程序
fi
```
    或者
```sh
if [ 条件判断式 ];then 程序;fi
```
    (2)多分支
```sh
if [ 条件判断式 ]
then 
    程序 
elif [ 条件判断式 ]
then
    程序
else
    程序
fi
```
    注意事项:
    1.[ 条件判断式 ]，中括号和条件判断式之间必须有空格  
    2.if后要有空格  
2. **案例实操**
    (1)输入一个数字，如果是1，则输出 banzhang zhen shuai，如果是 2，则输出 cls zhen mei，如果是其他，什么也不输出。
```sh
shitoguaji@shitoguaji:~$ touch if.sh
shitoguaji@shitoguaji:~$ vim if.sh
#!/bin/bash

if [ $1 -eq 1 ]
then
    echo "banzhang zhen shuai"
elif [ $1 -eq 2 ]
then
    echo "cls zhen mei"
fi

shitoguaji@shitoguaji:~$ chmod 777 if.sh
shitoguaji@shitoguaji:~$ ./if.sh 1
banzhang zhen shuai
```
    (2)-a 代替 &&
```sh
shitoguaji@shitoguaji:~$ a=25
shitoguaji@shitoguaji:~$ if [ $a -gt 18] && [ $a -lt 35 ]; then echo OK; fi
OK

shitoguaji@shitoguaji:~$ if [ $a -gt 18 && $a -lt 35 ]; then echo OK; fi
-bash: [: 缺少 `]'

shitoguaji@shitoguaji:~$ a=20
shitoguaji@shitoguaji:~$ if [ $a -gt 18 -a $a -lt 35 ]; then echo OK; fi
OK
```
    (3)打印客户名
```sh
shitoguaji@shitoguaji:~$ vim if test.sh
#!/bin/bash

if [ "$1"x = "shitoguaji"x ]
then
    echo "welcome, shitoguaji"
fi

shitoguaji@shitoguaji:~$ chmod 777 if.sh
shitoguaji@shitoguaji:~$ ./if test.sh xiaoming
shitoguaji@shitoguaji:~$ ./if test.sh shitoguaji
welcome, shitoguaji
```

## case语句
1. **基本语法**
```sh
case $变量名 in
"值1")
    如果变量的值等于值1，则执行程序1
;;
"值2")
    如果变量的值等于值2，则执行程序2
;;
    # ...省略其他分支...
*)
    如果变量的值都不是以上的值，则执行此程序
;;
esac
```
    注意事项:  
    (1)case 行尾必须为单词“in”，每一个模式匹配必须以右括号“)”结束。  
    (2)双分号“;;”表示命令序列结束，相当于java中的 break。  
    (3)最后的“*)”表示默认模式，相当于java 中的 default。  
2. 案例实操
    输入一个数字，如果是1，则输出 banzhang，如果是2，则输出cls，如果是其它，输出renyao
```sh
shitoguaji@shitoguaji:~$ touch case.sh
shitoguaji@shitoguaji:~$ vim case.sh
#!/bin/bash

case $l in
"1")
    echo "banzhang"
;;
"2")
    echo "cls"
;;
*)
    echo "renyao"
;;
esac

shitoguaji@shitoguaji:~$ chmod 777case.sh
shitoguaji@shitoguaji:~$ ./case.sh 1
1
```

## for 循环
1. **基本语法1**
```sh
for (( 初始值;循环控制条件;变量变化 ))
do
    程序
done
```
2. **案例实操1**
    从1加到100
```sh
shitoguaji@shitoguaji:~$ touch forl.sh
shitoguaji@shitoguaji:~$ vim forl.sh

#!/bin/bash

sum=0

for ((i=0;i<=100;i++))
do
    sum=$[ $sum+$i ]
done
echo $sum

shitoguaji@shitoguaji:~$ chmod 777 forl.sh
shitoguaji@shitoguaji:~$ forl.sh
5050
```
3. **基本语法2**
```sh
for 变量 in 值1 值2 值 3... 
do
    程序
done
```
4. **案例实操2**
    (1)打印所有输入参数
```sh
shitoguaji@shitoguaji:~$ touch for2.sh
shitoguaji@shitoguaji:~$ vim for2.sh

#!/bin/bash
#打印数字

for i in cls mly wls
do
echo "ban zhang love $i"
done

shitoguaji@shitoguaji:~$ chmod 777 ./for2.sh
shitoguaji@shitoguaji:~$ ./for2.sh
ban zhang love cls
ban zhang love mly
ban zhang love wls
```
    (2)打印，从1加到100
```sh
shitoguaji@shitoguaji:~$ for os in linux windows macos; do echo $os; done
linux
windows
macos
shitoguaji@shitoguaji:~$ for i in {1..100}; do sum=$[ $sum+$i ]; done; echo $sum
5050
```
    (3)比较$*和$@区别  
    S*和S@都表示传递给函数或脚本的所有参数，不被双引号“”包含时，都以$1$2...$n的形式输出所有参数。
```sh
shitoguaji@shitoguaji:~$ vim parameter for test1.sh
#!/bin/bash

echo '==========$*=========='
for para in $*
do
    echo $para
done

echo '==========$@=========='
for para in $@
do
    echo $para
done

shitoguaji@shitoguaji:~$ chmod +x parameter for test1.sh
shitoguaji@shitoguaji:~$ ./parameter for test1.sh a b c d e
==========$*==========
a
b
c
d
e
==========$@==========
a
b
c
d
e
```
    当它们被双引号“”’包含时，$*会将所有的参数作为一个整体，以“$1$2...$n”的形式输出所有参数；S@会将各个参数分开，以“$1”“$2”...“$n”的形式输出所有参数。
```sh
shitoguaji@shitoguaji:~$ vim parameter for test2.sh
#!/bin/bash

echo '==========$*=========='
for para in "$*"
# $*中的所有参数看成是一个整体，所以这个or循环只会循环一次
do
    echo $para
done

echo '==========$@=========='
for para in "$@"
# $@中的每个参数都看成是独立的，所以"$@"中有几个参数，就会循环几次
do
    echo $para
done

shitoguaji@shitoguaji:~$ chmod +x parameter for test2.sh
shitoguaji@shitoguaji:~$ ./parameter for test2.sh a b c d e
==========$*==========
a b c d e
==========$@==========
a
b
c
d
e
```

## while 循环
1. **基本语法**
```sh
while [ 条件判断式 ]
do 
    程序
done
```
2. **案例实操**
    从1加到 100
```sh
shitoguaji@shitoguaji:~$ touch while.sh
shitoguaji@shitoguaji:~$ vim while.sh
#!/bin/bash←
sum=0
i=l
while [ $i -le 100 ]
do
    sum=$[$sum+$i]
    i=$[$i+1]
done
echo $sum
shitoguaji@shitoguaji:~$ chmod 777 while.sh
shitoguaji@shitoguaji:~$ ./while.sh
5050
```
