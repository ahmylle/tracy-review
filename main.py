'''
Docstring for main
#pig
#head
#rightears
left ear
#nose
#lefteyes
right eye
'''
from turtle import *
import turtle
setup(width=400, height=400)  #set window size
color('pink')
speed(10)
pensize(4)
#head
goto(0,-100)
begin_fill()
fillcolor('pink')
circle(80,)  #head
end_fill()
#ear
color('pink')
circle(80,115)

right(90)
begin_fill()
circle(35,100)
left(25)
circle(35,100)
fillcolor('pink')
end_fill()
#left ear
penup()
goto(0,-100)
pendown()
begin_fill()
seth(0)
circle(80,-115)

right(90)
begin_fill()
circle(-35,100)
right(25)
circle(-35,100)
fillcolor('pink')
end_fill()
#nose
penup()
goto(0, -85)
pendown()
fillcolor('hot pink')
seth(0)
begin_fill()
forward(10)
circle(20,180)
forward(20)

#leftside
circle(20,180)
forward(20)
end_fill()

#left eye 
penup()
goto(-30, -30)
pendown()
color('black')
begin_fill() 
circle(10)
fillcolor('black')
end_fill()
#right eye
penup()
goto(30, -30)
pendown()
begin_fill()
circle(10)
fillcolor('black')
end_fill()

#keep window open
done()