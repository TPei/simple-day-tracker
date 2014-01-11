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
		yesterday = raw_input('Was it yesterday? (y/n) ')
		if yesterday == 'y' or yesterday == 'Y':
			date = datetime.date.today() - datetime.timedelta(1)

		else:
			print ('When was it?')
			year = int(raw_input('year: '))
			month = int(raw_input('month '))
			day = int(raw_input('day: '))
			date = datetime.date(year, month, day)
	
	week = date.isocalendar()[1]
	first = datetime.date(date.year, 01, 01)
	days = date - first

	weekday = date.weekday()
	weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	return week, days.days, weekdays[weekday], date.year

def add_week(week, year):
	with open('tracking/weektracker'+year+'.txt', 'a') as myfile:
		myfile.write(str(week) + '\n')


def add_day(day, year):
	with open('tracking/daytracker'+year+'.txt', 'a') as myfile:
		myfile.write(str(day) + '\n')

def add_weekday(weekday, year):
	with open('tracking/weekdaytracker'+year+'.txt', 'a') as myfile:
		myfile.write(str(weekday) + '\n')


if __name__ == '__main__':
	week, day, weekday, year = get_date()
	add_week(week, str(year))
	add_day(day, str(year))
	add_weekday(weekday, str(year))
