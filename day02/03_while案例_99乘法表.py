# 单行打印 print('内容', end = '')
# 多行之间对齐使用制表符  \t

# 定义外层循环初始值
i = 1
while i <= 9:
    # 定义内层循环初始值
    j = 1
    while j <= i:
        print(f'\t{j}✖️{i} = {i * j}', end='')
        j += 1
    i += 1
    # 打印空行，实现换行
    print()
