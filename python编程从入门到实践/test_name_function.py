#使用python的unittest模块工具测试方法name_function
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
		'''创建用于测试的类，必须继承于unittest.TestCase'''
		def test_first_last_name(self):
			'''是否能够正确地处理像 janis joplin这样的姓名
			所有以test开头的方法都将自动运行，一般一个方法用于测试被测物的的某一面
			'''
			formatted_name = get_formatted_name('janis','joplin')
			self.assertEqual(formatted_name,'Janis Joplin')
		
		def test_first_last_middle_name(self):
			'''能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗'''
			formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
			self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
			
#让python运行这个文件中的测试
unittest.main()
