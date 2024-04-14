# 变量类别
n = 9
def fn():
    # num是局部变量
    num = 1
    print(num)
    print(n)
fn()
print(n)

print('--------------------')
# global关键字：在函数内部修改全局变量
def fn_1():
    global n  # 将内部变量设置为全局变量
    n = 2
    print(n)
fn_1()
print(n)

