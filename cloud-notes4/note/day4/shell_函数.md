# shell_函数
## 1 系统函数
### 1.1 basename
1. **基本语法**
    basename 命令会删掉所有的前basename [string/pathname][suffix]       (功能描述:缀包括最后一个('/')字符，然后将字符串显示出来。)  
    basename 可以理解为取路径里的文件名称    
    选项:  
    suffix 为后缀,如果 sufx被指定了,basename 会将 pathname 或 string 中的 suffix 去掉。  
2. **案例实操**
    截取该/home/atguigu/banzhang.txt路径的文件名称。
```sh
shitoguaji@shitoguaji:~$ basename /home/atquigu/banzhang.txt
banzhang.txt
shitoguaji@shitoguaji:~$ basename /home/atquiqu/banzhang.txt .txt
banzhang
```
### 1.2 dirname
1. **基本语法**
    dirname 文件绝对路径    (功能描述:从给定的包含绝对路径的文件名中去除文件名(非目录的部分)，然后返回剩下的路径(目录的部分))  
    dirname 可以理解为取文件路径的绝对路径名称  
2. **案例实操**
    获取 banzhang.txt 文件的路径。
```sh
shitoguaji@shitoguaji:~$ dirname /home/atquiqu/banzhang.txt
/home/atquiqu
```
```sh
shitoguaji@shitoguaji:~$ vim parameter.sh
#!/bin/bash
echo '==========$n=========='
echo script name: $(basename $0 .sh)
echo script path: $(cd $(dirname $0); pwd)
echo 1nd parameter: $1
echo 2nd parameter: $2
echo '==========$#=========='
echo parameter number: $#
echo '==========$*=========='
echo $*
echo '==========$@=========='
echo $@



shitoguaji@shitoguaji:~$ chmod +x parameter.sh
shitoguaji@shitoguaji:~$ ./parameter.sh a b
==========$n==========
script name: parameter
script path: /root/scripts
1nd parameter: a
2nd parameter: b
==========$#==========
7
==========$*==========
a b
==========$@==========
a b
```

## 2 自定义函数
1. **基本语法**
    [ function ] funname[ 0 ]{  
        Action;  
        [return int;]  
    }  
    [ ] 表示可选  
2. **经验技巧**
    (1)必须在调用函数地方之前，先声明函数，shell 脚本是逐行运行。不会像其它语言样先编译。  
    (2)函数返回值，只能通过$?系统变量获得，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。return 后跟数值 n(0-255)  
3. **案例实操**
    计算两个输入参数的和。  
```sh
shitoguaji@shitoguaji:~$ vim fun_test.sh
#!/bin/bash

function add(){
        s=$[$1 + $2]
        echo "和："$s
}

read -p "请输入第一个整数：" a
read -p "请输入第二个整数：" b

add $a $b

shitoguaji@shitoguaji:~$ chmod +x fun_test.sh
shitoguaji@shitoguaji:~$ ./fun test.sh
请输入第一个整数: 35
请输入第二个整数: 67
和: 102
```

    取得返回值。
```sh
shitoguaji@shitoguaji:~$ vim fun_test2.sh
#!/bin/bash

function add(){
        s=$[$1 + $2]
        echo $s
}

read -p "请输入第一个整数：" a
read -p "请输入第二个整数：" b

sum=$(add $a $b)
echo "和："$sum

shitoguaji@shitoguaji:~$ chmod +x fun_test2.sh
shitoguaji@shitoguaji:~$ ./fun test2.sh
请输入第一个整数: 35
请输入第二个整数: 67
和: 102

```



