# 临时变量的作用域
for i in range(5):
    print(i)
print(i)  # 循环体外的变量实际上可以访问循环体内部的变量的，但是这么写不规范（因为没定义）

# 规范写法
i = 0
for i in range(5):
    print(i)
print(i)
