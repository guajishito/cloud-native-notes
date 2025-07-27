

## **🐍 file_ops.py（示例代码）**
```python
# -*- coding: utf-8 -*-

# ====================
# 文件读取操作
# ====================

# 场景1：读取整个文件
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("---全文读取---\n", content)

# 场景2：逐行读取
with open("example.txt", "r", encoding="utf-8") as f:
    print("---逐行读取---")
    for line in f:
        print(line.strip())  # strip() 去除首尾空白

# 场景3：读取为行列表
with open("example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("---行列表---\n", lines)

# ====================
# 文件写入操作
# ====================

# 场景4：覆盖写入（文件不存在则创建）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行内容\n")
    f.write("第二行内容\n")

# 场景5：追加写入
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的内容\n")

# 场景6：写入多行（需自行添加换行符）
lines = ["Line1\n", "Line2\n", "Line3\n"]
with open("multiline.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

