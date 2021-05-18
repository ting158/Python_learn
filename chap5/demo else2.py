a=0
while a<3:
    pwd=input('请输入您的密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
        a+=1
else:
    print('您已输入三次错误')