i=['apper','banana','others']
j=(23,45,12,78,79)

d={i.upper():j for i,j in zip(i,j)} #.upper() 将i中的字母变成大写
print(d)