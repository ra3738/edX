# Problem 1

from turtle import *
from random import *
import time

def spiral(initialLength, angle, multiplier):
    if initialLength < 1:
        return

    elif initialLength > 500:
        return

    else:
        c = choice( ['green','red','blue'] )
        color(c)
        forward(initialLength)
        left(angle)
        spiral(initialLength*multiplier, angle, multiplier)

# --------------------------------
# Problem 2

def chai(size):
    """ our chai function! """
    if (size<9): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai( size/2 )
        right(90)
        forward(size)
        left(90)
        chai( size/2 )
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

# --------------------------------
# Problem 3

def svtree(trunklength, levels):
    if (levels<1):
        return
    else:
        forward(trunklength)
        left(30)
        svtree(trunklength/2, levels-1)
        right(30)
        right(30)
        svtree(trunklength/2, levels-1)
        left(30)
        backward(trunklength)
        return
        
# --------------------------------
# Problem 4

def snowflake(sidelength, levels):
    """ fractal snowflake function
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)

def flakeside(sidelength, levels):
    speed('fastest')
    if (levels == 0):
        forward(sidelength)
        return
    else:
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)
        left(60)
        left(60)
        flakeside(sidelength/3, levels-1)
        right(60)
        flakeside(sidelength/3, levels-1)
        return



# --------------------------------

##from turtle import *    # loads the turtle library...
##
##width(5)        # make the turtle pen 5 pixels wide
##shape('turtle') # use a turtle shape!
##forward(100)    # turtle goes forward 100 steps
##right(90)       # turtle turns right 90 degrees
##up()            # turtle lifts its pen up off of the paper
##forward(100)    # turtle goes forward 100 steps
##down()          # turtle puts its pen down on the paper
##color("red")    # turtle uses red pen
##circle(100)     # turtle draws circle of radius 100 
##color("blue")   # turtle changes to blue pen
##forward(50)     # turtle moves forward 50 steps

# -------------------------------

##from turtle import *
##import time
##
##def poly( n, N ):
##    """ draws n sides of an N-sided regular polygon """
##    if n == 0:
##        return
##    else:
##        forward( 50 )   # 50 is hard-coded at the moment...
##        left( 360.0/N )
##        poly( n-1, N )

