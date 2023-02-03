from turtle import *

shape("turtle")
bgcolor("black")
pensize(3)
speed(0)


COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

while True:
    for i in range(len(COLORS)):
        for item in COLORS:
            color(item)
            circle(150)
            lt(15)

mainloop()
