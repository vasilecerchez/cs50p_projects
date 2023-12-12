
"""
Even so, in a file called lines.py, implement a program that expects exactly 
one command-line argument, the name (or path) of a Python file, and outputs 
the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the 
specified file’s name does not end in .py, or if the specified file does not
exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, 
is a comment. (A docstring should not be considered a comment.) 
Assume that any line that only contains whitespace is blank.
"""

import sys

def main():
    restriction()
    loc=0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if chech_line(line):
                    loc+=1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(loc)
        
# check if the line begins with # or if it is empty
def chech_line(line):
    if line.lstrip().startswith("#"):
        return False
    elif line.isspace(): # empty row
        return False
    return True

# control restrictions on the number of parameters
def restriction():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1][-3:]!=".py":
        sys.exit("Not a Python file") 
    
if __name__=="__main__":
    main()     



