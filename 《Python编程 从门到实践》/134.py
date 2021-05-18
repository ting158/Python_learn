'''
def sandwish(*food):
    print(f'三明治添加了\n{food}')

sandwish('鸡肉','牛肉')
'''

'''
def user_profile(first,last,**me_info):
    me_info['first']=first
    me_info['last']=last
    return me_info

i = user_profile('shi','zhen',type='smart')
print(i)
'''

def make_car(name,type,**information_car):
    information_car['name']=name
    information_car['type']=type
    return information_car

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)