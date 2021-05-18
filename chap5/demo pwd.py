'''从键盘录入密码，最多录入三次，如果正确就结束循环'''

for item in range(3):
    pwd=input('请输入您的密码：')
    if pwd=='888888':
        print('密码正确')
        break
    else:
        print('密码错误')