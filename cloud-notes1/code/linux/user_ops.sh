#!/bin/bash
# chmod 演示

# 1. 创建测试文件（用重定向代替echo）
cat > testfile.txt <<EOF
Hello World
EOF

# 2. 显示原始权限
ls -l testfile.txt

# 3. 用数字模式修改权限
chmod 744 testfile.txt
ls -l testfile.txt

# 4. 用符号模式移除组和其他用户的读权限
chmod go-r testfile.txt
ls -l testfile.txt

# chown 演示

# 1. 创建测试文件
cat > ownerdemo.txt <<EOF
This is an ownership test
EOF

# 2. 显示原始所有者
ls -l ownerdemo.txt

# 3. 修改所有者（需提前手动创建用户）
# 先检查用户是否存在，若不存在则跳过（避免报错）
if id demo_user &>/dev/null; then
  chown demo_user ownerdemo.txt
  ls -l ownerdemo.txt
else
  ls -l ownerdemo.txt
  printf "[提示] 请先手动创建用户: sudo useradd demo_user\n"
fi