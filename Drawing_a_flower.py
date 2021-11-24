import turtle
import turtle

def desenha_petala(tartaruga, tamanho, arco):
    tartaruga.circle(tamanho, arco)
    tartaruga.left(180-arco)
    tartaruga.circle(tamanho, arco)
    tartaruga.left(180-arco)

x = 100
Aimi = turtle.Turtle()
num_petalas = 8
for i in range (num_petalas):
    desenha_petala(Aimi, 75, 75)
    Aimi.right(360/num_petalas)
Aimi.right(90)
Aimi.forward(x)
desenha_petala(Aimi, 50, 50)
Aimi.forward(x)

turtle.done()