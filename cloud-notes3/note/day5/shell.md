# day5_Shell脚本入门
## 1 脚本格式
  脚本以`#!/bin/bash`开头(指定解析器)  
## 2 第一个Shell 脚本:helloworld.sh
  (1)需求:创建一个 Shell 脚本，输出 helloworld  
  (2)案例实操:  
```sh
shitoguaji@shitoguaji:~/scripts$ touch helloworld.sh
shitoguaji@shitoguaji:~/scripts$ vim helloworld.she
# 在 helloworld.sh 中输入如下内容
#!/bin/bash
echo "helloworld"
```
  (3)脚本的常用执行方式  
  第一种:采用`bash`或`sh`+脚本的相对路径或绝对路径(不用赋予脚本+x权限)  
  sh+脚本的相对路径  
```sh
shitoguaji@shitoguaji:~/scripts$ sh ./helloworld.sh
helloworld
```
  sh+脚本的绝对路径  
```sh
shitoguaji@shitoguaji:~/scripts$ sh /home/shitoguaji/sctipts/helloworld.sh
helloworld
```
  bash+脚本的相对路径  
```bash
shitoguaji@shitoguaji:~/scripts$ bash ./helloworld.sh
helloworld
```
  bash+脚本的绝对路径  
```bash
shitoguaji@shitoguaji:~/scripts$ bash /home/shitoguaji/sctipts/helloworld.sh
helloworld
```
  第二种:采用输入脚本的绝对路径或相对路径执行脚本`(必须具有可执行权限+x)`  
  1.首先要赋予 belloworld.sh 脚本的+x 权限  
```bash
shitoguaji@shitoguaji:~/scripts$ chmod +x helloworld.sh
```
  2.执行脚本
  相对路径
```bash
shitoguaji@shitoguaji:~/scripts$ ./helloworld.sh
helloworld
```
  绝对路径
```bash
shitoguaji@shitoguaji:~/scripts$ /home/shitoguaji/sctipts/helloworld.sh
helloworld
```
  注意:第一种执行方法，本质是bash解析器帮你执行脚本，所以脚本本身不需要执行权限。第二种执行方法，本质是脚本需要自己执行，所以需要执行权限。
  【了解】第三种:在脚本的路径前加上“.”，或者 source
```bash
shitoguaji@shitoguaji:~/scripts$ source helloworld.sh
helloworld
shitoguaji@shitoguaji:~/scripts$ . helloworld.sh
helloworld
```
  原因:  
  1.前两种方式都是在当前 shel 中打开一个子shell 来执行脚本内容，当脚本内容结束，则子 shell 关闭，回到父 shell 中。  
  2.第三种，也就是使用在脚本路径前加“.”或者source 的方式，可以使脚本内容在当前shell 里执行，而无需打开子 shell!这也是为什么我们每次要修改完/etc/profile 文件以后，需要 source 一下的原因。  
  3.开子 shell 与不开子 shel 的区别就在于，`环境变量`的继承关系，如在子shell 中设置的当前变量，父shell 是不可见的。  
```bash
shitoguaji@shitoguaji-VMware-Virtual-Platform:~/scripts$ ps -f
UID          PID    PPID  C STIME TTY          TIME CMD
shitogu+    3412    3405  0 14:55 pts/0    00:00:00 bash
shitogu+    3860    3412  0 15:24 pts/0    00:00:00 ps -f
shitoguaji@shitoguaji-VMware-Virtual-Platform:~/scripts$ bash
shitoguaji@shitoguaji-VMware-Virtual-Platform:~/scripts$ ps -f
UID          PID    PPID  C STIME TTY          TIME CMD
shitogu+    3412    3405  0 14:55 pts/0    00:00:00 bash
shitogu+    3864    3412  0 15:25 pts/0    00:00:00 bash
shitogu+    3870    3864 99 15:25 pts/0    00:00:00 ps -f
shitoguaji@shitoguaji-VMware-Virtual-Platform:~/scripts$ exit
exit
shitoguaji@shitoguaji-VMware-Virtual-Platform:~/scripts$ ps -f
UID          PID    PPID  C STIME TTY          TIME CMD
shitogu+    3412    3405  0 14:55 pts/0    00:00:00 bash
shitogu+    3871    3412 99 15:26 pts/0    00:00:00 ps -f
```
  以上输入bash，进入新的子bash  
  输入exit，退出子bash  