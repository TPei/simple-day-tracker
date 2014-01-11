simple-day-tracker
==================

Add occurences to keep track of special dates. Visualize them using days in year, weeks in year or weekdays
![alt tag](https://raw.github.com/dragon5689/simple-day-tracker/master/visualize_days.png)
![alt tag](https://raw.github.com/dragon5689/simple-day-tracker/master/visualize_weeks.png)
![alt tag](https://raw.github.com/dragon5689/simple-day-tracker/master/visualize_weekdays.png)

simply run the add_occurence.py program to add the week, day and weekday of an occurence
whenever you want a graph created run the visualize_days.py, visualize_weeks.py visualize_weekdays.py file

for each date the week in year will be added to the weektracker.txt
for each date the day in year will be added to daytracker.txt
for each date the day of the week will be added to weekdaytracker.txt

note that entering wrong values corrupts the tracking file
while entering an invalid date simply crashes the add_occurence.py file,
entering a valid date from another year corrupts the data
you can however simply open the stracker.txt file and remove the last entry
(make sure you sustain the empty line at the end of the program)

examples for thins you could track:
weeks/days in which:
- you were very (un)productive
- you spent more money than you wanted
- you met with someone or someone from a group of certain people
 
By default the trackings folder is empty and tracking files are created on firs use. If there are any file permission problems on your system simply create the aforementioned empty .txt files.

