'''key的判断'''
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三'] #删除指定的key-value对
#scores.clear() #清空字典的元素
print(scores)
scores['陈六']=98 #新增元素
print(scores)

scores['陈六']=100 #修改元素
print(scores)