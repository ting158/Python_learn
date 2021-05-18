'''
people={
    'sz':{
        'first':'shi',
        'last':'zhen',
        'age':20,
        'city':'wuhu'
         },
    'my':{
        'first':'ma',
        'last':'yun',
        'age':50,
        'city':'hangzhou'
        },
    'mht':{
        'first':'ma',
        'last':'huateng',
        'age':44,
        'city':'shenzhen'
        }
       }

for n,x in people.items():
    print('\n' f'name:{n}')
    full_name=f"{x['first']} {x['last']}"
    ag=x['age']
    ct=x['city']
    print('\t'+f'full_name:{full_name}')
    print('\t'+f'age:{ag}')
    print('\t'+f'city:{ct}')
'''

pets=[
    {'type':'dog','master':'a'},
    {'type':'cat','master':'b'}
    ]
for pet in pets:
    print(f"type:{pet['type']} \t master:{pet['master']}")