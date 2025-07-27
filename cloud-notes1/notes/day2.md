# Day 2 学习笔记

## Python 部分

### 列表推导式
#### 核心概念
- **定义**：通过单行表达式快速生成列表
- **语法结构**：`[expression for item in iterable if condition]`
- **执行顺序**：
  1. 遍历 iterable
  2. 执行 condition 过滤
  3. 计算 expression

## Linux 命令
### 1. 当日所学内容
[cp]
# 功能
复制文件或目录

# 语法
cp [选项] 源文件 目标文件
cp [选项] 源文件... 目标目录

# 参数详解
-a, --archive       # 归档模式，保留所有属性（等于-dpr）
-d                  # 保留软链接
-f, --force         # 强制覆盖不提示
-i, --interactive   # 覆盖前提示确认
-l, --link          # 硬链接而非复制
-p, --preserve      # 保留权限/时间戳/属主
-r, -R, --recursive # 递归复制目录
-u, --update        # 仅当源文件比目标新时复制
-v, --verbose       # 显示详细操作

# 注意事项
1. 复制软链接时默认跟随链接，加`-d`保留链接本身
2. 目标目录不存在时会自动创建父目录（需用`-r`）

[mv]
# 功能
移动或重命名文件/目录

# 语法
mv [选项] 源文件 目标文件
mv [选项] 源文件... 目标目录

# 参数详解
-b, --backup        # 覆盖前备份目标文件
-f, --force         # 强制覆盖不提示
-i, --interactive   # 覆盖前提示确认
-n, --no-clobber    # 禁止覆盖已有文件
-u, --update        # 仅当源文件比目标新时移动
-v, --verbose       # 显示详细操作

# 特殊情况
1. 跨文件系统移动大文件时相当于"复制+删除"
2. 重命名操作不需要`-r`参数

[find]
# 功能
递归搜索目录中的文件

# 语法
find [路径] [表达式]

# 常用表达式
-name "模式"       # 按文件名匹配（支持通配符*?）
-iname "模式"      # 不区分大小写匹配
-type [fdc]       # 按类型筛选(f文件/d目录/c设备)
-size [+-]n[cwkMG] # 按大小筛选(+n大于,-n小于)
-mtime [+-]n      # 按修改时间筛选（天）
-exec 命令 {} \;   # 对搜索结果执行命令
-print            # 打印结果（默认）

# 组合示例
1. 找7天内修改的.log文件：  
   `find /var -name "*.log" -mtime -7`
2. 删除空目录：  
   `find . -type d -empty -exec rmdir {} \;`