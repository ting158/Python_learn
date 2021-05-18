'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5): #外层循环执行5次
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()