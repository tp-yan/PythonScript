# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:51:01 2019

异常
@author: 10841
"""

# 1.主动引发异常,raise语句：以Exception及其子类或者异常实例作为参数
'''
raise Exception # 以类作为参数，将自动创建一个实例
raise Exception("hypder overload")
raise ArithmeticError
'''
# 2.自定义异常类：必须是Exception的子类
class CustomException(Exception):
    pass
class CustomException2(ArithmeticError):
    pass

# 3.捕获异常try/except
try:
    10/0
except ZeroDivisionError:
    print("ZeroDivisionError")

# 3.1 捕获后再抛出异常：适用于当前无法处理此异常
class MuffledCalculator:
    muffled = True # 抑制异常，不让用户看到异常信息
    def cal(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise # 不带参数的 raise 将捕获到的异常原样抛出
calculator = MuffledCalculator()
calculator.cal("10/2")
calculator.cal("10/0")
calculator.muffled = False
#calculator.cal("10/0")

# 3.1.1 异常上下文
'''
try:
    1/0
except ZeroDivisionError:
    raise ValueError # 使用raise引发其他类型的异常，而不是将原异常抛出。这将导致
    # 原异常会被作为异常上下文存储起来，并在最终的错误信息中打印
# raise ... from ... ：提供自己的异常上下文，或者使用None禁用上下文
try:
    1/0
except ZeroDivisionError:
    raise ValueError from None
'''
# 3.2一个except子句捕获多个异常
try:
    x = int(input("Enter number x:"))
    y = int(input("Enter number y:"))
    print("x / y = ",x/y)
except (ZeroDivisionError,TypeError,NameError) as e: # 注意：需要使用元组将它们括起来，作为一个参数
    # 第二个参数e捕获异常对象
    print("too many ...")
    print(e)
except Exception:
    print("都归我管")
except:
    print("我才是真正的捕获之王，Exception的超类BaseException我也能捕获")
    print("SystemExit(调用函数sys.exit触发),KeyboardInterrupt(摁下Ctrl+C时触发)异常都是BaseException的子类")

# 4.try/except/else,try/finally
# 4.1 try/except/else
try:
    print("try...")
except BaseException as e:
    print(e)
else:
    print("try代码块没有报错时执行else子句")

# 直到输入合法内容时跳出循环
while True:
    try:
        x = int(input("Enter number x:"))
        y = int(input("Enter number y:"))
        print("x / y = ",x/y)
    except Exception as e:
        print("Invalid input:",e)
        print("Please try again!")
    else:
        break

# 4.2 try/finally：完成清理工作
try:
    print("try....")
#    1 / 0
finally:
    print("这里完成清理工作。无论try是否抛出异常，都执行finally")
    # 抛出异常时，先执行完finally后再抛出异常

# 能使用try/except就不要用if语句去判断
def describe_person(person):
    print("Description of ", person['name'])
    print("Age: ", person['age'])
    try:
        print("Occuption: ",person['occuption'])
    except KeyError: # 没有Occuption就不输出
        pass

describe_person({'name':"Tom","age":24})
describe_person({'name':"Tom","age":24,"occuption":"IT"})

# 5.警告Warning:通常只打印一条错误/警告信息，只显示一次
# 需要导入 warnings模块，使用里面的warn和filterwarnings函数
# 5.1 warn函数：抛出警告
from warnings import warn,filterwarnings
warn("I've got a bad feeling about this.") # 抛出警告
warn("I've got a bad feeling about this.",DeprecationWarning)  # 抛出指定的警告类型

# 5.2 filterwarnings函数：抑制指定的警告，并采取措施：“error"或"ignore"
filterwarnings("ignore") # 忽略所有警告
warn("I've got a bad feeling about this.") # 抛出警告
warn("I've got a bad feeling about this.",DeprecationWarning)  # 抛出指定的警告类型
filterwarnings('error')
warn("I've got a bad feeling about this.",DeprecationWarning) # 指定的警告为抛出的异常
filterwarnings('error',category=DeprecationWarning) # 将警告变异常抛出，并过滤掉指定异常
warn("I've got a bad feeling about this.",DeprecationWarning) # 指定的警告为抛出的异常
warn("I've got a bad feeling about this.") # 默认引发的异常：UserWarning


