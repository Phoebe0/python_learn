# index() 查找某个数据，如果数据存在则返回对应下标，否则报错
t1 = (0, 1, 1, 2)
print(t1.index(1))  # 1
# print(t1.index(3))  # 报错

# count() 统计某个数据在当前元组出现的次数
print(t1.count(1))  # 2
# len(元组) 统计元组内的元素个数
print(len(t1))  # 4
