class Person(object):  #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student (Person):
    def __init__(self,name,age,stu_number):
        super().__init__(name,age)
        self.stu_number=stu_number
    def info(self):
        super().info()
        print(self.stu_number)

class Teacher(Person):
    def __init__(self,name,age,teach_of_year):
        super().__init__(name,age)
        self.teach_of_year=teach_of_year
    def info(self):
        super().info()
        print(self.teach_of_year)

stu=Student('张三',20,22)
tea=Teacher('李四',30,6)
stu.info()
print('-------------')
tea.info()