# while 遍历 元组
t = (0, 1, 2, 3, 3)
index = 0
while index < len(t):
    print(t[index])
    index += 1
# for循环遍历 元组
for i in t:
    print(t[i])

# 虽然元组不可修改，但是元组中的list可以修改
t2 = (0, 11, ['Tt', 'Oo'])
t2[2][0] = 'Xx'
print(t2)
