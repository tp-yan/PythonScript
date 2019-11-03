
def init(data):
	'''初始化姓名字典,添加几个键'''
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}

def lookup(data, label, name):
	'''根据名字按域查询全名'''
	return data[label].get(name)	# 若返回的是列表或者字典，返回的也是引用，可改变

def store(data, *full_names):
    ''' 存储全名:通过收集参数改造函数 '''
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1,' ')		# 没有中间名时，插入空白符代替
        labels = 'first', 'middle', 'last'	# 元组，省略了括号
        for label, name in zip(labels, names):	# zip：将多个list或元组的每个对应位置元素拼成一个元组
            people = lookup(data, label, name)	# 返回列表型，同label下同name的list
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]	# list不存在则创建一个list，并添加内容

# 存储联系人姓名
storage = {}
init(storage)	# 传入的是引用将会改变字典内容
storage['first'].setdefault('TP',[])	# 为字典设置默认 key-value 对 等价于 storage['first']['TP'] =  []
print(storage)

store(storage,"Magnus Lie Hetland")
print(lookup(storage,'middle','Lie'))
store(storage,"Robin Hetland")
store(storage,"Robin Hood")
store(storage,"Mr. Gumby")
store(storage,"Luke Skywalker","Anakin Skywalker")
print(lookup(storage,'middle',' '))

