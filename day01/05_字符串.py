name = 'Tricia'
age = 18.5
year = 2005
# 占位拼接   %s表示要占位的位置
msg = '你好，%s,年龄：%.2f，出生年份：%d' % (name, age, year)
print(msg)
num = 23.6
print('%6.2f' % num)
# f"{}"进行占位
msg1 = f'你好, {name}, 年龄{age}, 出生：{year} '
print(msg1)

# 练习
company = '金仕达'
employee = 1560
salary = 11000.45
number = 1.5
print(f"公司{company}, 人数{employee}")
print("工资是%.2f, 希望涨%.1f倍薪水"%(salary, number))
