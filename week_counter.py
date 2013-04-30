import datetime
"""
dt = datetime.date(2010, 6, 16) 
wk = dt.isocalendar()[1]
print (wk)

dt = datetime.date.today()
print (dt)
wk = dt.isocalendar()[1]
print (wk)
"""

def get_date():
	""" (None) -> int 
	asks user for a date and returns the week of the date
	"""
	today = raw_input('Was it today? (y/n) ')

	if today == 'y' or today == 'Y':
		date = datetime.date.today()
	else:
		print ('When was it?')
		year = int(raw_input('year: '))
		month = int(raw_input('month '))
		day = int(raw_input('day: '))
		date = datetime.date(year, month, day)
	
	week = date.isocalendar()[1]
	return week

def add_date(week):
	with open('weektracker.txt', 'a') as myfile:
		myfile.write(str(week) + '\n')


if __name__ == '__main__':
	add_date(get_date())