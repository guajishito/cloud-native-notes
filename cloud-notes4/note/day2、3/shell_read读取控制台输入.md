# shell_read读取控制台输入
1. **基本语法**
```sh
read (选项) (参数)
```
    (1)选项:  
        -p:指定读取值时的提示符；  
        -t:指定读取值时等待的时间(秒)，如果-t不加表示一直等待  
    (2)参数  
        变量:指定读取值的变量名  
2. **案例实操**
    提示7秒内，读取控制台输入的名称
```sh
shitoguaji@shitoguaji:~$ vim read.sh
#!/bin/bash
read -t 10 -p "请输入您的芳名：" name
echo "welcome, $name"

shitoguaji@shitoguaji:~$ chmod +x test.sh
shitoguaji@shitoguaji:~$ ./read test.sh
请输入您的芳名：shitoguaji
welcome, shitoguaji
```