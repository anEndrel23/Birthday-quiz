"""
birthday.py
Author: Andrew
Credit: Matt
Assignment

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
month = input("Hi "+name+", what was the name of the month you were born in? ")
year = input("And what year were you born in, "+name+"? ")
day = input("And the day? ")

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month_names.index['months'] = month_names.index['months'] + 1

winter == month_names[0,1] and month_names[11]




if month == october and day == 31:
    print("You were born on Halloween!")
elif month_names.index['month'] == todaymonth and day == todaydate:
    print("Happy birthday!")
else: 
    if month_names.index['month'] == 1 or month_names.index['month'] == 2 or month_names.index['month'] == 12:
        season = 'winter'
    if month_names.index['month'] >= 3 and month_names.index['month'] <= 5:
        season = 'spring'
    if month_names.index['month'] >= 6 and month_names.index['month'] <= 8:
        season = 'summer'
    if month_names.index['month'] >= 9 and month_names.index['month'] <= 11:
        season = 'fall'
    if year < 1979:
        time = 'stone age'
    if year >= 1980 and year < 1990:
        time = 'eighties'
    if year >= 1990 and year < 2000:
        time = 'nineties'
    if year >= 2000:
        time = 'two thousands'
    print(""+name+", you are a "+season+" baby of the"+time+".")

