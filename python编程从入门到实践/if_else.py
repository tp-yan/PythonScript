#-*- coding:utf-8 -*-
#--if elif else语句--

#if x:	#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
#    print('True')

height = 1.75
weight = 80.5
bmi = 80.5/pow(1.75,2)
if bmi > 32:
	print('严重肥胖')
elif bmi>28:
	print('肥胖')
elif bmi > 25:
	print('过重')
elif bmi > 18.5:
	print('正常')
else:
	print('过轻')
