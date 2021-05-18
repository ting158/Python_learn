file = 'guest.txt'
with open(file,'w') as names:
    while True:
        name = input('请输入名字：')
        if name != '':
            print('hello')
            names.write(f'{name}\n')
        else:
            break