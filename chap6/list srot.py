lst=[12,34,6542,214,4536,75]
print('排序签的列表',lst,id(lst))
#开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True) #reverse=True表示降序排序，reverse=False就是升序排序
print(lst)
lst.sort(reverse=False)
print(lst)

print('----------使用内置函数sorted()对列表进行排序，将产生一个新的列表对象---------')
lst=[12,34,6542,214,4536,75]
print('原列表',lst)
#开始排序
new_list=sorted(lst)
print(new_list)
#指定关键字参数，实现列表元素的降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list)