# # continue
# # 单循环
# for i in range(0, 3):
#     print('u一')
#     continue
#     print('二')  # 跳过不执行
#
# # 嵌套循环
# for i in range(0, 3):
#     print('三')
#     for j in range(0, 5):
#         print('一')
#         continue
#         print('二')  # 跳过不执行
#     print('四')

# break
# 单循环
for i in range(0, 3):
    print('u一')
    break
    print('二')  # 循环整体结束
# 嵌套循环
for i in range(0, 3):
    print('三')
    for j in range(0, 5):
        print('一')
        break
        print('二')  # 跳过不执行
    print('四')
