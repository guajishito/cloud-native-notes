# 基础示例：生成平方数列表
squares = [x**2 for x in range(10)]

# 带条件的推导式：筛选偶数
evens = [x for x in range(20) if x % 2 == 0]

# 多重循环：笛卡尔积
pairs = [(x, y) for x in [1,2] for y in [3,4]]