#高级特性之切片(slice)操作
#对 list 切片后得到新的 list
#对 tuple 切片后得到新的 tuple
#str也可以做切片，看做list，每个元素就是一个字符，得到的也是str,所以python中没有字符串截取函数，使用切片即可

L = list(range(20))
print(L[0:3])	#取前三个元素，不包括索引3，其中0可以省略
print(L[:3])	#效果同上
print(L[-3:])	#从倒数第三个取到末尾元素
print(L[-3:-1])	#不取最后一个元素
print(L[:10:2])	#第一个冒号指定切片的始末索引，第二个冒号后面的数指定步数，即每多少个数中取一个
print(L[:])	#复制一个同样的list
print(L[::5])	#所有的数，每5个取一个

s = "hello,python!"
print(s[2:10])
print(s[::2])
print(s[-3:])
print(s[-3:-1])


#列表中的切片
players = ['charles','martina','michael','florence','eli']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
for player in players[:3]:
	print(player.title())
#使用切片完成列表的深复制，即创建新的存储区并复制内容
new_players = players[:]
new_players.append('jason')
players.append('meiss')
print("new_players: ",new_players)
print("players: ",players)
