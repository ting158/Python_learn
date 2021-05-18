people={'first_name':'shi','last_name':'zhen','age':20,'city':'wuhu'}
print(people['first_name'])

print('------------------------')

uses={'title()':'将每个单词的首字母都改为大写',
      'upper()':'将字符串改为全部大写',
      'lower()':'将字符串全部改为小写',
      'rstrip()':'删除字符串末尾的空白',
      'lstrip()':'删除字符串开头的空白'
      }

for world,use in uses.items():
      print(f'{world}:' '\n' f'{use}')