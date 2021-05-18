s='hello,hello'
print(s.index('lo'))
print(s.rindex('lo'))
print(s.find('lo'))
print(s.rfind('lo'))

#print(s.index('k')) #ValueError: substring not found
print(s.find('k')) #-1
#print(s.rindex('k')) #ValueError: substring not found
print(s.rfind('k')) #-1
