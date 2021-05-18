'''元组的遍历'''
t=('Python','world',98)
'''第一种获取元组元素的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
#print(t[3]) #IndexError: tuple index out of range
'''第二种获取元组的方式，遍历元组'''
for item in t:
    print(item)