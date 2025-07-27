# Day 3 学习笔记

## Python 部分
## 1. 字典基础
### 特性
- **键值对**存储：`{key: value}`
- **键必须不可变**：字符串/数字/元组
- **值任意类型**：支持嵌套

### 操作语法
| 操作               | 示例                          | 说明                  |
|--------------------|-------------------------------|----------------------|
| 创建字典           | `d = {"name": "Alice"}`       |                      |
| 访问值             | `d["name"]`                   | 键不存在时报错        |
| 安全访问           | `d.get("age", 18)`            | 键不存在返回默认值    |
| 添加/修改          | `d["age"] = 25`               |                      |
| 删除键值对         | `del d["name"]`               |                      |
| 遍历所有键         | `for key in d.keys():`        |                      |
| 遍历所有值         | `for value in d.values():`    |                      |
| 遍历键值对         | `for k, v in d.items():`      |                      |

## 2. 字典嵌套
### 常见嵌套结构
- **字典列表**：`[{"name": "Alice"}, {"name": "Bob"}]`
- **字典嵌套字典**：`{"user1": {"age": 25}, "user2": {"age": 30}}`

### 访问嵌套数据
users = {
    "user1": {"name": "Alice", "scores": [80, 90]},
    "user2": {"name": "Bob", "scores": [70, 85]}
}
print(users["user1"]["scores"][0])  # 输出: 80


## Linux 命令
### 1. 当日所学内容
# Linux文本处理命令详解

## 1. `cat` - 查看文件内容
### 基础用法
cat file.txt          # 查看整个文件
cat file1.txt file2.txt > combined.txt  # 合并文件
### 高级参数
cat -n file.txt       # 显示行号
cat -b file.txt       # 非空行显示行号
cat -s file.txt       # 压缩连续空行
cat -E file.txt       # 在行尾显示$符号
### 典型场景
快速查看小文件内容

合并多个配置文件

配合重定向创建新文件

## 2. `head` - 查看文件头部
### 基础用法
head file.txt         # 默认显示前10行
head -n 5 file.txt    # 显示前5行
### 高级参数
head -c 20 file.txt   # 显示前20个字节
head -q file1.txt file2.txt  # 不显示文件名标题
head -v file.txt      # 强制显示文件名标题
### 典型场景
检查日志文件开头

快速确认文件格式

大数据集采样

## 3. `grep` - 文本搜索
### 基础搜索
grep "error" file.log          # 搜索包含error的行
grep -i "warning" file.log     # 忽略大小写
grep -v "success" file.log     # 反向匹配(不包含success的行)
### 正则表达式
grep -E "[0-9]{3}" file.log   # 扩展正则(匹配3位数字)
grep -P "\d{3}" file.log      # Perl正则(需支持PCRE)
### 上下文控制
grep -A 3 "panic" file.log    # 显示匹配行及后3行
grep -B 2 "exception" file.log # 显示匹配行及前2行
grep -C 1 "critical" file.log # 显示匹配行及前后各1行
### 文件处理
grep -r "config" /etc/        # 递归目录搜索
grep -l "main" *.py           # 只显示包含匹配的文件名
grep -c "import" script.py    # 统计匹配次数
### 特殊参数
grep -n "TODO" file.py        # 显示行号
grep -b "pattern" file.bin    # 显示字节偏移量
grep --color=auto "key" file  # 高亮匹配文本