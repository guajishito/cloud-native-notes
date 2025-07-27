#!/bin/bash
# 创建测试目录
mkdir day1_demo
echo "Hello Linux" > day1_demo/test.txt

# 查看结果
ls -l day1_demo
cat day1_demo/test.txt

# 清理
rm -r day1_demo