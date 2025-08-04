# day6

# python部分

## pymysql
### 基础使用
1. Python中使用什么第三方库来操作MySOL?如何安装?
使用第三方库为:`pymysql`
安装:`pip install pymysql`
2. 如何获取链接对象?
from pymysql import Connection 导包
`Connection`(主机,端口,账户,密码)即可得到链接对象链接对象.close()关闭和MySOL数据库的连接
3. 如何执行SOL查询
通过连接对象调用`cursor()`方法，得到游标对象
`游标对象.execute()`执行SQL语句
`游标对象.fetchall()`得到全部的查询结果封装入`元组内`

### 数据插入
1. 什么是commit提交?
pymysql库在执行对数据库有修改操作的行为时，是需要通过链接对象的`commit`成员方法来进行确认的。
`游标对象.commit()`只有确认的修改，才能生效。
2. 如何自动提交呢?
```py
# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",            # 主机名（IP）
    port=3306,                   # 端口
    user="root",                 # 账户
    password="123456",           # 密码
    autocommit=True              # 自动提交（确认）
)
```



