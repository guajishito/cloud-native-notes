
#定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好啊，我是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name}, {msg}")


stu = Student()
stu.name = "周杰伦"
stu.say_hi()
stu.say_hi2("你好")