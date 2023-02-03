from turtle import *

shape("turtle")
bgcolor("black")
speed(0)


def fractal_tree(size, levels, angle):
    if levels == 0:
        return

    forward(size)
    right(angle)

    fractal_tree(size*0.8, levels-1, angle)

    left(angle*2)
    fractal_tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


COLORS = ["red", "orange", "yellow", "light green", "cyan", "violet", "pink", "white"]

for i in COLORS:
    color(i)
    left(45)
    fractal_tree(70, 7, 30)

mainloop()