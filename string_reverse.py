"""
string_reverse.py: Recursive implementation of string_reverse(input string)
Authors: Jim Li
Credits: Starter code

CIS 210 assignment 4, part 2, Fall 2015. 
"""
import argparse      # Used in main program to get PIN code from command line
from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

def string_reverse(the_string):
    """
    Set a recursion to reverse the string
    """
    if len(the_string) > 0:
        return the_string[-1] + string_reverse(the_string[:-1])
    else:
        return the_string

def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of string_reverse()")
    parser.add_argument("string", type=str, help="String to reverse.")
    args = parser.parse_args()  # gets arguments from command line
    the_string = args.string
    print(string_reverse(the_string))

if __name__ == "__main__":
    main()     


