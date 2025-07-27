# 列表增删改查
fruits = ["apple", "banana"]
fruits.append("orange")  # 增加
fruits.remove("apple")   # 删除
fruits[0] = "mango"     # 修改
print(fruits[1])        # 查询

# 列表切片
nums = [1, 2, 3, 4, 5]
print(nums[1:3])  # 输出 [2, 3]
print(nums[::-1]) # 输出 [5, 4, 3, 2, 1]