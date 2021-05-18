'''获取字典中的元素'''
scores={'张三':100,'李四':98,'王五':45}
'''第一种方式，使用[]'''
print(scores['张三'])
#print(scores['陈六']) #KeyError: '陈六'

'''第二种方式，使用get()方法'''
print(scores.get('张三'))
print(scores.get('陈六')) #None
print(scores.get('麻七',99)) #99是在查找‘麻七’所对应的value不存在时，提供的一个默认值