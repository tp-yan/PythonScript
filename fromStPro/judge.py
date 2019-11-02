car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict False.")
print(car == 'audi')

currency = ['Dollar','RMB','Pound','Euro']
print("Yen in currency ? ",'Yen' in currency)
print("RMB in currency ? ",'RMB' in currency)
print("HK not in currency ?",'HK' not in currency)

s1 = 'tp'
s2 = 'TangPeng'
print("s1 == s2 ? ",s1 == s2)
print("s1 != s2 ? ",s1 != s2)
print("s1 == 'tp' ?",s1 == 'tp')
print("s1.upper() == 'TP' ?",s1.upper() == 'TP')
print("s2.lower() == 'tangpeng' ?",s2.lower() == 'tangpeng')

a = 1
b = 2
print("a == b ?",a == b)
print("a != b ?",a != b)
print("a > b ?",a > b)
print("a >= b ?",a >= b)
print("a < b ?",a < b)
print("a <= b ?",a <= b)

if a == 1 and b > 2:
	print(a,b)
elif a > 0 or b > 0:
	print("a > 0 and b > 0")

if not False:
	print('FFFalse')

alien_color = 'red'

if alien_color == 'green':
	print('you get 5 points')
elif alien_color == 'yellow':
	print('you get 15 points')
elif alien_color == 'red':
	print("you get 10 points")

if alien_color == 'green':
	print('you get 5 points')
if alien_color == 'yellow':
	print('you get 15 points')
if alien_color == 'red':
	print("you get 10 points")

age = 22
if age < 2:
	print("婴儿")
elif age < 4:
	print("蹒跚学步")
elif age < 13:
	print("儿童")
elif age < 20:
	print("青少年")
elif age < 65:
	print("成年人")
elif age >= 65:
	print("老年人")

fruits = ['banana','apple','orgin']
if 'banana' in fruits:
	print('you really like bananas!')
if 'apple' in fruits:
	print('you really like apple!')
if 'orgin' in fruits:
	print('you really like orgin!')
if 'coffe' in fruits:
	print('you really like coffe!')
if 'mutton' in fruits:
	print('you really like mutton!')
if 'beef' in fruits:
	print('you really like beef!')
	
users = ['admin','tp','mh','dd','lz']
#users = []
if users:
	for user in users:
		t_str = ''
		if user == 'admin':
			t_str = 'Hello admin, would you like to see a status report?'
		else:
			t_str = 'Hello '+user+", thank you for logging in again"
		print(t_str)
else:
	print('We need to find some users!')
new_users = [users[0],users[-1],'zx','zy','hzg']
for user in new_users:
	if user.lower() in users or user.upper() in users:
		print('you should input another name')
	else:
		print('you can use this name')

num = list(range(1,10))
for each in num:
	m_str = ''
	if each == 1:
		m_str = '1st'
	elif each == 2:
		m_str = '2nd'
	elif each == 3:
		m_str = '3rd'
	elif each <= 9:
		m_str = str(each)+'th'
	print(m_str)
		
		
