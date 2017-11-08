"""
squareroot.py:  Approximate pi with iterative function
Authors: FIXME: Jinjie(Jim) Li
Credits: FIXME: Information from Canvas
CIS 210 assignment 2, Fall 2015. 
"""

import math
import argparse 

## Constants used by this program

def my_sqrt(number, iterations):
    """
    Generate an iterative approximation to the square root of a number
    args:
        number:  positive number to calculate the square root of
        iterations: number of iterations to perform
    returns:
        approximate value of the square root
    """
    value = 1
    for i in range(iterations):
        value = 0.5*(value+number/value)
    return value

def main():
    """
    Interaction if run from the command line.
    Magic for now; we'll look at what's going on here
    in the next week or two. 
    """
    parser = argparse.ArgumentParser(description="Iterative approximation for pi")
    parser.add_argument("Number", type=float, help="number (a float)")
    parser.add_argument("-i", "--iterations", type=int, help="iterations (an int)")
    args = parser.parse_args() 
    number = args.Number
    iterations = args.iterations
    value = my_sqrt(number, iterations)
    print("After", iterations, "iterations, sqrt(", number, ") =", value)
    print("This represents", '{:.2%}'.format(value/math.sqrt(number)-1), "error compared to the math library")

if __name__ == "__main__":
    main()     


