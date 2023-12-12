
"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
"""




list_months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


"""
def main():
    print(format_date())
    

def format_date():
    while True:
        date=input("Date: ").strip()
        if "/" in date:
            try:
                month,day,year=date.split("/")
                if 1<=int(day)<=31 and 1<=int(month)<=12 and int(year)>0: 
                    return(f"{int(year):02}-{int(month):02}-{int(day):02}")
                    break
                else:
                    pass
            except:
                pass
        elif date.split()[0].title() in list_months:
            try:
                month,day,year=date.split(" ")
                month=list_months.index(month.title())+1
                day=day.replace(",","")                
                if 1<=int(day)<=31 and 1<=int(month)<=12 and int(year)>0: 
                    return(f"{int(year):02}-{int(month):02}-{int(day):02}")
                    break
                else:
                    pass
            except:
                pass
        else:
            pass
            
if __name__=="__main__":
    main()         
                

"""




"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
"""



def main():
    print(format_date())
    

def format_date():
    while True:
        date=input("Date: ").strip()
        try:
            month,day,year=date.split("/")
            if 1<=int(day)<=31 and 1<=int(month)<=12 and int(year)>0: 
                return(f"{int(year):02}-{int(month):02}-{int(day):02}")
                break
            else:
                pass
        except:
            try:
                month,day,year=date.split(" ")
                if month.endswith(","):
                    month=list_months.index(month.title())+1
                    day=day.replace(",","")                
                    if 1<=int(day)<=31 and 1<=int(month)<=12 and int(year)>0: 
                        return(f"{int(year):02}-{int(month):02}-{int(day):02}")
                        break
                    else:
                        pass
                else:
                    pass
            except:
                pass

            
if __name__=="__main__":
    main()         
                

