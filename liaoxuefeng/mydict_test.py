#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:14:16 2019

@author: tangpeng

mydict_test.py:测试用例组成的单元测试，用于测试m_unittest中的Dict类
"""

import unittest

from m_unittest import Dict

# 编写一个单元测试类，从`unittest.TestCase`继承。
class TestDict(unittest.TestCase):
    # 以`test`开头的方法就是测试方法，不以`test`开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a,1) # TestCase内置的条件判断,调用这些方法可以断言输出是否是我们所期望的
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
        
    # 对每**一类测试**都需要**编写一个`test_xxx()`方法**，每个测试方法都是独立的
    def test_key(self): # 测试通过属性来访问和设置 value
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')
        
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
        
    def test_keyerror(self):
        d = Dict()
        # 另一种重要的断言就是期待抛出指定类型的`Error`
        with self.assertRaises(KeyError): # 访问不存在的 key 应该抛出 KeyError
            value = d['empty']
            
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
        
    # 单元测试中两个特殊的setUp()和tearDown()方法：在调用每一个测试方法的前后分别被自动执行
    # 可以将很多测试方法的公共代码，置于此，比如在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

# 最简单的单元测试运行方式，这样就可以把mydict_test.py当做正常的python脚本运行
if __name__ == '__main__':
    unittest.main()            
    
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试（推荐）：
# python -m unittest mydict_test