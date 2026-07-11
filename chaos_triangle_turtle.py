# 2026.07.12
# chaos_triangle_turtle.py

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")

points = [(-300, -220), (300, -220), (0, 300)]
x, y = 0, 0

for i in range(20_000):

    tx, ty = random.choice(points)
    x, y = (x + tx) / 2, (y + ty) / 2

    if i > 20:

        pen.goto(x, y)
        pen.dot(2)

screen.update()
turtle.done()
