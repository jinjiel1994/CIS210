"""
drawflower.py:  Draw flower from multiple squares using Turtle graphics
Authors: Jinjie(Jim) Li  ID:951532421
Credits: Information from canvas
CIS 210 assignment 1, Fall 2015. 
"""

import time
import turtle

def drawSquare(myTurtle, sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)

def drawFlower(myTurtle, numSquares, sideLength):
    i = 0
    j = int(numSquares)
    k = 360/j
    while i<j:
        drawSquare(myTurtle, sideLength)
        myTurtle.right(k)
        i += 1

def main():
    numsquares=input('numsquares=')
    sideLength=input('sideLength=')
    sideLength= int(sideLength)
    numsquares= int(numsquares)
    myTurtle = turtle.Turtle()
    drawFlower(myTurtle, numsquares, sideLength)
    time.sleep(10)

if __name__ == "__main__":
    main()
