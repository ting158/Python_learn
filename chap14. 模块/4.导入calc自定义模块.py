#导入calc自定义模块使用
import calc
print(calc.add(2,3))
print(calc.div(4,2))

from calc import add
print(add(2,3))