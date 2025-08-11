# day3_python部分

## Python执行Linux命令
### 1 执行简单命令 subprocess.run()
下面是一个例子，我们将使用 Python 执行 ls 命令，列出当前目录下的文件和文件夹：
```py
import subprocess

result = subprocess.run(['ls'], capture_output=True, text=True)
print(result.stdout)
```
**代码解释**：  
`subprocess.run(['ls'])` 调用系统命令 ls，并等待命令执行完毕。  
`capture_output=True` 表示将命令的输出结果捕获到变量 result 中。  
`text=True` 表示将命令的输出结果以文本形式返回。  
上述代码执行结果将输出当前目录下的文件和文件夹的列表。  

### 2 执行带参数的命令 
在subprocess.run() 方法中传入命令及其参数列表来执行带参数的命令。  
下面是一个例子，我们将使用 Python 执行 grep 命令在文件中查找包含特定文本的行：
```py
import subprocess

result = subprocess.run(['grep', 'pattern', 'file.txt'], capture_output=True, text=True)
print(result.stdout)
```
**代码解释**：  
subprocess.run(['grep', 'pattern', 'file.txt']) 执行带参数的命令 `grep pattern file.txt`。  
上述代码执行结果将输出包含特定文本的行。  

### 3 处理命令的输出结果
subprocess.run() 方法返回的 result 对象包含命令的`执行结果、输出结果、错误信息等`。  
1. **获取命令的执行结果**
`result.returncode` 的值为 0 表示命令执行成功，非 0 表示命令执行失败。  

下面是一个例子，我们将使用 Python 执行 ls 命令，并检查命令的执行结果是否成功：  
```py
import subprocess

result = subprocess.run(['ls'], capture_output=True, text=True)
if result.returncode == 0:
    print("Command executed successfully")
else:
    print("Command execution failed")
```
**代码解释**：  
`result.returncode` 获取命令的执行结果。  

2. **获取命令的输出结果**
`result.stdout` 存储命令的标准输出结果。  
下面是一个例子，我们将使用 Python 执行 ls 命令，并打印出命令的输出结果：  
```py
import subprocess

result = subprocess.run(['ls'], capture_output=True, text=True)
print(result.stdout)
```
**代码解释**：  
`result.stdout` 获取命令的输出结果。  

3. **处理命令的错误信息**
`result.stderr` 存储命令的标准错误输出。  
下面是一个例子，我们将使用 Python 执行错误的命令，并打印出命令的错误信息：  
```py
import subprocess

result = subprocess.run(['wrong_command'], capture_output=True, text=True)
print(result.stderr)
```
**代码解释**：  
`result.stderr` 获取命令的错误信息。  

### 4 使用管道连接命令
subprocess.run() 方法允许我们使用管道 (|) 连接多个命令，实现命令的串联执行。  

下面是一个例子，我们将使用 Python 执行 ls -l | grep pattern 这个命令组合，实现先列出当前目录下的文件和文件夹的详细信息，然后通过 grep 命令筛选包含特定文本的行：  
```py
import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
ls_output = result.stdout

result = subprocess.run(['grep', 'pattern'], input=ls_output, capture_output=True, text=True)
grep_output = result.stdout

print(grep_output)
```
**代码解释**：  
第一个 `subprocess.run(['ls', '-l'])` 命令执行 `ls -l`，并将结果存储到 `ls_output` 变量中。  
第二个 `subprocess.run(['grep', 'pattern']`, `input=ls_output` 命令执行 `grep pattern`，并将 ls_output 作为输入。  
打印出 grep 命令的输出结果。  
上述代码执行结果将输出包含特定文本的行。  

### 5 阻塞与非阻塞执行 subprocess.Popen()
在默认情况下，subprocess.run() 方法是`阻塞`的，即 *Python 代码会等待命令执行完成后才会继续往下执行*。  

如果需要使用`非阻塞`的方式执行命令，可以使用 `subprocess.Popen()` 方法。  

下面是一个例子，我们将使用 Python 非阻塞地执行 ping 命令：
```py
import subprocess

subprocess.Popen(['ping', 'example.com'])
print("Command executed in non-blocking mode")
```
**代码解释**：  
`subprocess.Popen(['ping', 'example.com'])` 使用非阻塞方式执行 ping 命令。  
print() 函数直接打印出文字，而不需要等待命令执行完成。  
上述代码执行后，程序将立即打印出 “Command executed in non-blocking mode”，而不需要等待 ping 命令执行完成。  
