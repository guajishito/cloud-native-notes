# 字典基础操作
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}

# 1. 访问值
print(student["name"])          # 输出: Alice
print(student.get("gender", "Unknown"))  # 输出: Unknown

# 2. 修改值
student["age"] = 21

# 3. 遍历字典
for key, value in student.items():
    print(f"{key}: {value}")

# 4. 删除键值对
del student["courses"]

# 字典嵌套示例
company = {
    "departments": {
        "IT": {"head": "John", "staff": 15},
        "HR": {"head": "Lisa", "staff": 8}
    },
    "locations": ["New York", "London"]
}

# 1. 访问嵌套数据
print(company["departments"]["IT"]["head"])  # 输出: John

# 2. 修改嵌套数据
company["departments"]["HR"]["staff"] = 10

# 3. 动态添加嵌套结构
company["departments"]["Finance"] = {"head": "Mike", "staff": 5}