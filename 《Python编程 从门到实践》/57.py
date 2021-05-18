'''
lst=['33','45','66','34','87']

print('The first three items in the list are:')
print(lst[:3])
print('Three items from the middle of the list are:')
print(lst[1:4])
print('The last three items in the list are:')
print(lst[-3:])
'''

my_pizza=['巴厘岛风味披萨','美味培根披萨','酸甜水果披萨']
friend_pizza=my_pizza[:]
my_pizza.append('浓郁海鲜口味披萨')
friend_pizza.append('意大利辣味香肠披萨')
print('My favorite pizzas are:')
for m in my_pizza:
    print(m)
print("My friend's favorite pizzas are:")
for f in friend_pizza:
    print(f)