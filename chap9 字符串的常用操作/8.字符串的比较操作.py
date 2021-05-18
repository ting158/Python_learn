print('apple'>'app')
print('apple'>'banana') #False   相当于97>98  False
print(ord('a'),ord('b'))
print(ord('史'))

print(chr(97),chr(98))
print(chr(21490))

'''==与is的区别
   ==比较的是value
   is 比较的是id是否相等'''
a=b='Python'
c='Python'
print(a==b)
print(b==c)

print(a is b)
print(b is c)
print(id(a))
print(id(b))
print(id(c))