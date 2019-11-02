msg = 'Let me see if I can find you a Subaru'
cay_type = input('Which type car would like ?')
print(msg)

customer_num = int(input('How much people will come?'))
if customer_num > 8 :
	new_msg = 'Sorry,we don\'t have enough seats'
else:
	new_msg = 'Welcome,my friends,please have a seat!'
print(new_msg)

if int(input('Please input a numer:'))%10 == 0 :
	msg = 'this num is a multiple of 10'
else:
	msg = 'this num not is a multiple of 10'
print(msg)


