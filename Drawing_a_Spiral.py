import turtle
import math

x = 8
Aimi = turtle.Turtle()
Aimi.speed(10)

for x in range(56, 440, 2):
    Aimi.forward(x/2)
    Aimi.right(92)

turtle.done()