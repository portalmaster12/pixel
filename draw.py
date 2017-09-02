#!python3.5
"""
This program draws shapes and fills them with colors.

Author: Ethan Bartlett
"""

#preliminaries
import turtle 

#functions
def turn(d):
    'turns based on user input'
    if d == "left":
        turtle.left(90) 
    else:
        turtle.right(90)
          
def makesq(s):
    """makes a square and returns variables for the corners
    s is starting point
    """
    
    corner = []
    turtle.goto(0,0)
    
    turtle.forward(l)
    corner.append(turtle.pos())

    turn(d)
    turtle.forward(l)
    corner.append(turtle.pos())

    turn(d)
    turtle.forward(l)
    corner.append(turtle.pos())

    turn(d)
    turtle.forward(l)
    corner.append(turtle.pos())

    return(corner)


#draw stuff

l = input("input the squares length")
#d = raw_input("left or right(type it exatly as the question presented it)")
d="left"
fsq = makesq((0,0))
turtle.goto(fsq[0])
#turtle.
    


