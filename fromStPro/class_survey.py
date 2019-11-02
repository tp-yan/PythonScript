class AnonymousSurvey():
	'''手机匿名调查问卷的答案'''
	def __init__(self,question):
		'''存储一个问题，并为存储答案做准备'''
		self.question = question
		self.responses = []
	def show_question(self):
		'''显示调查问题'''
		print(self.question)
	def store_response(self,new_response):
		'''存储单份调查问卷'''
		self.responses.append(new_response)
	def show_result(self):
		'''显示收集的所有答案'''
		print('Survey Result:')
		for response in self.responses:
			print('- '+response)

	
