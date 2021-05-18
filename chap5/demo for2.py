'''输出100到999之间的水仙花数
   举例：
   153=3*3*3+5*5*5+1*1*1*1
'''

for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    #print(bai,shi,ge)
    #判断
    if bai**3+shi**3+ge**3==item:
        print(item)