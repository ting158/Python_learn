#在导入带有包的模块时的注意事项
import package1
import calc
#使用import方式进行导入时，只能跟包名或模块名


from package1 import module_A
from package1.module_A import a
#使用from...import可以导入包，模块，函数，变量