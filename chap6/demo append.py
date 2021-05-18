#向列表的末尾添加一个元素
lst=[10,20,30]
print('添加元素之前：',lst,id(lst))
lst.append(100)
print('添加元素之后：',lst,id(lst))

lst2=['hello','world']
#lst.append(lst2) #将lst2作为一个元素添加到列表的末尾
lst.extend((lst2)) #向列表的末尾一次性添加多个元素
print(lst)

#在任意位置上添加一个元素
lst.insert(1,'python')
print(lst)

lst3=[True,False,'python']
#在任意位置上添加N多个元素
lst[1:]=lst3 #把切掉的部分用新的列表替换
print(lst)