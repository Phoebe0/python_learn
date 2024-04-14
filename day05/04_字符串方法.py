str = 'a b cdefgg'
# index
print(str.index("d"))  # 5

# replace  字符串替换
# 语法：字符串.replace(字符串1, 字符串2)   这个并没有修改字符串本身，而是得到了新的字符串。
new_str = str.replace('a', 'v')
print(new_str)

# split 字符串分割，存入列表
list1 = str.split(' ')
print(list1)

# strip  去除前后空格
str2 = ' adbg '
print(str2.strip())
# strip  去除前后指定字符串
str3 = '11aaa'
print(str3.strip('11'))
# 统计字符串中某字符串出现的次数  count()
str4 = 'aaaaab'
print(str4.count('a'))

# 统计字符串长度 len()
print(len(str4))
