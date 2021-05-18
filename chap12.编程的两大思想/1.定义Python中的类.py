class Student:  #Student为类的名称（类名），有一个或多个单词组成，每个单词首字母大写，其余小写
    pass

#Python中一切皆对象 Student是对象吗？ 内存有开空间吗？
print(id(Student)) #2739165022256
print(type(Student)) #<class 'type'>
print(Student) #<class '__main__.Student'>

