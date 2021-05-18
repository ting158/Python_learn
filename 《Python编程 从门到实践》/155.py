class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name      #初始化属性
        self.type=cuisine_type
    def describe_restaurant(self):     #描述餐馆名称，类型
        print(f'\n餐馆叫做{self.name}')
        print(f'类型为{self.type}')
    def open_restaurant(self):        #营业状态
        print('餐馆正在营业')

class Icecream_stand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['orange','apple']
    def show_ice(self): #遍历冰激凌口味
        for i in self.flavors:
            print(i)

ice=Icecream_stand('甜啦啦','奶茶，冰激凌')
ice.describe_restaurant()
ice.open_restaurant()
ice.show_ice()