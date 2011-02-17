
from turtle import *
from math import *

def block(s,a):
    # Diamond
    fillcolor('white')
    begin_fill()
    fd(s)
    rt(a)
    fd(s)
    rt(90 - a/2)
    end_fill()
    # Tower
    fillcolor('black')
    begin_fill()
    fd(s*2)
    rt(90-a/2)
    fd(s)
    rt(a)
    fd(s)
    rt(90-a/2)
    fd(s*2)
    end_fill()
    fillcolor('white')
    begin_fill()
    rt(90+a/2)
    fd(s)
    lt(a)
    fd(s)
    end_fill()

def kopimi(s, a):
    lt(a/2)
    # Top-right of K
    for z in range(2):
        block(s,a)
        bk(s*2)
    block(s,a)

    # Bottom-right of K
    for z in range(2):
        block(s,a)
    for z in range(4):
        bk(s)
        rt(a)
        bk(s)
        lt(a)

    # Left of K
    rt(a)
    bk(s)
    lt(a)
    for z in range(4):
        block(s,a)
        bk(s)
    block(s,a)
    rt(a/2)

def trirow(s,row):
    rt(45+90)
    fd(sqrt((row*s)**2*2))
    lt(45)
    fd(s)
    lt(45+90)
    fd(sqrt(((row+1)*s)**2*2))
    rt(45)

def triangle(s, ksize, kangle):
    lt(45)
    penup()

    fillcolor('red')
    begin_fill()
    fd(s)
    rt(90)
    fd(s)
    end_fill()

    fillcolor('orange')
    begin_fill()
    trirow(s,1)
    end_fill()

    fillcolor('yellow')
    begin_fill()
    trirow(s,2)
    end_fill()

    fillcolor('green')
    begin_fill()
    trirow(s,3)
    end_fill()

    fillcolor('blue')
    begin_fill()
    trirow(s,4)
    end_fill()

    fillcolor('purple')
    begin_fill()
    trirow(s,5)
    end_fill()

    # Position half-way across red's base
    lt(180)
    fd(s*5)
    lt(45)
    fd(sqrt(s**2*2)/2)
    # Position of K's start
    lt(kangle/2)
    fd(ksize)
    lt(180-(kangle/2))

    pendown()

    kopimi(ksize, kangle)

if __name__ == '__main__':
    setup()
    triangle(40,10,70)
    hideturtle()
