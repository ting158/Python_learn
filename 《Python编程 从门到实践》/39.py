'''
trip=['b北京','s上海','g广州','s深圳','x厦门']
print(trip)
print(sorted(trip))
print(trip)
print(sorted(trip,reverse=True))
print(trip)
trip.reverse()
print(trip)
trip.reverse()
print(trip)
trip.sort()
print(trip)
trip.sort(reverse=True)
print(trip)
'''

def fun():
    lst=[]
    while True:
        a=input('请输入你要添加的东西（每次只能输入一个,停止输入请输入n）：')
        if a=='n':
            break
        else:
            lst.append(a)
    print(lst)

fun()