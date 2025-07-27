from json import *

students = [
    {"name": "张三", "id": "1001", "score": 85},
    {"name": "李四", "id": "1002", "score": 92}
]


def add_student():
    try:
        name = input("姓名: ")
        stu_id = input("学号: ")
        score = float(input("成绩: "))
        students.append({"name": name, "id": stu_id, "score": score})
        print("添加成功！")
    except Exception:
        print("有错误！")

def del_student():
    if students:
        visit = False
        try:
            name = input("请输入你要删除的姓名：")
            for stu in students:
                if stu["name"] ==  name:
                    students.remove(stu)
                    visit = True
                    print("删除成功！")
        except Exception:
            print("有错误！")

        if visit == False:
            print("查无此人！")

def cha_student():
    if students:
        visit = False
        num = input("请选择你要修改的内容：\n"
                    "1.name\n"
                    "2.id\n"
                    "3.score")
        if num == 1:
            try:
                name = input("请输入你要修改的原来的姓名：")
                namenew = input("请输入你要修改后的姓名：")
                for stu in students:
                    if stu["name"] == name:
                        stu["name"] = namenew
                        visit = True
            except Exception:
                print("有错误！")
            if not visit:
                print("查无此人！")
        if num == 2:
            try:
                id = input("请输入你要修改的原来的id：")
                idnew = input("请输入你要修改后的id：")
                for stu in students:
                    if stu["id"] == id:
                        stu["id"] = idnew
                        visit = True
            except Exception:
                print("有错误！")
            if not visit:
                print("查无此人！")
        if num == 3:
            try:
                score = input("请输入你要修改的原来的id：")
                scorenew = input("请输入你要修改后的id：")
                for stu in students:
                    if stu["score"] == score:
                        stu["score"] = scorenew
                        visit = True
            except Exception:
                print("有错误！")
            if not visit:
                print("查无此人！")

# 统计平均分
def calc_average():
    if not students:
        return 0
    return sum(s["score"] for s in students) / len(students)




# 按成绩排序
def sort_by_score():
    return sorted(students, key=lambda x: x["score"], reverse=True)

# 按学号排序
def sort_by_id():
    return sorted(students, key=lambda x: x["id"], reverse=True)

# 保存到文件
def save_to_file():
    with open("D:/student.json", "w", encoding=  "UTF-8") as f:
        f.write(dumps(students))

# 从文件加载
def load_from_file():
    try:
        with open("D:/students.json", "r", encoding=  "UTF-8") as f:
            return load(f)
    except FileNotFoundError:
        return []  # 文件不存在时返回空列表