# 5类数据容器
my_list = [0, 1, 2, 3]
my_tuple = (0, 1, 2, 3)
my_str = 'abcdefg'
my_set = {0, 1, 2, 3}
my_dict = {"a": 1, "A": 2}

# len - 统计元素个数
print(f'数组的元素个数是{len(my_list)}')

# max - 统计最大元素
print(f'元组中最大的元素是{max(my_tuple)}')

# min - 统计最小元素
print(f'字典中最小的元素是{max(my_dict)}')

# 容器之间的转换
# list(容器) - 将给定容器转换为列表
# str(容器) - 将给定容器转换为字符串
# tuple(容器) - 将给定容器转换为元组
# set(容器) - 将给定容器转换为集合


# 容器的排序功能
# sorted(容器,[reverse = True])   -- reverse 表示排序结果是否进行反转
# 排序的结果是会都变成列表对象

my_list1 = [0, 6, 3, 4, 1, 2, 5]
my_tuple1 = (0, 6, 3, 4, 1, 2, 5)
print(sorted(my_list1))
print(sorted(my_tuple1, reverse= True))
