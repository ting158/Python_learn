'''
names=[]

if names:
    for name in names:
        if name=='admin':
            print(f'Hello {name},would you...')
        else:
            print(f'Hello {name},thank you ...')
else:
    print('We need to find some users!')
'''

'''current_users=['yi','er','san','si','wu']
new_users=['er','Si','liu','qi','ba']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('用户名已被使用')
    else:
        print('你可以使用这个名字')'''

nums=['1','2','3','4','5','6','7','8','9']
for num in nums:
    if num == '1':
        print(f'{num}st')
    elif num == '2':
        print(f'{num}nd')
    elif num == '3':
        print(f'{num}rd')
    else:
        print(f'{num}th')