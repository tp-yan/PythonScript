import unittest
from class_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	'''针对AnonymousSurvey类的测试'''
	
	def setUp(self):
		'''相当于类的__init__方法，最先执行setUp,然后执行test_xx'''
		#创建一个调查对象和一组答案，供使用的测试方法使用,减少各测试单元重复代码
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Chinese','Spanish']
	
	def test_single_response(self):
		'''测试单个答案会被妥善存储'''
		self.my_survey.store_response(self.responses[0])
		
		self.assertIn(self.responses[0],self.my_survey.responses)
		
	def test_store_3_responses(self):
		'''测试3个答案会被妥善存储'''
		
		for response in self.responses:
			self.my_survey.store_response(response)
		
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)
		
unittest.main()
