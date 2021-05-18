import random
suiji_num=random.randint(1,100)
print('游戏开始')
for i in range(1,11):
    num = int(input('请输入一个整数：'))
    if num>suiji_num:
        print('大了')
    elif num<suiji_num:
        print('小了')
    elif num==suiji_num:
        print('恭喜你猜对了')
        break
if i<5:
    print('真聪明！')
elif i<7:
    print('不算笨')
else:
    print('你可能不太聪明')
input('Press <Enter>')