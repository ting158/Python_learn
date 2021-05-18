a='python'
b="python" #双引号不等于两个单引号
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(a==b==c)