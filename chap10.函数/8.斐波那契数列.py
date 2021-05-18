def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)

#斐波那契数列上的第六位数字
print(fun(6))

print('-------------------------')
#输出这个数列上的前六位数字
for i in range(1,7):
    print(fun(i),end='\t')