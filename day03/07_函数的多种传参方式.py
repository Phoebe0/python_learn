# 位置参数
# 传递参数和定义参数的顺序及个数必须一致
def fn1(name, age, gender):
    print(f'hi. My name is {name}, {age} years old, i am a {gender}')


fn1('Tricia', 18, 'girl')

# 关键字参数
# 函数调用时通过 键 = 值 的形式传递参数
fn1( age=23, name='Yy', gender='boy')

# 缺省参数


def fn2(name, age, gender='girl'):
    print(f'hi. My name is {name}, {age} years old, i am a {gender}')


fn2('Fff', 43)

# 不定长参数
# 位置传递
def fn3(*args):
    print(args)


fn3('YOU', 89)

# 关键字传递
def fn4(**kwargs):
    print(kwargs)


fn4(name='Tt', age=18)