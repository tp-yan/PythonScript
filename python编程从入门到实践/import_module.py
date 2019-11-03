'''
#import:实质是将要导入的模块复制到此程序中。导入模块中所有的函数/代码
import module_make_pizza

module_make_pizza.make_pizza(16,'pepperoni')
module_make_pizza.make_pizza(12,'mushrooms','green pepper','extra cheese')
'''

#从模块汇总导入指定的函数，一个或多个
from module_make_pizza import make_pizza,make_cloth
make_pizza(15,'pineapple')
make_pizza(18,'potato')
make_cloth()

#as:给函数起别名，避免函数名冲突
from module_make_pizza import make_pizza as pizza,make_cloth as cloth
pizza(15,'pineapple')
pizza(18,'potato')
cloth()

#as:还可给模块取别名
import module_make_pizza as mp
mp.make_pizza(15,'pineapple')
mp.make_pizza(18,'potato')
mp.make_cloth()

#导入所有函数，不推荐。此举很可能导致重名变量与函数
from module_make_pizza import *
