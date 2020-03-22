courses=['maths','cao','os','oops','dbms','ls']
totalHours={}
attendedHours={}
percentageHours={}
name=file_data[row][1]
min=75.0
i=3 #variable to iterate through percentage attendance
j=2 #variable to iterate through total hours of the courseName
lowAttendanceSubjects=0 #to store the number of subjects that have low attendance
for courseName in courses:

	percentageHours[courseName]=float(file_data[row][i++])
	attendedHours[courseName]=int(file_data[row][j])
    totalHours[courseName]=int(file_data[2][j++])
	

print('\n\tHello {}'.format(name))
print('\n\n\tYour current attendance is\n')
	
for courseName in courses:
	print('\t{} : {}%  Attended periods : {} out of {} periods'.format(courseName,percentageHours[courseName],attendedHours[courseName],totalHours[courseName]))
	
for courseName in courses:
	if percentageHours[courseName]<min :
	    print('\n\n\tOops!! Your attendance is low for :'+courseName)
		duty_leave.calculate(attendedHours[courseName],totalHours[courseName])
		print('\n\n')
        lowAttendanceSubjects+=1

if lowAttendance==0:
	print("\n\n\tHey {} you don't need to worry about your attendance as you are over the margin".format(name))
	
	