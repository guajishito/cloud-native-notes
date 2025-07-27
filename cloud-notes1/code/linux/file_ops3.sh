#!/bin/bash
# 纯cat/grep/head实战演示

# 创建测试文件（用cat代替echo）
cat <<EOF > test.txt
=== 测试文件内容 ===
Line 1

Line 3 with error
Line 4
Last line with ERROR
EOF

# 1. cat命令演示
cat test.txt

# 2. head命令演示
head -n 3 test.txt

# 3. grep命令演示
grep "error" test.txt
grep -i "error" test.txt
grep -n "line" test.txt
grep -E "line [0-9]" test.txt

# 4. 组合使用
grep -i "error" test.txt | head -n 2

# 清理
rm test.txt