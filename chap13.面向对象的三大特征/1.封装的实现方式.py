class Car():
    def __init__(self,name):
        self.name=name
    def start(self):
        print('汽车已启动')


car=Car('宝马X5')
car.start()
print(car.name)