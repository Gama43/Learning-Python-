import turtle
import math

Aimi = turtle.Turtle()
Aimi.speed(10)

x = 100

#Estrutura do relógio
Aimi.circle(50)

#horas
Aimi.up()
Aimi.left(90)
Aimi.forward(x/20)
Aimi.right(90)
Aimi.down()

for i in range(12):
    Aimi.dot(x/25, 'black')
    Aimi.up()
    Aimi.circle(45, 30)
    Aimi.down()

#ponteiros_posição
Aimi.up()
Aimi.left(90)
Aimi.forward(x/2 - x/20)
Aimi.down()

#Ponteiro_A
Aimi.left(60)
Aimi.forward(x/4)
Aimi.right(180)
Aimi.forward(x/4)

#Ponteiro_B
Aimi.color('red')
Aimi.left(124)
Aimi.forward(x/2.5)
Aimi.right(180)
Aimi.forward(x/2.5)

#Ponteiro_C
Aimi.color('black')
Aimi.left(90)
Aimi.forward(x/4 + x/10)

turtle.done()