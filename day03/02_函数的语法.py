# 定义函数 函数必须先定义后使用
def hello():
    print('你好python')
# 调用函数
hello()

# 函数传入参数
def add(num1, num2):
    sum = 0
    sum = num1 + num2
    print(sum)
add(4,2)

# 返回值
def dev(x1,x2):
    num = x1 - x2
    return num
n = dev(3,1)
print(n)

# 无return语句的函数返回值
def no_r():
    print('no')
res1 = no_r()
print(res1)  # 返回none值

# none在if中的应用
def check_age(age):
    if age > 18:
        return '成年'
    else:
        return None
res2 = check_age(17)
if not res2:
    print('未成年哦')
# None用于声明无初始内容的变量
name = None

# 练习1
def check(money):
    if money >= 100:
        print(f'有钱人，你的金钱为{money}元！')
    else:
        print(f'穷鬼，才{money}快钱，爬')
check(8089)