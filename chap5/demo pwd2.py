a=0
while a<3:
    '''条件执行体（循环体）'''
    pwd=input('请输入您的密码：')
    if pwd=='888888':
        print('密码正确')
        break
    else:
        print('密码错误')

    '''改变变量'''
    a+=1