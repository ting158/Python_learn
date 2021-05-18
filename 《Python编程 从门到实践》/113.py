'''
sandwich_orders=['a','b','c']
finish_sandwich=[]
for sandwich_order in sandwich_orders:
    print(f'I made your {sandwich_order}.')
    finish_sandwich.append(sandwich_order)
print(finish_sandwich)
'''

'''sandwich_orders=['a','p','p','b','p','c']
print('五香熏牛肉买完了')
while 'p' in sandwich_orders:
    sandwich_orders.remove('p')

print(sandwich_orders)'''

places=[]
place=input('Where would you go?')
if place!='':
    places.append(place)
print(places)