"""
 数据类型
 Number(包含整型、浮点型、布尔型、复数)

"""
# Number
a = 10
b = 1.2
c = True
d = 4+3j
print(a, b, c, d)

# 使用print直接输出类型
print(type(10))
# 使用变量存储type()的结果
ty = type("执行")
print(ty)
# 使用type()查看变量中存储的数据类型
money = 10000.89
print(type(money))
# 使用instance判断数据类型


# 数据类型转换
num_str = str(10)
print(num_str, type(num_str))
str_num = int("22")
print(str_num, type(str_num))
float_num = int(13.14)
print(float_num, type(float_num))
str_float = float("77.8888")
print(str_float, type(str_float))

