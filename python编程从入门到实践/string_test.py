# _*_ coding:utf-8 _*_	
#上面一行告诉 python解释器 按照utf-8格式读取源代码

#python中的字符串采用unicode编码，所有字符2个字节
#可变长的编码格式：utf-8,英文字符一个字节，中文三个字节
#在计算机内存中统一使用unicode编码，但是需要保存到硬盘或者用于网络传输时，需将unicode先转换成utf-8
#python中'str'代表字符串，str是不可变对象

print(ord('A'))	#ord:获取字符的unicode编码
print(ord('中'))

print(chr(66))	#chr:将编码转换成字符
print(chr(25991))


#将字符串保存到硬盘或者用于网络传输时，需要将 str 转换成 以字节为单位的 bytes
#bytes数据类型的数据用 b + 单/双引号表示，引号里面即是bytes数据
# str有方法 encode('编码格式')来编码成指定格式的 bytes数据
x = b'ABC'	#这里的ABC与字符串的ABC不同，这里的每个字符只占一个字节
print(x)
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))	#bytes数据将不在ascii范围内的字符，用\x##表示
#将从硬盘或者网络中获得的bytes数据转换成str的方法：decode('编码格式')
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad'.decode('utf-8'))	
print(b'\xe4\xb8\xad\xe6'.decode('utf-8',errors='ignore'))	#如果bytes中有无法编码的字节，可以设置errors='ignore'忽略这部分字节

#len：计算str的字符数，或bytes的字节数
print(len('ABXC'))
print(len(b'\xe4\xb8\xad\xe6'))
print(len(b'\xe4\xb8\xad'))

#python中的格式化输出与C语言一样
print("%s,%04d,%.2f" % ('格式化输出',22,22.2345))	#%x:输出16进制的整数，
print("%s%%,%s" % (25,True))	#任何数据都可以按 %s输出	%%：输出 '%''
print("%.1f" % (85-72))
#字符串的format方法也可以格式化输出
print("hello,{0},成绩提高了 {1:.1f}%".format('小明',17.125)) 	#用format中的参数分别填充 {0}、{1}

a = 'abc';
b = a.replace('a','A')	#将原来的a替换成A后，新建了一个字符串，而a指向的字符串内容没变，因为str是不可变对象
print(a)	
print(b)


##########################################################################################
name = '  ada lovelace  '
print(name.title())	#title:实现每个单词首字母大写
print(name.lower())
print(name.upper())
print("hello " + name.title())

#分别去除开头、末尾、两端空白字符
print(name.lstrip())
print(name.rstrip())
print(name.strip())

username = input("hi,what's your name?")
username = username.strip()
print("Welcome "+username+"! Would you like to learn some Python today?")
print("Welcome "+username.title())
print("Welcome "+username.lower())
print("Welcome "+username.upper())
print("Welcome ",username.upper())

#str:将非字符串值转换为字符串
print(str(190.111)+"$")
