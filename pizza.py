

"""
Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+


In a file called pizza.py, implement a program that expects exactly one 
command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at 
pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .csv, or if the specified file 
does not exist, the program should instead exit via sys.exit.

"""




from tabulate import tabulate
import sys
import csv



def main():
    restriction()
    table=[]
    try:
        with open(sys.argv[1]) as file:
            reader=csv.reader(file)
            for line in reader:
                table.append(line)
    except FileNotFoundError:
            sys.exit("b")
    except FileExistsError:
        sys.exit("File does not exist")
           
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

def restriction():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1][-4:]!=".csv":
        sys.exit("Not a CSV file") 

if __name__=="__main__":
    main()  