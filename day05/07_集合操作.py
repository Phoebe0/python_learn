# 集合添加元素
my_set = {0, 1, 2, 3}
my_set.add(9)
print(my_set)

# 集合删除元素
my_set.remove(0)
print(my_set)

# 清空集合
set1 = {0, 1, 2}
set1.clear()
print(set1)

# 取两个集合的差集
set2 = {0, 1, 2, 3}
set3 = {1, 4, 5, 6}
set4 = set2.difference(set3)
print(set4)

# 消除两个集合的差集 - 在集合1内部删除集合2相关的元素 - 集合1被修改，集合2不变
set2.difference_update(set3)
print(set2, set3)

# 两个集合合并成一个
set4 = {0, 1, 2}
set5 = {1, 3, 4, 5}
set6 = set4.union(set5)
print(set6)

# 统计集合元素数量
num = len(set6)
print(num)

# 集合不支持下标索引，不支持while循环遍历，可用for遍历
set7 = {0, 1, 23}
for k in set7:
    print(k)

