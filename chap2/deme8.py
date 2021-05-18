name='张三'
age=20

print(type(name),type(age)) #说明name与age的数据类型不相同
#print('我叫'+name+'，今年'+age+'岁')  #当将str类型与int类型进行连接是，报错，解决方案：类型转换
print('我叫'+name+'，今年'+str(age)+'岁')  #将int类型通过str（）函数转成了str类型

print('------------str()将其他类型转成str类型----------')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('------------int()将其他类型转成int类型----------')
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #将str转成int类型，字符串为 数字串
print(int(f1),type(int(f1)))  #float转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2))) #将str转成int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3))) #将str转成int类型时，字符串必须为数字串（整数），非数字串不允许转换

print('---------float()函数，将其他数据类型转换成float类型-------')
s1='128.98'
s2='76'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),typr(float(s3)))  #字符串中的数据如果是非数字串，则不允许转换
print(float(i),type(float(i)))