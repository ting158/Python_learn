from name_function import get_formatted_name

print('输入q停止程序')

while True:
    first = input('\n姓')
    if first == 'q':
        break
    last = input('名')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f'\t姓名:{formatted_name}')