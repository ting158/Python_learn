#比较运算符,比较运算符结果为bool类型
a,b=10,20
print('a>b吗？',a>b)  #False
print('a<b吗？',a<b)  #Ture
print('a>=b吗？',a>=b)#False
print('a<=b吗？',a<=b)#Ture
print('a==b吗？',a==b)#False
print('a!=b吗？',a!=b)#Ture

''' 一个 = 称为赋值运算符 ， == 称为比较运算符
    一个变量由三部分组成：标识，类型，值
    == 比较的是值还是标识呢？ 比较的是值
    比较对象的标识使用 is
'''
a=10
b=10
print(a==b)     #True  说明，a与b的value相等
print(a is b)   #True  说明，a与b的id标识相等
#以下代码没学过，以后会给大家讲解
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)    #value    -->True
print(list1 is list2)  #id       -->False
print(id(list1))
print(id(list2))
print(a is not b) #False  a的id与b的id是不相等的
print(list1 is not list2) #True