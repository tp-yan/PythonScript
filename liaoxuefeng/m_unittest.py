#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:08:31 2019

@author: tangpeng

单元测试：对一个模块、一个函数或者一个类来进行**正确性检验**的测试工作。
"""

"""
测试用例:对函数(模块，类)的一次 期望值与其真实值（比如输出值，返回结果等）的对比，即是否符合期望
测试用例放到一个测试模块里，就是一个完整的单元测试
"""

"""
1. 编写单元测试
假设有一个`Dict`类，这个类的行为和`dict`一致，但是可以通过属性来访问
"""
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
        
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value
        

"""
练习
对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
"""
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError('score must between 0 and 100')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
    


"""
应该将一以下测试代码，单独存于一个模块中作为完整的单元测试

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常
单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug
单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug
"""
import unittest
class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()