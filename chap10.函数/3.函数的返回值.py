print(bool(0)) #0的布尔值为False
print(bool(1)) #非0的布尔值为True


def fun(num):
    odd=[] #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

#函数的调用
lst=[10,29,34,23,44,53,55]
print(fun(lst))

'''
函数的返回值
（1）如果函数没有返回值（函数执行完毕之后，不需要给调用处提供数据） return可以不写
（2）函数的返回值如果是一个，直接返回原类型
（3）函数的返回值如果是多个，返回的结果为元组
'''

def fun():
    print('hello')
    #return

fun()


def fun2():
    return'hello'

res=fun2()
print(res)


def fun3():
    return'hello','world'

res2=fun3()
print(res2)


'''函数在定义时，是否需要返回值，视情况而定'''