

class Student:
    #成员变量
    name = None
    age = None

    #构造方法
    def __init__(self, name, age):
        self.name = name    #学生姓名
        self.age = age      #学生年龄
        print("构造函数")

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象，name:{self.name}，age：{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    #__eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰伦", 18)
stu2 = Student("林俊杰",13)

print(stu1)
print(stu1 < stu2)
