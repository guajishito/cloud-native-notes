# day5_Shell_变量
## 1 系统预定义变量
1. **常用系统变量**  
  $HOME、$PWD、$SHELL、$USER 等  
2. **案例实操**  
  (1)查看系统变量的值  
```bash
shitoguaji@shitoguaji:~$ echo $HOME
/home/shitogauji
```
  (2)显示当前Shell中所有变量：**set**  
```bash
shitoguaji@shitoguaji:~$ set
BASH=/bin/bash
BASH ALIASES=()
BASH ARGC=()
BASH ARGV=()
...
```
  (3)查看所有系统全局变量  
```bash
shitoguaji@shitoguaji:~$ env
SHELL=/bin/bash
SESSION_MANAGER=local/shitoguaji:@/tmp/.ICE-unix/2630,unix/shitoguaji:/tmp/.ICE-unix/2630
...
shitoguaji@shitoguaji:~$ printenv
SHELL=/bin/bash
SESSION_MANAGER=local/shitoguaji:@/tmp/.ICE-unix/2630,unix/shitoguaji:/tmp/.ICE-unix/2630
...

shitoguaji@shitoguaji:~$ printenv USER
shitoguaji
shitoguaji@shitoguaji:~$ printenv HOME
/home/shitoguaji
```
## 2 自定义变量
1. **基本语法**  
  (1)定义变量：变量名=变量值，**注意，=号前后不能有空格**  
  (2)撤销变量：unset 变量名  
  (3)声明静态（只读）变量：readonly变量，注意:不能unset  
  (4)声明成全局变量：export 变量名  
2. **变量定义规则**  
  (1)变量名称可以由字母、数字和下划线组成，但是不能以数字开头，环境变量名建议大写。  
  (2)等号两侧不能有空格  
  (3)在bash中，变量默认类型都是字符串类型，无法直接进行数值运算。  
  (4)变量的值如果有空格，需要使用双引号或单引号括起来。  

3. **案例实操**  
  (1)定义变量A  
```bash
shitoguaji@shitoguaji:~$ A=5
shitoguaji@shitoguaji:~$ echo $A
5
```
  (2)给变量A重新赋值  
```bash
shitoguaji@shitoguaji:~$ A=8
shitoguaji@shitoguaji:~$ echo $A
8
```
  (3)撤销变量A  
```bash
shitoguaji@shitoguaji:~$ unset A
shitoguaji@shitoguaji:~$ echo $A
```
  (4)声明静态的变量 B=2，不能 unsete  
```bash
shitoguaji@shitoguaji:~$ readonly B=2
shitoguaji@shitoguaji:~$ echo $B
2
shitoguaji@shitoguaji:~$ B=9
-bash: B: readonly variable
```
  (5)在bash中，变量默认类型都是字符串类型，无法直接进行数值运算  
```bash
shitoguaji@shitoguaji:~$ C=1+2
shitoguaji@shitoguaji:~$ echo $C
1+2
```
  (6)变量的值如果有空格，需要使用双引号或单引号括起来  
```bash
shitoguaji@shitoguaji:~$ D=I love banzhang
-bash: world: command not found
shitoguaji@shitoguaji:~$ D="I love banzhang"
shitoguaji@shitoguaji:~$ echo $D
I love banzhang
```
  (7)可把变量提升为全局环境变量，可供其他Shell程序使用  
```bash
export 变量名
shitoguaji@shitoguaji:~$ vim helloworld.sh
```
  在 helloworld.sh文件中增加 echo $B  
```bash
#!/bin/bashe
echo "helloworld"←
echo $B

shitoguaji@shitoguaji:~$ ./helloworld.sh
helloworld
```
  发现并没有打印输出变量B的值  
```bash
shitoguaji@shitoguaji:~$ export B
shitoguaji@shitoguaji:~$ ./helloworld.sh
helloworld
2
```
## 3 特殊变量
1. $n  
  (1)**基本语法**  
    $n  （功能描述：n为数字，$0代表该脚本名称，$1-&9代表第一到第九个参数，十以上的参数，十以上的参数需要用大括号包含，如${10}）  
  (2)**案例实操**  
```bash
shitoguaji@shitoguaji:~$ touch parameter.sh
shitoguaji@shitoguaji:~$ vim parameter.sh

#!/bin/bash
echo '==========$n=========='
echo $0
echo $1
echo $2

shitoguaji@shitoguaji:~$ chmod 777 parameter.sh
shitoguaji@shitoguaji:~$ ./parameter.sh cls xz
==========$n==========
./parameter.sh
cls
xz

shitoguaji@shitoguaji:~$ basename
parameter.sh
```
2. $#  
  (1)**基本语法**  
    S#  （功能描述：获取所有**输入参数个数**，常用于循环,判断参数的个数是否正确以及加强脚本的健壮性）。  
  (2)**案例实操**  
```bash
shitoguaji@shitoguaji:~$ vim parameter.sh
#!/bin/bash
echo '==========$n=========='
echo $0
echo $1
echo $2
echo '==========$#=========='
echo $#

shitoguaji@shitoguaji:~$ chmod 777 parameter.sh
shitoguaji@shitoguaji:~$ ./parameter.sh cls xz
==========$n==========
./parameter.sh
cls
xz
==========$#==========
2
```
3. $*、$@  
  (1)基本语法  
    `$*`  （功能描述：这个变量代表命令行中所有的参数，**$* 把所有的参数看成一个整体**）
    `$@`  （功能描述：这个变量也代表命令行中所有的参数,不过***$@ 把每个参数区分对待**）  
  (2)案例实操  
```bash
shitoguaji@shitoguaji:~$ vim parameter.sh
#!/bin/bash
echo '==========$n=========='
echo $0
echo $1
echo $2
echo '==========$#=========='
echo $#
echo '==========$*=========='
echo $*
echo '==========$@=========='
echo $@

shitoguaji@shitoguaji:~$ ./parameter.sh a b c d e f g 
==========$n==========
./parameter.sh
a
b
==========$#==========
7
==========$*==========
a b c d e f g
==========$@==========
a b c d e f g
```

4. $?  
  (1)**基本语法**  
    S?  （功能描述：最后一次执行的命令的返回状态。如果这个变量的值为0，证明上一个命令正确执行；如果这个变量的值为非0（具体是哪个数，由命令自己来决定），则证明上一个命令执行不正确了。）  
  (2)**案例实操**  
    判断 helloworld.sh 脚本是否正确执行
```bash
shitoguaji@shitoguaji:~$ /helloworld.sh
helloworld
shitoguaji@shitoguaji:~$ echo $?
0