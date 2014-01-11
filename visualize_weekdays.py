import numpy as np
import matplotlib.pyplot as plt

def get_weekday_tracking():
	""" (None) -> list
	gets weeks from file
	puts them into list
	returns list
	"""
	year = raw_input('Which year do you want to visualize? ')
	x_coords = []
	try:
		f = open('tracking/weekdaytracker'+year+'.txt', 'r')
		for i, line in enumerate(f):
			# appends line to list (cutting '\n' at the end of each line)
			x_coords.append(line[: -1])
		
	except (IOError):
		print "Error reading file weekdaytracker"+year+".txt"

	weekdays = {
		'Monday': 0,
		'Tuesday': 0,
		'Wednesday': 0,
		'Thursday': 0,
		'Friday': 0,
		'Saturday': 0,
		'Sunday': 0
	}

	for i in x_coords:
		for j in weekdays:
			if i == j:
				weekdays[j]+=1
	
	return weekdays

def visualize(weekdays):
	N = 7
	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots()

	print weekdays

	occurences = [0, 0, 0, 0, 0, 0, 0]

	for key, value in weekdays.iteritems():
		occurences[map_weekday(key)] = value

	rects1 = ax.bar(ind, occurences, width, color='r')

	# add some
	ax.set_ylabel('Occurences')
	ax.set_title('Occurences per weekday')
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') )

	#autolabel(rects1)
	plt.show()

def map_weekday(daystring):
	return {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }[daystring]

if __name__ == '__main__':
	visualize(get_weekday_tracking())
