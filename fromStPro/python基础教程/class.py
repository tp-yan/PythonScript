# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:50:40 2019

类
@author: tangpeng
"""

class Student(object):
    '''学生类'''
    # 在方法外定义(即类中)的变量属于类变量，所有实例共享
    # 公有变量
    pub = "类中定义的(方法外)公有变量(public)"
    # 私有变量
    __pri = "类中定义的(方法外)私有变量(private)，子类也不可访问" # 在公有变量前面加2个下划线即可
    _protect = "以单划线开头的是protect类型，子类可访问"
    
    def __init__(self,name,tell):
        '''构造函数,self:代表实例本身'''
        # 给实例绑定属性
        # 公有变量
        self.name = name
        self.tell = tell
        self.other = "方法内定义的公有变量"
        # 私有变量
        self.__other = "方法内定义的私有变量"
        
    def out_pub(self):
        '''公有方法'''
        print("公有方法：\n",self.pub,self.__pri)
        print("公有方法：\n",self.other,self.__other)
    
    def __out__pri(self):
        '''私有方法'''
        print("私有方法：\n",self.pub,self.__pri)
        print("私有方法：\n",self.other,self.__other)
        
    def print_info(self):
        print(self.name,":",self.tell)
        
st = Student('tp','12345678901')
# 给实例动态绑定属性，与在实例方法中绑定效果是一样的，只有此实例拥有
st.age = 23
st.__sex = 'M'

st.out_pub()
print(st.name,st.tell,st.pub,st.other,st.age)
try:
    # 调用私有变量与方法
    print(st.__pri,st.__other,st.__sex)
    st.__out__pri()
except Exception:
    print("不允许从外部调用私有成员！")

print(Student.pub)
# print(Student.__pri) # 错误！不能从外部访问私有变量


