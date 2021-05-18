'''while True:
    try:
        num1 = int(input('请输入一个整数：'))
        num2 = int(input('请输入一个整数：'))
    except ValueError:
        print('输入的不是整数')
    else:
        num = num1 + num2
        print(num)'''


'''dogs='dogs.txt'
cats='cats.txt'
try:
    with open(dogs) as dog:
        for dog_name in dog:
            print(dog_name.rstrip())
    with open(cats) as cat:
        for cat_name in cat:
            print(cat_name.rstrip())
except FileNotFoundError:
    pass
'''

rs = ''
line = 'alice.txt'
with open(line,encoding='utf-8') as read:
    for r in read:
        rs += r
    print(rs.lower().count('the '))