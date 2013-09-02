# import matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim

def get_weeks():
	""" (None) -> list
	gets weeks from file
	puts them into list
	returns list
	"""
	x_coords = []
	f = open('daytracker.txt', 'r')
	for i, line in enumerate(f):
		# appends line to list (cutting '\n' at the end of each line)
		x_coords.append(int(line[: -1]))

	return x_coords

def plot_graph(x):
	x_coords = x
	x_coords.append(0)
	# sorts list (in case the dates in the file are in the wrong order)
	x_coords.sort()
	y_coords = []
	
	for i in range(len(x_coords)):
		# add one y-value (prev_y+=1) for each x-value
		y_coords.append(i)

	# plots a graph with x and y coordinates
	plt.plot(x_coords, y_coords, 'b--')

	# labes the x and y axis
	plt.ylabel('occurences')
	plt.xlabel('days in year')

	# limit x axis to 52 weeks
	xlim (0, 365)
	ylim (0, y_coords[-1])

	# shows the plot
	plt.show()

if __name__ == '__main__':
	plot_graph(get_weeks())

	