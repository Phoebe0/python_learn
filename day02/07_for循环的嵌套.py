# 循环打印99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # 内层循环输出每一行数据
        print(f'{j} * {i} = {i * j}\t', end='')
    # 外层循环控制换行
    print()
