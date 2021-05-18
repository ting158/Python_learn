s='hello,python'
a=s.upper() #转成大写之后，会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))
b=s.lower() #转换之后会产生一个新的字符串对象
print(b,id(b))
print(s,id(s))
print(b==s) #内容相等
print(b is s) #地址不相等

s2=('hello,Python')
print(s2.swapcase())
print(s2.capitalize())
print(s2.title())