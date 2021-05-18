#计算100-999之间的水仙花数
import math
for i in range(100,1000):
    if math.pow((i//100),3)+math.pow((i//10%10),3)+math.pow((i%10),3)==i:
        print(i)

print('-------------------------')
#第二种方法
for a in range(100,1000):
    if a==(a//100)**3+(a//10%10)**3+(a%10)**3:
        print(a)
