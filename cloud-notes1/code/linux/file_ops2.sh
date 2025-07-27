# cp命令实战
# 基础复制
cp file1.txt /backup/          # 复制到目录
cp file1.txt file2.txt         # 重命名复制

# 保留属性复制
cp -a /home/user /backup/      # 保留所有属性复制目录

# 交互式复制
cp -i *.log /logs/             # 覆盖前确认

# 创建硬链接
cp -l original.txt link.txt    # 硬链接节省空间

# mv命令实战
# 重命名文件
mv oldname.txt newname.txt     # 原地重命名

# 移动多个文件
mv *.jpg /images/             # 移动所有jpg文件

# 强制覆盖
mv -f new_data.db /db/        # 不提示直接覆盖

# 备份覆盖
mv -b updated.conf /etc/      # 原文件会被备份为/etc/updated.conf~

# find命令实战
# 按名称搜索
find /etc -name "*.conf"       # 搜索所有.conf文件

# 按类型和大小搜索
find /var/log -type f -size +10M  # 找大于10MB的文件

# 批量修改权限
find ~/projects -type d -exec chmod 755 {} \;  # 目录设755权限

# 复杂逻辑组合
find . \( -name "*.tmp" -o -name "*.bak" \) -mtime +30 -delete  # 删除30天前的临时文件