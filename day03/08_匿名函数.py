# 函数作为参数传入
def add(a, b):
    return a + b

def fn1(f):
    res = f(1, 2)
    print(res)

fn1(add)


# lambda 定义匿名函数
def fn2(f):
    res = f(14, 4)
    print(res)


fn2(lambda x, y: x - y)
