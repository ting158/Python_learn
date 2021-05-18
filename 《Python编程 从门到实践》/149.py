class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f'\n餐馆叫做{self.name}')
        print(f'类型为{self.type}')
    def open_restaurant(self):
        print('餐馆正在营业')
    def set_number_served(self,number):
        self.number_served = self.number_served + number
        print(f'有{self.number_served}人在这家餐馆就餐过')
    def increment_number_served(self,up_number):
        self.number_served += up_number


restaurant=Restaurant('青木台自助料理','自助餐')
restaurant.describe_restaurant()
restaurant.increment_number_served(11)
restaurant.set_number_served(45)
restaurant.open_restaurant()