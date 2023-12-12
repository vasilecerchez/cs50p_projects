

'''
name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
"Boot, Terry",Ravenclaw
"Brown, Lavender",Gryffindor
"Bulstrode, Millicent",Slytherin
"Chang, Cho",Ravenclaw
"Clearwater, Penelope",Ravenclaw
"Crabbe, Vincent",Slytherin
"Creevey, Colin",Gryffindor
"Creevey, Dennis",Gryffindor
"Diggory, Cedric",Hufflepuff
"Edgecombe, Marietta",Ravenclaw
"Finch-Fletchley, Justin",Hufflepuff
"Finnigan, Seamus",Gryffindor



Even though each “row” in the file has three values 
(last name, first name, and house), the first two are combined into one
“column” (name), escaped with double quotes, with last name and first name 
separated by a comma and space. Not ideal if Hogwarts wants to send a form 
letter to each student, as via mail merge, since it’d be strange to start a 
letter with:

Dear Potter, Harry,

Rather than with, for instance:

Dear Harry,

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed
to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, 
first, last, and house.
Converts that input to that output, splitting each name into a first name and
last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the 
first cannot be read, the program should exit via sys.exit with an 
error message.

'''


import csv
import sys


def main():
    restriction() 
    try:
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            with open(sys.argv[2],"w", newline="") as file2:
                writer=csv.DictWriter(file2, fieldnames=["first","last","house"])
                writer.writerow({"first":"first","last":"last","house":"house"})
                for line in reader:
                    house=line["house"]
                    last_name, first_name=line["name"].split(", ")
                    writer.writerow({"first":first_name,"last":last_name,"house":house})
                
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
    

def restriction():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1][-4:]!=".csv":
        sys.exit("Not a CSV file")
    elif sys.argv[2][-4:]!=".csv":
        sys.exit("Not a CSV file")  
        

if __name__=="__main__":
    main()     
