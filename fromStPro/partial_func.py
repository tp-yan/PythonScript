#偏函数：就是把一些函数的参数默认值，改为其他的默认值
#当函数参数太多，需要简化时，就可以使用偏函数来创建一个新函数
import functools
int2 = functools.partial(int,base=2)	#将函数int的参数base默认值(原来为10)修改为2，即字符串转换为数字时采用几进制
print(int2('1000000001'))
print(int2('1000000001',base=8))	#调用偏函数时，也可以传入其他值