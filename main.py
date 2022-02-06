import turtle as t
import random
from turtle import Screen

scr = Screen()
tim = t
t.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

tim.speed("fastest")

def draw_spyroghraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spyroghraph(5)

scr.exitonclick()
