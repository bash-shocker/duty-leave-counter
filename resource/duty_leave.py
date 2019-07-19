def calculate(cur_atd,tot):
	req_perc = 75.00
	y = (req_perc/100)*tot
	x = tot - y
	req_atd = tot - x
	req_days =  req_atd - cur_atd
	print ('\n\n\tyou need {} more hours to level the attendance!'.format(int(req_days)))







