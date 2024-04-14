# if ... else...
age = 19
if age > 18:
    print("可以喝酒了")
else:
    print("好好学习")

# if ... elif ... else ...
if 12 > age > 6:
    print("小学生")
elif 18 > age > 12:
    print("中学生")
else:
    print("大学生或者幼稚园")

# if嵌套
if 0 < age < 4:
    print("无忧无虑")
elif 18 > age > 4:
    print("你上学了")
    if age < 6:
        print("还在读幼稚园")
    elif 6 < age < 11:
        print("小学")
    else:
        print("中学")
else:
    print("社会人士")
    