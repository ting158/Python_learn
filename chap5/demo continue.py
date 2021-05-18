'''要求输出1到15之间所有5的倍数
   和5的余数为0
   与5的余数不为0的数都不是5的倍数
   使用continue实现
'''

for item in range(1,51):
    if item%5==0:
        print(item)


print('-------使用continue-------')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)