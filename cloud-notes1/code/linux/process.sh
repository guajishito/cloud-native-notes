ps -ef                  # 查看所有进程（完整格式）
ps aux                  # 查看所有进程（含CPU/内存）
ps -u root              # 查看指定用户的进程
ps -p 1234              # 查看指定PID的进程
ps -eLf                 # 查看线程信息

ps aux --sort=-%mem     # 按内存使用降序排列

top -p 1234             # 只监控指定PID
top -u root             # 只监控root用户的进程

kill 1234               # 正常终止进程（信号15）
kill -9 1234            # 强制终止进程（信号9）
kill -l                 # 查看所有信号