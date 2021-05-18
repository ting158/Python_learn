s='hello,Python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))

'''将列表或元组中的字符串合并成一个字符串'''
lst=['hello','java','python']
print('|'.join(lst))
print(''.join(lst))
t=('hello','Java','Python')
print(''.join(t))

print('*'.join('python'))