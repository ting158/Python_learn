t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''尝试将t[1]修改为100'''
print(id(100))
#t[1]=100 #元组是不允许修改元素的
'''由于[20,30]组成列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存不变'''
t[1].append(100) #向列表中添加元素
print(t,id(t[1]))