from turtle import *

setup(1080, 1920)
hideturtle()
bgcolor("black")
speed(0)

COLORS = ["yellow", "light green", "cyan", "violet", "pink", "white"]

side = 0

while side < 1000:
    color(COLORS[side%6])
    forward(side)
    right(59)
    side += 1

mainloop()