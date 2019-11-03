print('hello','world!','python')	#遇到逗号，输出一个空格
print("100 + 200 =",100+200)

name = input("input your name：")	#input返回的是字符串
# int(str):将str转换成 int数据
print('hello',name)


a = 100
if a >= 0:		#python中一条语句占一行，若语句以‘：’结尾，则代表以下若干行需要缩进，缩进的代码构成代码块
	print(a)	#缩进的空格数没有要求一般是4个空格
else:
	print(-a)
