'''第一种创建方式，使用{}'''
s={2,3,4,5,5,6,7,7} #集合中的元素不允许重复
print(s)

'''第二种创建方式，使用set()'''
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,4,5,5,5,6,6])
print(s2,type(s2))

s3=set((1,2,4,4,5,65)) #集合中的元素是无序的
print(s3,type(s3))

s4=set('Python')
print(s4,type(s4))

s5=set({12,4,34,55,66,44,4})
print(s5,type(s5))

#定义一个空集合
s6={} #字典类型
print(type(s6))

s7=set()
print(type(s7))