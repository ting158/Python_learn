#集合的相关操作

s={10,20,30,405,60}

#判断
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

#新增
s.add(80) #add一次添加一个元素
print(s)
s.update({200,400,300}) #update一次至少添加一个元素
print(s)
s.update([100,99,8])
s.update((78,64,56))
print(s)

#删除
s.remove(100)
print(s)
#s.remove(500) #KeyError: 500
s.discard(500)
s.discard(300)
print(s)
s.pop()
s.pop()
#s.pop(400) #TypeError: set.pop() takes no arguments (1 given)
print(s)
s.clear()
print(s)