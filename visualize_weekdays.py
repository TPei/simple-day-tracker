def get_weekdays():
	""" (None) -> list
	gets weeks from file
	puts them into list
	returns list
	"""
	x_coords = []
	f = open('weekdaytracker.txt', 'r')
	for i, line in enumerate(f):
		# appends line to list (cutting '\n' at the end of each line)
		x_coords.append(line[: -1])

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
	

	print weekdays
	return weekdays

if __name__ == '__main__':
	get_weekdays()