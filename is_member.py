"""
is_member.py: Recursive implementation of is_member() on a set
              represented by a sorted list of integers
Authors: Jim Li
Credits: Starter code

CIS 210 assignment 4, part 1, Fall 2015. 
"""
import argparse      # Used in main program to get PIN code from command line
from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

def gen_set(set_file):
    """
    Extract members from set file then put them into a list
    """
    the_set = []
    for line in set_file:
        the_set.append(line)
    the_set = sorted(the_set)
    return the_set

def is_member(set, number):
    """
    Set a recursion to check if the checking number is in the list
    """
    set = gen_set(set)
    midnum = len(set)
    midnum //= 2
    if number == int(set[midnum]):
        return True
    if int(midnum) > 0:
        if number > int(set[midnum]):
            return is_member(set[midnum:],number)
        else:
            return is_member(set[:midnum],number)
    else:
        return False


def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of is_member()")
    parser.add_argument("set", type=argparse.FileType('r'),
                        help="A text file containing set elements, one per line.")
    parser.add_argument("number", type=int, help="number to check for membership")
    args = parser.parse_args()  # gets arguments from command line
    set_file = args.set
    number = args.number
    the_set = gen_set(set_file)
    if is_member(the_set, number):
        print(number, "is an element of the set")
    else:
        print(number, "is not an element of the set")

if __name__ == "__main__":
    main()     
