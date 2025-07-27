# Day 5 学习笔记

## Python 部分 - 异常处理与模块系统

## 1. 异常捕获与传递
### 1. 基础语法（5种完整情况）
#### 情况1：基础捕获
try:
    file = open("data.txt")
    print(10 / 0)
except ZeroDivisionError:
    print("除零错误发生！")

#### 情况2：捕获多个异常
try:
    int("abc")
except (ValueError, TypeError) as e:
    print(f"值或类型错误: {e}")

#### 情况3：else分支
try:
    print("正常执行")
except:
    print("异常时执行")
else:
    print("无异常时执行")

#### 情况4：finally块
try:
    file = open("data.txt")
finally:
    file.close()  # 无论是否异常都会执行

#### 情况5：捕获所有异常
try:
    import nonexist_module
except Exception as e:  # 等效于裸except
    print(f"捕获所有异常: {type(e).__name__}: {e}")

## 2. 模块系统全体系
### 1. 模块导入
#### 写法1：基础导入
import math
print(math.sqrt(4))

#### 写法2：别名导入
import pandas as pd

#### 写法3：选择性导入
from os import path, mkdir

#### 写法4：全量导入（不推荐）
from sys import *

#### 写法5：相对导入（包内使用）
from .submodule import func

#### 写法6：动态导入
module = __import__("json")

### 2. 自定义模块
文件结构
text
custom_module/
├── __init__.py     # 标识为Python包
├── math_utils.py   # 自定义模块
└── main.py         # 调用模块

## 3. 第三方包管理
### 安装包（指定版本）
pip install requests==2.28.1 flask

### 导出环境
pip freeze > requirements.txt

### 安装依赖
pip install -r requirements.txt

### 卸载包
pip uninstall flask

### 1. `if __name__ == '__main__'` 深度解析
#### 功能说明：
- 用于判断当前模块是**直接被运行**还是**被导入**
- 保护模块代码：被导入时不执行测试代码

#### 典型用法：
def calculate(x):
    return x * 2

if __name__ == '__main__':
    print("测试模式启动")  # 直接运行显示
    print(calculate(5))  # 测试函数

__all__ = ['public_func']  # 限制*导入的内容


## Linux部分

### `ps` 命令（进程快照）
1. 基础功能
静态查看当前进程状态（非实时）。

2. 完整语法及场景
ps [options]
选项组合	功能说明	示例
ps -ef	显示所有进程完整信息	`ps -ef	grep nginx`
ps -aux	显示所有用户进程及资源占用	ps -aux --sort=-%mem
ps -eLf	显示线程级信息（LWP）	`ps -eLf	grep java`
ps -p PID	查看指定PID的进程	ps -p 1234

3. 输出字段解析
UID   PID  PPID  C STIME TTY    TIME CMD
root  1    0     0 Oct01 ?    00:00:01 /sbin/init
PPID：父进程ID

STIME：进程启动时间

CMD：完整命令路径

### `top` 命令（动态监控）
1. 基础功能
实时监控系统资源和进程状态（默认3秒刷新）。

2. 所有交互指令
按键	功能	示例
M	按内存使用排序	按M后显示%MEM降序
P	按CPU使用排序	按P后显示%CPU降序
k	终止进程（需输入PID）	按k → 输入1234 → 回车
z	高亮显示运行中的进程	

3. 关键信息区域
%Cpu(s):  5.3 us,  1.2 sy,  0.0 ni, 93.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
Tasks: 150 total,  2 running, 148 sleeping,  0 stopped,  0 zombie
KiB Mem : 16.7/32000.0 [|||||||||||||||||||                     ]
us：用户空间CPU占用

id：CPU空闲率

zombie：僵尸进程数量（>0需处理）

### `kill` 命令（进程控制）
1. 基础功能
向进程发送信号（默认SIGTERM=15）。

2. 所有信号类型
信号	数值	功能	适用场景
SIGTERM	15	优雅终止（允许清理资源）	正常关闭服务
SIGKILL	9	强制终止（立即杀死）	进程无响应时
SIGHUP	1	重新加载配置	Nginx配置重载
SIGSTOP	19	暂停进程	调试进程时临时冻结
3. 完整语法
bash
kill [-信号] <PID>
killall [-信号] <进程名>
pkill [-信号] <模式>

场景	命令示例
终止单个进程	kill -9 1234
终止所有同名进程	killall -15 nginx
模糊匹配进程名终止	pkill -f "python.*flask"
