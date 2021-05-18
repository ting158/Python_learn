scores={'张三':100,'李四':98,'王五':45}
#获取所有的key
i=scores.keys()
print(i)
print(type(i))
print(list(i)) #将所有key组成的视图转成列表

#获取所有的value
j=scores.values()
print(j)
print(type(j))
print(list(j))

#获取所有的key-value对
k=scores.items()
print(k)
print(type(k))
print(list(k)) #转换之后的列表元素是由元组组成 （元组将在下个章节讲解）