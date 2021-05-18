
print(type(open('a.txt','r')))
with open('a.txt','r') as file:
    print(file.read())