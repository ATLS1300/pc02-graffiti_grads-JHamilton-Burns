#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Jessie Hamilton
May 29, 2020
'''

import turtle 

turtle.colormode(255)

 
panel = turtle.Screen()
w = 750 
h = 750 
panel.setup(width=w, height=h) 


image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)


#=======Add your code here======

t = turtle.Turtle()
t.fillcolor(176,27,46)
t.pencolor(176,27,46)
t.pensize(20)

# lasers out of Jeff's eyes
lefteye = (-15,108)
t.pensize=15
t.penup()
t.goto(lefteye)
t.pendown()
t.goto(200,-150)


righteye = (42,120)
t.penup()
t.goto(righteye)
t.pendown()
t.goto(400,-50)

# Jeff's green maraca
hand = (45,-65)
t.pen(pencolor="green", fillcolor="green", pensize=15, speed=9)
t.penup()
t.goto(hand)
t.pendown()
t.left(60)
t.fd(80)
t.penup()
t.goto(105,-20)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

# Jeff's blue party hat
t.penup()
t.pen(pencolor="blue", fillcolor="blue", pensize=15, speed=9)
leftForehead = (-90,195)
t.goto(leftForehead)
t.pendown()
t.begin_fill()
t.right(30)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

# varying shapes and colors that decorate Jeff's maraca
t.penup()
t.pen(pencolor="white", fillcolor="white", pensize=5, speed=20)
t.goto(100,-15)
t.pendown()
t.begin_fill()
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.end_fill()


t.penup()
t.pen(pencolor="pink", fillcolor="pink", pensize=5, speed=20)
t.goto(60,-22)
t.pendown()
t.lt(30)
t.fd(15)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(15)
t.rt(90)
t.fd(10)


t.penup()
t.pen(pencolor="red", fillcolor="red", pensize=5, speed=20)
t.goto(90,-10)
t.pendown()
t.begin_fill()
t.fd(10)
t.lt(120)
t.fd(10)
t.lt(120)
t.fd(10)
t.end_fill()

t.penup()
t.pen(pencolor="purple", fillcolor="purple", pensize=5, speed=20)
t.goto(70,5)
t.pendown()
t.begin_fill()
t.right(40)
t.fd(10)
t.lt(120)
t.fd(10)
t.lt(120)
t.fd(10)
t.end_fill()

t.penup()
t.pen(pencolor="orange", fillcolor="orange", pensize=5, speed=20)
t.goto(70,14)
t.pendown()
t.begin_fill()
t.lt(15)
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.end_fill()

t.penup()
t.pen(pencolor="blue", fillcolor="blue", pensize=5, speed=9)
t.goto(53,1)
t.pendown()
t.begin_fill()
t.right(60)
t.fd(10)
t.lt(120)
t.fd(10)
t.lt(120)
t.fd(10)
t.end_fill()

t.penup()
t.pen(pencolor="yellow", fillcolor="yellow", pensize=5, speed=9)
t.goto(90,15)
t.pendown()
t.begin_fill()
t.right(20)
t.fd(10)
t.lt(120)
t.fd(10)
t.lt(120)
t.fd(10)
t.end_fill()

t.penup()
t.pen(pencolor="lightblue", fillcolor="lightblue", pensize=5, speed=15)
t.goto(100,0)
t.pendown()
t.begin_fill()
t.lt(40)
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.end_fill()


#=======Clean up code (do not change)======
turtle.done()









