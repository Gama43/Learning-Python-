import turtle
import math

construtor = turtle.Turtle()

x = 100

#casa
construtor.fillcolor('blue')
construtor.begin_fill()
for i in range(2):
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)
construtor.end_fill()

#porta
construtor.forward(x/4)
construtor.left(90)

construtor.fillcolor('red')
construtor.begin_fill()
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)
construtor.end_fill()

#janela
construtor.up()
construtor.left(90)
construtor.forward(x/4)
construtor.left(90)
construtor.forward(x/3)
construtor.down()

construtor.fillcolor('white')
construtor.begin_fill()
for i in range(4):
    construtor.forward(x/3)
    construtor.right(90)

#janela 02
construtor.up()
construtor.right(90)
construtor.forward(x/3 + x/4)
construtor.down()

for i in range(4):
    construtor.forward(x/3)
    construtor.left(90)
construtor.end_fill()

#telhado
construtor.up()
construtor.forward(x/3 + x/4)
construtor.left(90)
construtor.forward(x - x/3)
construtor.right(90)
construtor.down()

construtor.fillcolor('brown')
construtor.begin_fill()
construtor.forward(x/8)
construtor.left(135)
construtor.forward(x * math.sqrt(2.5))
construtor.left(90)
construtor.forward(x * math.sqrt(2.5))
construtor.end_fill()


turtle.done()