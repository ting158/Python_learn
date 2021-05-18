class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
    def describe_restaurant(self):
        print(f'\n餐馆叫做{self.name}')
        print(f'类型为{self.type}')
    def open_restaurant(self):
        print('餐馆正在营业')


restaurant1=Restaurant('青木台自助料理','自助餐')
restaurant2=Restaurant('九田家黑牛烤肉料理','日式烧烤/烤肉')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()