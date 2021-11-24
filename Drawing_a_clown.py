import turtle
import math

Aimi = turtle.Turtle()
Aimi.speed(10)

x = 50
Aimi.color('blue')
Aimi.speed(10)

Aimi.left(90)

#olho_1
Aimi.fillcolor('black')
Aimi.begin_fill()
Aimi.circle(x/3, 360)
Aimi.end_fill()

for i in range (2, 8, 2):
    Aimi.circle ((i+1)*x/4, 360)

Aimi.left(180)

#olho_2
Aimi.fillcolor('black')