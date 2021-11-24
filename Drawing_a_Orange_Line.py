import turtle
import math

Aimi = turtle.Turtle()
Aimi.speed(10)

for i in range(20, 60, 5):
    Aimi.fillcolor('orange')
    Aimi.begin_fill()
    Aimi.circle(i)
    Aimi.up()
    Aimi.forward((12/5) * i)
    Aimi.down()
    Aimi.end_fill()

turtle.done()