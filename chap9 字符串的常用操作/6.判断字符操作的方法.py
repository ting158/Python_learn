s='hello,python'
'''判断指定的字符串是不是合法的字符串'''
print('1',s.isidentifier())
print('2','hello'.isidentifier())
print('3','张三_'.isidentifier())
print('3','张三_123'.isidentifier())

'''判断指定的字符是否全部由空白字符组成（回车、换行，水平制表符'''
print('5','\t'.isspace())

'''判断指定的字符是否全部由字母组成'''
print('6','abc'.isalpha())
print('7','张三'.isalpha())
print('8','张三1'.isalpha())

'''判断指定字符串是否全部由十进制的数字组成'''
print('9','123'.isdecimal())
print('10','123四'.isdecimal())
print('11','ⅡⅡⅡ'.isdecimal())

'''判断指定的字符串是否全部由数字组成'''
print('12','123'.isnumeric())
print('13','123四'.isnumeric())
print('14','ⅡⅡⅡ'.isnumeric())

'''判断指定字符串是否全部由字母和数字组成'''
print('15','abc1'.isalnum())
print('16','张三123'.isalnum())
print('17','abc!'.isalnum())