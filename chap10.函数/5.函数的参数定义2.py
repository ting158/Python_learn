def fun(*aer):  #函数定义时的可变的位置参数
    print(aer)


fun(10)
fun(10,30)
fun(30,405,50)


def fun1(**aer):
    print(aer)

fun1(a=10)
fun1(a=10,b=20,c=30)

'''def fun2(*aer,*a):
    pass
    以上代码，程序会报错，个数可变的位置参数，只能是1个
    def fun2(**aer,*a):
    pass
    以上代码，程序会报错，个数可变的关键字参数，只能是1个
    '''

def fun2(*aer1,**aer2):
    pass

'''def fun3(**aer1,*aer2):
    pass
    在一个函数的定义过程中，既有可变的关键字形参，也有个数可变的位置形参，要求个数可变的位置形参放在个数可变的关键字形参之前
    '''