import random

money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)
    print(score)
    if score < 5:
        print('不发工资')
        continue
    # 判断余额是否充足,充足的情况
    if money >= 1000:
        money -= 1000
        print(f'发1000块，还剩{money}')
    # 不充足
    else:
        print('余额不足')
        break
