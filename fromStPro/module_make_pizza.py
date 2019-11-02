#一个 .py 文件就是一个模块
#包：组织模块的目录，包下面必须有个 __init__.py 文件，若没有该目录就是普通目录而非python中的Package
# __init__.py 可以是空的，也可以有代码。 __init__.py本身是一个模块，但是他的模块名为 所在包(目录)名字

'a test module'		#任何模块代码的第一个字符串都被视为模块的文档注释，可使用 __doc__访问
__author__ = 'tangpeng'	#__author__ 变量标明作者

#python没有 public、private这种关键字，所以没有访问限制范围，即所有的 都是public
#但是有约束： 以 '_' "__"开头的函数或变量被认为 是 private的，在模块外不应该被访问
# pip:包管理工具，可安装 第三方python包，如：
# pip install Pillow	#Pillow是基于 PIL(Python Image Library)的项目，支持Python 3.x，而PIL已经不更新了，只支持python 2.x
# 第三方库都会在python官网 pypi.python.org注册
#Anaconda：基于python的数据处理和科学计算平台，内置了很多第三方库，Anaconda安装的第三方库存在Anaconda的路径下与 不影响Python自带的库
#Anaconda会把系统path中的python指向自己带的Python
#搜索一个模块时，Python解释器会搜索当前路径、已安装的内置模块、第三方模块，搜索路径保存在 sys模块的path变量中

import sys	# sys变量指向sys模块

def test():
	args = sys.argv		#sys模块有一个 lsit类型的变量argv，它存了从命令行输入的所有参数，第一个元素永远是模块名。如python module_make_pizza.py wwwww
	print(args)			#则argv内容为 ['module_make_pizza.py', 'wwwww']
	if len(args) == 1:
		print("hello,World!")
	elif len(args) == 2:
		print("Hello,%s!" % args[1])
	else:
		print("Too many arguments!")

#这两行代码表示：若是从命令行运行此模块，python解释器把一个特殊变量__name__置为__main__，如果是从其他地方调用此模块，则if判断失败。
#这种方式，可以在命令行运行的情况下，额外执行一些任务，最常见的是 测试
if __name__ == '__main__':	
	test()



def make_pizza(size,*toppings):
	print("\nmaking a ",size,"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- ",topping)
		
def make_cloth():
	print("clothing")
