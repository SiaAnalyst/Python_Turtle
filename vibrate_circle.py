from turtle import *

shape("turtle")
bgcolor("black")
speed(0)
penup()
goto(-20, 180)
pendown()

COLORS = ["red", "orange", "yellow", "light green", "cyan", "violet", "pink", "white"]

size = 0
angle = 0

while angle <= 210:
    for i in COLORS:
        color(i)
        fd(size)
        rt(angle)
        size += 3
        angle += 1


hideturtle()
mainloop()
