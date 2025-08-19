# shell_正则表达式入门
在Linux中，grep，sed，awk等文本处理工具都支持通过正则表达式进行模式匹配。  
## 1 常规匹配
    一串不包含特殊字符的正则表达式匹配它自己，例如：
```sh
root@shitoguaji:~$ cat /etc/passwd | grep root
```
    就会匹配所有包含 root 的行  
## 2 常用特殊字符
**(1)特殊字符:** `^`
    `^`匹配一行的开头，例如:
```sh
root@shitoguaji:~$ cat /etc/passwd | grep ^a
```
    会匹配出所有以a开头的行  
**(2)特殊字符:**`$`
    `$`匹配一行的结束，例如：
```sh
root@shitoguaji:~$ cat /etc/passwd | grep t$
```
    会匹配出所有以t结尾的行  
    思考:^$ 匹配什么?  空白行  
```sh
root@shitoguaji:~$ cat daily_archive.sh | grep -n ^$
2:
9:
20:
23:
26:
20:
32:
35:
37:
48:
50:
```
**(3)特殊字符:**`.`
    `.`匹配一个任意的字符，例如：
```sh
root@shitoguaji:~$ cat /etc/passwd grep r..t
```
    会匹配包含 rabt,rbbt,rxdt,root 等的所有行  
**(4)特殊字符:**`*`
    `*`不单独使用，他和上一个字符连用，表示匹配上一个字符0次或多次，例如：
```sh
root@shitoguaji:~$ cat /etc/passwd |grep ro*t
```
    会匹配 rt.rot.root.rooot.roooot 等所有行   
    思考:.*匹配什么?  
```sh
root@shitoguaji:~$ cat /etc/passwd | grep ^a.*in$
adm:x:3:4:adm:/var/adm:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
```
**(5)字符区间(中括号):**`[]`
```
[]表示匹配某个范围内的一个字符，例如e
[6,8]------匹配6或者8
[0-9]------匹配一个 0-9的数字
[0-9]*------匹配任意长度的数字字符串
[a-z]------匹配一个 a-z之间的字符
[a-z]*-----匹配任意长度的字母字符串
[a-c,è-f]-匹配 a-c 或者 e-f 之间的任意字符
```
```sh
root@shitoguaji:~$ cat /etc/passwd | grep r[a,b,c]*t
```
会匹配 rt, rat, rbt, rabt, rbact, rabccbaaacbt 等等所有行

**(6)特殊字符:**`\`
    `\`表示转义，并不会单独使用。由于所有特殊字符都有其特定匹配模式，当我们想匹配某一特殊字符本身时(例如，我想找出所有包含'$'的行)，就会碰到困难。此时我们就要将转义字符和特殊字符连用，来表示特殊字符本身，例如
```sh
root@shitoguaji:~$ cat /etc/passwd | grep 'a\$b'
```
    就会匹配所有包含a$b的行。注意需要使用单引号将表达式引起来