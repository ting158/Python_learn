#“千年虫“问题

year=[24,67,65,00,45,99]
print(year)
for index,value in enumerate(year):
    #print(index,value)
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))

print(year)

#列表排序
year.sort()
print(year)
