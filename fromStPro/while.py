'''
active = True
while active:
	ingredient = input('input your ingredients:')
	if ingredient != 'quit':
		print(ingredient)
	else:
		active = False

active = True
while active:
	age = input('your age:')
	if age == 'quit':
		break
	age = int(age)
	if age < 3:
		price = 0
	elif age < 12:
		price = 10
	elif age >= 12:
		price = 15
	print("you need to pay $",price)
	
while active:
	print(active)
'''

sanwich_orders = ['yeelow','blue','green','red']
sanwich_orders.append('pastrami')
sanwich_orders.insert(0,'pastrami')
sanwich_orders.insert(3,'pastrami')
print("I'am so sorry,pastrami is gone!")
while 'pastrami' in sanwich_orders:
	sanwich_orders.remove('pastrami')

finished_sanwiches = []
while sanwich_orders:
	sanwich = sanwich_orders.pop()
	print('I made your ',sanwich,' sanwich')
	finished_sanwiches.append(sanwich+"-ed")
print(finished_sanwiches)


visit_places = []
while True:
	place = input('IF you could visit one place in the world,where you go?')
	if place == 'no':
		break
	visit_places.append(place)
print(visit_places)
	
