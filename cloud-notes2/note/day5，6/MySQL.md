# day5,6

# MySQL部分

## SQL
1. SQL:结构化查询语言，用于操作数据库，通用于绝大多数的数据库软件
2. 语法特征:
· SQL语言，`大小写不敏感`,大小写混着写也行
· SQL可以单行或多行书写，最后以`;`号结束
· SOL支持注释:
单行注释:`--`注释内容(--后面一定要有一个`空格`)
单行注释:`#`注释内容(#后面可以不加空格，推荐加上)
多行注释:`/*`注释内容 `*/`

3. SQL语言的分类
### DDL 数据定义

#### DDL-库管理
1. 查看数据库
SHOW DATABASES;
2. 使用数据库
USE 数据库名称;
3. 创建数据库
CREATE DATABASE 数据库名称 [CHARSET UTF8];    []中，指可写可不写
4. 删除数据库
DROP DATABASE 数据库名称;
5. 查看当前使用的数据库
SELECT DATABASEO();

### DDL-表管理
1. 查看有哪些表
SHOW TABLES;
**注意**:需要先选择数据库哦(use world)
2. 创建表
CREATE TABLE 表名称(
    列名称 列类型,
    列名称 列类型,
    ······
);
3. 删除表
DROP TABLE 表名称;
DROP TABLE IF EXISTS 表名称;
```sql
-- 列类型有
int                 -- 整数
float               -- 浮点数
varchar(长度)        -- 文本，长度为数字，做最大长度限制
date                -- 日期类型
timestamp           -- 时间截类型

**示例**
CREATE TABLE 表名称(
    id int,
    name varchar(10)
);
```

## DML数据操作
DML是指数据操作语言，英文全称是Data Manipulation Language，用来对数据库中表的数据记录进行更新
**注意事项**
字符串的值，出现在SOL语句中，必须要用单引号包围起来

### 数据插入 INSERT
**基础语法:**
```sql
INSERT INTO 表[(列1, 列2, ......, 列N)]VALUES(值1, 值2, ......, 值N)[, (值1, 值2, ......, 值N), ......, (值1, 值2, ......, 值N)];
```
[]中，指可写可不写
**示例:**
```sql
CREATE TABLE student(
    id INT.
    name VARCHART(20).
    age INT
);
# 仅插入id列数据
INSERT INTO student(id) VALUES(10001), (10002), (10003)
#插入全部列数据
INSERT into student(id, name, age) VALUES(10001, '周杰轮', 31), (10002, '王力鸿', 33), (10003, '林俊节', 26)
#插入全部列数据，快捷写法
INSERT INTO student VALUES(10001, '周杰轮', 31), (10002, '王力鸿', 33), (10003, '林俊节', 26)
```

### 数据删除 DELETE
条件判断:[列操作符值]
操作符:= < > <= >= != 等等，如
    id = 5
    id < 3
    id >= 6
    id != 5
**基础语法:**
```sql
DELETE FROM 表名称 [WHERE 条件判断]
```
**演示:**
```sql
DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id INT,
    name VARCHAR(20)，
    age INT
);
INSERT INTO student VALUES(10001, '周杰轮', 31), (10002, '王力鸿', 33), (10003, '林俊节', 26), (10004, '张学油', 36), (10005, '刘德滑', 30);
#删除name为林俊节的数据
DELETE FROM student WHERE name ='林俊节';   # 注意，不要忘记''
#删除age > 33 的数据
DELETE FROM student WHERE age > 33;
#删除全部数据
DELETE FROM student;
```

### 数据更新 UPDATE
**基础语法:**
```sql
UPDATE 表名SET列 = 值[WHERE 条件判断];
```
**演示:**
```sql
DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id INT,
    name VARCHAR(20),
    age INT
);
INSERT INTO student VALUES(10001, '周杰轮', 31), (10002, '王力鸿', 33), (10003, '林俊节', 26), (10004, '张学油', 36), (10005, '刘德滑', 30);
#修改id为10001的name为陈一讯
UPDATE student SET name ='陈一讯' WHERE id = 10001;
# 修改全部数据的age为11
UPDATE student sET age = 11;
```

## DQL数据查询
### 基础查询
在SQL中，通过`SELECT`关键字开头的SQL语句，来进行数据的查询
1. 基础查询的语法
```sql
SELECT 字段列表 | * FROM 表
# 含义就是:
# 从(FROM)表中，选择(SELECT)某些列进行展示
```
**演示:**
```sql
DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id INT,
    name VARCHAR(20),
    age INT
);
INSERT INTO student VALUES(10001, '周杰轮', 31), (10002, '王力鸿', 33), (10003, '林俊节', 26), (10004, '张学油', 36), (10005, '刘德滑', 30);

#查询id和name两个列
SELECT id, name FROM student;
#查询全部列
SELECT id, name, age, FROMstudent;
#查询全部列，快捷写法
SELECT * FROM student;
```
2. 过滤查询的语法
```sql
SELECT 字段列表 | * FROM 表 WHERE 条件判断
```

### 分组聚合
如:
统计班级中，男生和女生的人数。这种需求就需要
    按性别分组
    统计每个组的人数
这就称之为:分组聚合。
基础语法:
```sql
SELECT 字段|聚合函数FROM表 [WHERE条件] GROUP BY 列 
聚合函数有:
    SUM(列)求和
    AVG(列)求平均值
    MIN(列)求最小值
    MAX(列)求最大值
    COUNT(列|*)求数量
```
**演示:**
```sql
select gender, avg(age), sum(age), min(age), max(age), count(*) from student group by gender;
```
注意事项?
GROUP BY中出现了哪个列，哪个列才能出现在SELECT中的非聚合中

### 结果排序
语法:
```sql
SELECT 列|聚合函数|*FROM 表
WHERE ......
GROUP BY ......
ORDER BY [ASC|DESC]
LIMIT n[, m]
```
1. 可以对查询的结果，使用`ORDER BY`关键字，指定某个列进行排序
演示:
```sql
DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id INT,
    name VARCHAR(20),
    age INT,
    gender VARCHAR(10)
);
INSERT INTO student VALUES(10001, '周杰轮', 31, '男'), (10002, '王力鸿', 33, '男'), (10003, '林俊节', 26, '男'), (10004, '林志灵', 36, '女'), (10005, '刘德滑', 30, '男');
#按年龄降序排序结果
SELECT * FROM student ORDER BY age DESC;
#按ID升序排序结果
SELECT * FROM student WHERE age >31 ORDER BY id;
```
2. `LIMIT`关键字，对查询结果进行数量限制或分页显示
演示:
```sql
#从第二条开始显示三条
select age, count(*) from student where age > 20 order by age asc limit 1, 3;
#显示一条
select age from student where age > 20 order by age asc limit 1;
```





