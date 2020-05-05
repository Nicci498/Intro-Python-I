"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def new_calendar():
  arg = input('Select a month, year and/or see this month').split()
  yr = "20"
  mth = "05"    

  if len(arg) == 1:
    mth = arg[0]

  elif len(arg) == 2:
    mth = ans[0]
    yr = ans[1]
    print(yr)
  if mth.isdigit() == False or yr.isdigit() == False:
    return print('please only enter numbers')
  
  year = int(yr)
  month = int(mth)
  print(year)

  if month > 12 or month < 1:
    return print('please enter a valid month')
    
  print(calendar.month(year, month))
  print(f'month is {mth} and year is {yr}')
  
new_calendar()



# current_date = datetime.now()
# month = current_date.month
# year = current_date.year

# def change_month(new_month):
#   global month
#   month = new_month

# def change_year(new_year):
#   global year
#   year = new_year

# if len(sys.argv) == 2:
#   change_month(int(sys.argv[1]))
# elif len(sys.argv) == 3:
#   change_month(int(sys.argv[1]))
#   change_year(int(sys.argv[2]))
# print(calendar.month(year, month))



# date_and_time = datetime.now()
# today = date_and_time.day
# this_month = date_and_time.month
# this_year = date_and_time.year
# print(today, this_month, this_year)

# def new_calendar(*args):
#   if len(sys.argv) == 1:
#     print(calendar.month(this_year, this_month))
#   elif len(sys.argv) == 2:
#     print(calendar.month(this_year, sys.argv[1]))
#   elif len(sys.argv) == 3:
#     print(calendar.month(sys.argv[2], sys.argv[1]))
#   else:
#     return 'a usage statement to the terminal indicating the format that your program expects arguments to be given'
  
   
#nice formatted string of month print(calendar.month(2020, 5, w=3)) 
# print(calendar.weekheader(3)) #prints mo-su arg=name.length
# print(calendar.firstweekday()) # useful to have dates in number form
# print(calendar.month(2020, 5, w=3)) #nice formatted string of month
# print(calendar.monthcalendar(2020, 5)) #matrix (array of arrays of dates the weeks)
# print(calendar.calendar(2020))
# day_of_the_week = calendar.weekday(2020, 5, 6)
# print(day_of_the_week)
# is_leap = calendar.isleap(2020)
# print(is_leap)
# how_many_leap_days = calendar.leapdays(1990, 2021)#includes 90, but not 21
# print(how_many_leap_days)


