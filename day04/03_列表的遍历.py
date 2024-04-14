list_1 = [0, 1, 2, 3]
# 定义一个循环遍历函数 - while循环


def ls_while_fn(ls):
    n = 0
    while n < len(ls):
        res = ls[n]
        n += 1
        print(res)


ls_while_fn(list_1)

# 定义一个循环遍历函数 - for循环


def ls_for_fn(ls):
    for i in ls:
        res = ls[i]
        i += 1
        print(res)


ls_for_fn(list_1)

