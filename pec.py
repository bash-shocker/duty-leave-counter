import re
import csv
import sys
import time
import urllib.request
import os.path
from os import path
import socket
import urllib
from resource import duty_leave
from resource import loading
from resource import manual
from resource import welcome
from resource import validate

welcome.hola()
print('\n\n\t\t\tDUTY LEAVE COUNTER :P\n\n')
print('\n\n\t1.Manually check the attendance')
print('\n\n\t2.Automatically get the data from college website')

check = True
while check:

	choice = input('\n\n\tEnter your choice: ')
	if choice == '1':

		manual.man()

	elif choice == '2':
				#retrieving file from the internet

				try:
					loading.text()
					url = 'http://download1593.mediafire.com/pmmp1m71tgjg/i2rda38y5mn8262/_Attendance+S4+CSE+2019+-+Sheet1.csv'
					urllib.request.urlretrieve(url, 'attendance.csv')
				except:
					print('\n\n\tPlease connect to the internet!')
					print('\n\n\tExiting...')
					time.sleep(5)
					quit()
					
				#opening the csv file and converting it to lists

				file = open ('attendance.csv')
				file_read = csv.reader(file)
				file_data = list(file_read)
				rollno = input('\n\n\n\tEnter your roll number(pec17csxxx) : ')
				roll_no = rollno.upper()
				validate.check(roll_no)
				for row in range (1,41):

					for string in file_data[row]:

						if string == roll_no:


							name = file_data[row][1]
							maths = float(file_data[row][3])
							cao = float(file_data[row][5])
							os = float(file_data[row][7])
							oops = float(file_data[row][9])
							dbms = float(file_data[row][11])
							ls = float(file_data[row][13])
							maths_tot = int(file_data[2][2])
							cao_tot = int(file_data[2][4])
							os_tot = int(file_data[2][6])
							oops_tot = int(file_data[2][8])
							dbms_tot = int(file_data[2][10])
							ls_tot = int(file_data[2][12])
							maths_atd = int(file_data[row][2])
							cao_atd = int(file_data[row][4])
							os_atd = int(file_data[row][6])
							oops_atd = int(file_data[row][8])
							dbms_atd = int(file_data[row][10])
							ls_atd = int(file_data[row][12])
							minimum = 75.00


							print('\n\tHello {}'.format(name))
							print('\n\n\tYour current attendance is\n')
							print('\tMaths : {}%  Attended periods : {} out of {} periods'.format(maths,maths_atd,maths_tot))
							print('\tCAO   : {}%   Attended periods : {} out of {} periods'.format(cao,cao_atd,cao_tot))
							print('\tOS    : {}%  Attended periods : {} out of {} periods'.format(os,os_atd,os_tot))
							print('\tOOPS  : {}%  Attended periods : {} out of {} periods'.format(oops,oops_atd,oops_tot))
							print('\tDBMS  : {}%  Attended periods : {} out of {} periods'.format(dbms,dbms_atd,dbms_tot))
							print('\tLS    : {}%  Attended periods : {} out of {} periods'.format(ls,ls_atd,ls_tot))

							if maths >= minimum and cao >= minimum and os >= minimum and oops >= minimum and dbms >= minimum and ls >= minimum : 

									
								print("\n\n\tHey {} you don't need to worry about your attendance as you are over the margin".format(name))

							else:

								print('\n\n\tOops!! Your attendance is low for ')

								if maths < minimum :
									print ('\nMaths')
									duty_leave.calculate(maths_atd,maths_tot)
									print('\n\n')
								if cao < minimum :
									print ('CAO')
									duty_leave.calculate(cao_atd,cao_tot)
									print('\n\n')
								if os < minimum :
									print ('OS')
									duty_leave.calculate(os_atd,os_tot)
									print('\n\n')
								if oops < minimum :
									print ('OOPS')
									duty_leave.calculate(oops_atd,oops_tot)
									print('\n\n')
								if dbms < minimum :
									print ('DBMS')
									duty_leave.calculate(dbms_atd,dbms_tot)
									print('\n\n')
								if ls < minimum :
									print ('LS')
									duty_leave.calculate(ls_atd,ls_tot)
									print('\n\n')

								else:
									print('Null')
	else:
		print('\n\n\tWrong Choice!! Try again!')

	again = input('\n\n\n\tWant to check again (y/n)? : ')
	if again == 'y' :
		check = True
	else :
		check = False


		
			
