# 查询某元素索引
list_1 = [1, 2, 3, 4]
print(list_1.index(3))
# 修改
list_2 = [1, 2, 3, 4, 0]
list_2[-1] = 5
print(list_2)
# 插入
list_3 = [1, 2, 3]
list_3.insert(1, 0)
print(list_3)  # [1, 0, 2, 3]
# 追加
list_4 = [0, 1, 2, 3]
list_4.append(4)
print(list_4)  # [0, 1, 2, 3, 4]
list_4.extend([5, 6, 7])
print(list_4) # [0, 1, 2, 3, 4, 5, 6, 7]

# 删除元素
list_5 = [8, 9, 10, 11, 8]
list_5.remove(8)
print(list_5)  # [9, 10, 11, 8]
del list_5[0]
print(list_5)
list_5.pop(0)
print(list_5)
list_5.clear()

print(list_5)  # []

list_6 = [1, 2, 1, 2, 3]
num = list_6.count(1)
print(num)  # 2
total_num = len(list_6)
print(total_num)  # 5

