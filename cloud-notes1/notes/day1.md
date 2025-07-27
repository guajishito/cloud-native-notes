# Day 1 学习笔记

## Python 列表操作
### 1. 完整增删改查方法
- **增**：
  - `list.append(x)`：末尾添加单个元素
  - `list.extend(iterable)`：合并另一个列表
  - `list.insert(i, x)`：指定位置插入
- **删**：
  - `list.remove(x)`：删除第一个匹配项
  - `list.pop([i])`：删除并返回指定位置元素
  - `del list[i]`：删除指定位置元素
  - `list.clear()`：清空列表
- **改**：
  - `list[i] = x`：修改指定位置
  - `list[i:j] = [x,y]`：切片修改
- **查**：
  - `list.index(x)`：返回元素索引
  - `x in list`：成员检测

### 2. 切片完整语法
- `list[start:stop:step]`
- 特殊用法：
  - `list[:]`：完整复制
  - `list[::-1]`：反转
  - `list[::2]`：隔一个取一个

## Linux 命令
### 1. 当日所学内容
| 命令 | 用途 | 示例 |
|------|------|------|
| `ls` | 查看文件 | `ls -l` |
| `cd` | 切换目录 | `cd /home` |
| `mkdir` | 创建目录 | `mkdir new_dir` |
| `rm` | 删除文件 | `rm file.txt` |

### 2. 注意事项
- `rm -rf /` 会删除系统所有文件，禁止使用！
- 权限不足时用 `sudo` 或 `chmod`