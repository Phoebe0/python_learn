# 列表切片
list1 = [0, 1, 2, 3]
new_list1 = list1[0:2:1]
print(new_list1)

# 元组切片
t1 = (0, 1, 2, 3, 4, 5)
new_t1 = t1[0:4:2]
print(new_t1)

# 对字符串切片  步长为负
str1 = 'Hello World'
# 从下标8开始到下表为0结束
new_str1 = str1[8:0:-1]
print(new_str1)
# 从头到尾倒序步长为-2
new_str2 = str1[::-2]
print(new_str2)
