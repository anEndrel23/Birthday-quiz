"""
birthday.py
Author: <your name here>
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

monthnames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

monthnames.index['months'] = monthnames.index['months'] + 1

winter == monthnames[0,1] and monthnames[11]




if month == october and day == 31:
    print("You were born on Halloween!")
elif monthnames.index['month'] == todaymonth and day == todaydate:
        print("Happy birthday!")
elif 
    if monthnames.index['month'] == 1 or monthnames.index['month'] == 2 or monthnames.index['month'] == 12:
        season = 'winter'
    if monthnames.index['month'] >= 3 and monthnames.index['month'] <= 5
        season = 'spring'
    if monthnames.index['month'] >= 6 and monthnames.index['month'] <= 8
        season = 'summer'
    if monthnames.index['month'] >= 9 and monthnames.index['month'] <= 11
        season = 'fall'
    if year < 1979:
        time = 'stone age'
        

