

def layer1():
    raise ValueError("原始错误")

def layer2():
    try:
        layer1()
    except ValueError as e:
        print(f"第二层捕获: {e}")
        raise  # 重新抛出

try:
    layer2()
except ValueError as e:
    print(f"最外层捕获: {e}")