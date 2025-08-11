"""
SQL案例，读取MYSQL数据库，写入文件中
"""

# from file_define import TextFileReader, JsonFileReader
# from data_define import Record
from pymysql import Connection
from json import dumps
#
# text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
# json_file_reader = JsonFileReader("D:/2011年2月销传数据JSON.txt")
#
# jan_data: list[Record] = text_file_reader.read_data()
# feb_data: list[Record] = json_file_reader.read_data()
# #将2个月份的数据合并为1个list来存储
# all_data: list[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="xstlove346@",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 执行查询性质SQL
cursor.execute("select * from orders")

results = list(cursor.fetchall())
f = open("D:/list.txt", "w", encoding="UTF-8")
for line in results:
    data_line = dumps(line)
    f.write(data_line)
    f.write("\n")
# 关闭MySOL链接对象,文件
conn.close()
f.close()