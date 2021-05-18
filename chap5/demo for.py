for item in'Python':  #第一次取出来的是P，将P赋值给item，将item的值输出
    print(item)

#range（） 产生一个整数数列，--》也是一个可迭代对象
for i in range(10):
    print(i)


#如果在循环体中不需要使用到自定义变量，可将自定义变量写为"_"
for _ in range(5):
    print('人生苦短，我用Python')


print('使用for循环，计算1到100之间的偶数和')
sum=0 #用于存储偶数和
for item in range(0,101):
    if item % 2 == 0:
        sum=sum+item

print('1到100之间的偶数和为：',sum)