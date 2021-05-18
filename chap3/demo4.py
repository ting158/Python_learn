#赋值运算符，运算顺序从右到左
i=3+4
print(i)
a=b=c=20  #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('------支持参数赋值------')
a=20
a+=30  #相当于a=a+30
print(a)
a-=10  #相当于a=a-10
print(a)
a*=2   #相当于a=a*2
print(a)  #int
print(type(a))
a/=3
print(a)  #float
print(type(a))
a//=2
print(a)
print(type(a))
a%=3
print(a)
print('--------解包赋值--------')
a,b,c=20,30,40
print(a,b,c)


#a,b=20,30,40  报错，因为左右变量的个数和值的个数不对应
print('-------交换两个变量的值------')
a,b=20,30
print('交换之前：',a,b)
#交换
a,b=b,a
print('交换之后：',a,b)