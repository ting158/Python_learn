'''
rivers={'尼罗河':'坦桑尼亚、布隆迪、卢旺达、乌干达、苏丹、埃及等国境',
       '亚马逊河':'秘鲁、巴西等国境',
       '长江':'中国'
       }
for river,country in rivers.items():
    print(f'{river}流经{country}')

print('---------------------------')

for river in rivers.keys():
    print(river)

print('---------------------------')

for country in rivers.values():
    print(country)
'''

favorite_languages = {
    'j':'python',
    's':'c',
    'e':'ruby',
    'p':'python'
    }
f = ['j','s','e','p']
names = ['j','a','s','e','p']
for name in favorite_languages.keys():
    print(name)
print('thanks')
for n in names:
    if n not in f:
        print('\n' f'{n.title()},please go')

