lst=['hello','world',98,'hello']
print(lst.index('hello')) #如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
#print(lst.index('Python')) #ValueError: 'Python' is not in list
#print(lst.index('hello',1,3)) #ValueError: 'hello' is not in list      'world',98

print(lst.index('hello',1,4)) #3