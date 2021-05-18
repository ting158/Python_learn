#切片操作



lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1
#print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))
print(lst[1:6]) #默认步长为一
print(lst[1:6:])
#start=1,stop=6,step=2
print(lst[1:6:2])
#stop=6,step=2,start采用默认
print(lst[:6:2])
#start=1,step=2,stop采用默认
print(lst[1::2])
print('--------step步长为负数的情况--------')
print('原列表',lst)
print(lst[::-1])
#start=7,stop省略，step=-1
print(lst[7::-1])
#start=6,stop=0,step=-2
print(lst[6:0:-2])