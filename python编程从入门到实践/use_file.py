#打开文件并读取内容后打印输出
#with:让Python在适当时关闭文件，我们不用关心。但是文件对象只能在with的代码块中有效
file_path = r'C:\Users\tangpeng\Desktop\hello_python.txt'
file_path_pi = r'pi_digits.txt'
with open(file_path_pi) as file_obj:
	#逐行读取文本,每行都有一个换行符，将会被Python读取到
	#for line in file_obj:
	#	print(" -",line.rstrip())
	#read：读取所有内容，读到文件末尾时返回一个空字符串
	#content = file_obj.read()
	#print(content)
	#逐行读取并返回一个列表对象
	lines = file_obj.readlines()

pi_str = ''	
for line in lines:
	#print(line.rstrip())
	pi_str += line.strip()

#print(pi_str)
#print("length:",len(pi_str))
'''
birthday = input('input your birthday:')
if birthday in pi_str:
	print('pi_str include your birthday!')
else:
	print('pi_str does not include your birthday!')
'''	
file_path_learning = 'python_learning.txt'
with open(file_path_learning) as file_obj:
	#print(file_obj.read())
	#for line in file_obj:
	#	print(line,end="")
	lines = file_obj.readlines()

for line in lines:
	print(line.replace('Python','C'))

#写入文件,'w'模式清空原有文件，或创建不存在的文件
file_path_write = 'programming.txt'
with open(file_path_write,'w') as file_obj:
	file_obj.write('today is monday!\n')
	file_obj.write('yesterday is sunday!\n')
	file_obj.write('tomorrow is Tusday!\n')

#向文件中追加内容
with open(file_path_write,'a') as file_obj:
	file_obj.write('this is 12th week')

with open('guest.txt','a') as file_obj:
	while True:
		name = input('enter your name,please:')
		if name == 'no':
			break
		print("Hello,",name,"!")
		file_obj.write(name+"\n")
