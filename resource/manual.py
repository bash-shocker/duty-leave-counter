from resource import duty_leave

def man():
	atd = int(input("\n\n\tEnter the total number of hours you've attended: "))
	tot = int(input("\n\tEnter the total hours:"))
	x = tot - atd
	y = tot - x
	perc = (y/tot)*100
	print('\n\n\tYour overall percentage is {}'.format(perc))
	if perc >= 75.00:
		print('\n\n\t\tBoy! You have made it!!')
	else:
		duty_leave.calculate(atd,tot)

