
"""
Whereas most countries use a 24-hour clock, the United States tends to use a
12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would 
say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an
abbreviation for “ante meridiem” and “PM” is an abbreviation for 
“post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects
a str in either of the 12-hour formats below and returns the corresponding str
in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be
capitalized (with no periods therein) and that there will be a space
before each. Assume that these times are representative of actual times, 
not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those 
formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
But do not assume that someone’s hours will start ante meridiem and end post 
meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or 
implement other functions as you see fit, but you may not import any other 
libraries. You’re welcome, but not required, to use re and/or sys.
"""


import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches:=re.search(r'^(\d\d?(?:\:\d\d)?) ([A-Z]{2}) to (\d\d?(?:\:\d\d)?) [A-Z]{2}$',s):
        am_pm=matches.groups()[1]
        start_h, start_m=extract_minutes(matches.groups()[0],am_pm)
        end_h, end_m=extract_minutes(matches.groups()[2],am_pm)

        
        if not 0<=int(start_m)<60 or not 0<=int(end_m)<60 or not 0<=int(start_h)<=12 or not 0<=int(end_h)<=12:
                raise ValueError
        
        
        if am_pm=="AM":
            return f'{int(start_h):02}:{start_m} to {(int(end_h)+12):02}:{end_m}'
        else:
            return f"{(int(start_h)+12):02}:{start_m} to {int(end_h):02}:{end_m}"      
    else:
        raise ValueError




def extract_minutes(hm,am_pm):
    if ":" in hm:
        start_h,start_m=hm.split(":")
    else:
        start_h = hm
        start_m="00"
    if am_pm=="AM" and start_h=="12":
        start_h="00"
    return start_h,start_m





if __name__ == "__main__":
    main()