def hola():
	from datetime import datetime
	now = datetime.now()
	current_time = now.strftime("%H")
	new_time = int(current_time)
	if new_time >= 6 and new_time < 12 :
		print('\n\n\n\n\t\tEach good morning we are born again, what we do today is what matters most\n\n')
	if new_time >= 12 and new_time < 16 :
		print('\n\n\n\n\tThe afternoon is not only the middle of the day it is the time to complete our essential task and go ahead in life\n\n')
	if new_time >= 16 and new_time < 22 :
		print("\n\n\n\n\tThe evening's the best part of the day. You've done your day's work. Now you can put your feet up and enjoy it\n\n")
	if new_time >= 22 and new_time < 6 :
		print('\n\n\n\n\t\t\tA good sleep is always good for your health!!\n\n')


