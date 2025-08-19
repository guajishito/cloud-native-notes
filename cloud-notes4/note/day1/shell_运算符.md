# shell_运算符
1. **基本语法**  
    “$((运算式))”或“$[ 运算式 ]”  
2. **案例实操：**  
    (1)计算(2+3)*4的值  
```sh
[root@hadoop100 ~]# s=$[(2+3)*4]
[root@hadoop100 ~]# echo $s
20
```
```sh
[root@hadoop100 ~]# expr 5 - 2
3
[rootGhadoop100 ~]# expr 5 * 2
expr:语法错误
[root@hadoop100 ~]# expr 5 \* 2
10
[root@hadoop100 ~]# echo $[5 * 2]
10
[root@hadoop100 ~]# echo $[5*2]
10
[root@hadoop100 ~]# echo $((5*2))
10
[root@hadoop100 ~]# a=$[6+8]
[rootGhadoop100 ~]# echo $a
14
[root@hadoop100 ~]# a=expr 5 \* 2
bash:5:未找到命令...
[root@hadoop100 ~]# a="expr 5\* 2"
[root@hadoop100 ~]# echo $a
expr 5 \* 2
[root@hadoop100 ~]# a=$(expr 5 \* 2)
[root@hadoop100 ~]# echo $a
10
[root@hadoop100 ~]# a=`expr 5 \* 2`
[root@hadoop100 ~]# echo $a
10
```
    (2)在shell中运算
```sh
[root@hadoop100 ~]# vim add.sh
[root@hadoop100 ~]# chmod +x add.sh
[root@hadoop100 ~]# ./add.sh 25 89
sum=114
```