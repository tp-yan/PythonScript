#---list的使用---
#list是一种有序的数组，但list的元素数据类型与维度都可以不同
L = [
		['apple','google','micosoft'],
		['java','python','c#'],
		['Adam','bart','Lisa'],
		123,
		True
	]

for outer in L:
	if isinstance(outer,list):	#判断数据所属类型
		print(outer[-1])	#负索引，从后往前索引
	else:
		print(outer)

print(L[0])
print(L[2][1])

motorcycle = ['honda','yamaha','suzuki','caocao','toyota']
motorcycle[0] = 'byd'	#替换元素

motorcycle.append('honda')	#列表末添加元素
motorcycle.insert(1,'jili')	#在指定位置插入元素

motorcycle.pop()		#删除末尾元素。pop()会返回删除的元素
motorcycle.pop(-2)		#删除指定位置元素
del motorcycle[3]		#del语句删除指定位置的元素
motorcycle.insert(2,'byd')
motorcycle.remove('byd')	#根据元素值删除并返回，若有多个则删除第一个值,若无则报错

motorcycle.sort()		#sort([reverse=True/False])：将列表永久性排列，根据参数按字母顺序或反序排序
motorcycle.sort(reverse=True)
print(motorcycle)
print(sorted(motorcycle,reverse=False))	#sorted(list[,reverse=True/False])：临时排序，不改变原有序列
motorcycle.reverse()		#reverse:反转顺序

num_list = list(range(1,100,5))		#使用range方法生成list,range(start,end[,step]):其中step指定步长
print("sum: "+str(sum(num_list)))	#操作数值list的几个函数
print("mix: "+str(min(num_list)))
print("max: "+str(max(num_list)))



#---tuple:就是元素值不可变（实质上的元素的指向不可变）的list---，比list更安全，tuple的元素可以是list
print('-------------------tuple------------------------')
#dimensions只是变量它可以重新指向新的tuple或其他数据
dimensions = (100,200) #(100,200) 这个数据是tuple类型的，而dimensions只是变量
print(dimensions)
dimensions = (400,300)
print(dimensions)

foods = ('beef','mutton','pork','chicken','duck','fish')
foods = ('beef','mutton','noodles','chicken','rice','fish')
for food in foods:
	print(food.title())
M = ('hello','python',L)
print(M[2])
K = (1,2,3,4)
print(K)
K = (1)	#k为 整数1
print(K)
K = (1,)	#k为tuplex类型:(1)
print(K)





#==========================练习==========================
dear_people = ['father','mather','grandparents','old-sister']
print(dear_people)
print('无法出席：'+dear_people[3])
dear_people[3] = 'brother'
for name in dear_people:
	print('宴会邀请：'+name)

dear_people.insert(0,'teacher-tang')
dear_people.insert(1,'teacher-shi')
dear_people.append('teacher-xu')
for name in dear_people:
	print('宴会邀请：'+name)
	
while len(dear_people) > 2:		#len：得到list元素个数
	print("sorry："+dear_people.pop())
print('final list:',dear_people)
del dear_people[0]
del dear_people[0]
print(dear_people)
motorcycle = ['honda','yamaha','suzuki']