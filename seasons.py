
"""
Assuming there are 365 days in a year, there are 
 minutes in that same year (because there are 24 hours in a day and 60 minutes 
 in an hour). But how many minutes are there in two or more years? 
 Well, it depends on how many of those are leap years with 366 days, 
 per the Gregorian calendar, as some of them could have 
 additional minutes. In fact, how many minutes has it been since you were born?
 Well, that, too, depends on how many leap years there have been since! 
 There is an algorithm for such, but let’s not reinvent that wheel. 
 Let’s use a library instead. Fortunately, Python comes with a datetime
 module that has a class called date that can help, per d
 
ocs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for 
their date of birth in YYYY-MM-DD format and then sings prints how old they 
are in minutes, rounded to the nearest integer, using English words instead
of numerals, just like the song from Rent, without any and between words. 
Since a user might not know the time at which they were born, assume,
for simplicity, that the user was born at midnight (i.e., 00:00:00) 
on that date. And assume that the current time is also midnight. 
In other words, even if the user runs the program at noon, assume that it’s 
actually midnight, on the same date. Use datetime.date.today to get
today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also 
with one or more other functions as well:
"""

from datetime import date
import sys
import inflect
import re
p = inflect.engine()


def main():
    birth_date=input("Date of Birth: ").strip() 
    check_date(birth_date)
    print(numbers_to_words(daystoseconds(two_date_time(birth_date)))+" minutes")


def check_date(data):
    try:
        match=re.search(r'^(\d{4})\-(\d{2})\-(\d{2})$',data)
        year=match.groups()[0]
        month=match.groups()[1]
        day=match.groups()[2]
    except:
        sys.exit("ciaooo..........")

    if int(year)>int(date.today().year):
        sys.exit()
    elif not 1<=int(month)<=12:
        sys.exit()
    elif not 1<=int(day)<=31:
        sys.exit()
    return True # non è necessario

def two_date_time(day_date):
    today_date=date.today()
    born_date=date.fromisoformat(day_date)#.date()
    return (today_date-born_date).days
   
def daystoseconds(days):
    return days*24*60   

def numbers_to_words(number):
    return p.number_to_words(number, andword="").capitalize()
     
if __name__ == "__main__":
    main()