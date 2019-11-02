#使用try-except代码块处理异常

try:
	print(5/1)
except ZeroDivisionError:
	print('You can\'t divide by zero!')
else:#依赖于try代码块成功执行后的代码可放在else中
	print("there are no exceptions in try block!")

file_path = 'a.txt'

try:
	with open(file_path) as file_obj:
		print(file_obj.read())
except:
	print('The file',file_path,' does\'t exist!')


while True:
	try:
		digit = input('please input 2 digits(input \'q\' exit):')
		if digit == 'q':
			break
		a = int(digit)
		b = int(input())
	except ValueError:
		print('输入的不是数值类型!')
		#continue
	else:
		print('the sum of them is:',a+b)

def print_file(file_name):
	try:
		with open(file_name) as file_obj:
			contents = file_obj.read()
			for name in contents.split():
				print('-',name)
	except FileNotFoundError:
		pass
		#print(file_name,' not found!')
		
file_cat = 'cats.txt'
file_dog = 'dogs.txt'
file_mutton = 'mutton.txt'

print_file(file_cat)
print_file(file_dog)
print_file(file_mutton)

def count_txt_words(file_name):
	'''求文本文件的字数'''
	try:
		with open(file_name) as file_obj:
			contents = file_obj.read()
			print(file_name,' has ',len(contents.split()),' words.')
	except FileNotFoundError:
		print(file_name,' not found!')

file_novel = 'William.txt'
count_txt_words(file_novel)

def count_words_time(file_name,words):
	'''求words在文本文件中出现的次数'''
	try:
		with open(file_name) as file_obj:
			contents = file_obj.read()
			#x.count(y):计算y在字符串x中出现的次数
			print(words,' 出现了 ',contents.lower().count(words),'次')
	except FileNotFoundError:
		print(file_name,' not found!')

count_words_time(file_novel,'the')
