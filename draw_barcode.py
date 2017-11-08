"""
draw_barcode.py: Draw barcode representing a ZIP code using Turtle graphics
Authors:  Jim Li ID:951532421
Credits:  Starter code

CIS 210 assignment 3, part 2, Fall 2015.
"""
import argparse	                
import time
import turtle	


SLEEP_TIME = 30	
ENCODINGS = [[1, 1, 0, 0, 0],	
             [0, 0, 0, 1, 1],	
             [0, 0, 1, 0, 1],   
             [0, 0, 1, 1, 0],	
             [0, 1, 0, 0, 1],	
             [0, 1, 0, 1, 0],	
             [0, 1, 1, 0, 0],	
             [1, 0, 0, 0, 1],	
             [1, 0, 0, 1, 0],	
             [1, 0, 1, 0, 0]	
            ]
SINGLE_LENGTH = 25	

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    sum = 0
    for i in range(len(digits)):
        sum = sum + int(digits[i])
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit

"""
Draw each bar
args:
    my_turtle: inport turtle
    digit: input binary digit to draw bar
"""
def draw_bar(my_turtle, digit):
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()

"""
Encode the zip and compute the check zip to binary digit and then draw the bar
arg:
    zip: the zip prepared to be printed by barcode
"""
def draw_zip(my_turtle, zip):
    draw_bar(my_turtle, 1) # start bar
    binary = []
    origin_zip = str(zip) # save the original zip for computing check digit
    while zip > 0:
        reminder = zip%10 # extract each digit from zip
        binary = ENCODINGS[reminder] + binary # encode each digit to binary number
        zip = zip//10 
    binary = binary + ENCODINGS[compute_check_digit(origin_zip)]
    for i in range(len(binary)):
        draw_bar(my_turtle, binary[i])
    draw_bar(my_turtle, 1) # end bar
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ZIP", type=int)
    args = parser.parse_args()
    zip = args.ZIP
    if zip <= 0 or zip > 99999:
        print("zip must be > 0 and < 100000; you provided", zip)
    else:
        my_turtle = turtle.Turtle()
        draw_zip(my_turtle, zip)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
