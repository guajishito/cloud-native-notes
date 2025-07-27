#如下嵌套列表，要求对外层列表进行排序，排序的依据是内层列表的第二个元素数宁
#以前学习的sorted函数就无法适用了。可以使用列表的sort方法

#法1：函数
my_list =[["a", 33], ["b", 55], ["c", 11]]

#定义排序方法
def choose_sort_key(element):
    return element[1]

#将元素传入choose sort key函数中，用来确定按照谁来排序
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)


#法2：lambda
my_list =[["a", 33], ["b", 55], ["c", 11]]
my_list.sort(key=lambda element: element[1],reverse=True)
print(my_list)