import math
valor = float(input())
premio1 = float(valor*0.1)
sexo = input()
idade = int(input())

if sexo=='M' and idade<=24:
    premio2 = premio1
elif sexo=='M' and idade <=33:
    premio2 = premio1*0.9
elif sexo=='M' and idade>33:
    premio2 = premio1*0.8

if sexo=='F' and idade<=24:
    premio2 = premio1*0.95
elif sexo=='F' and idade <=33:
    premio2 = premio1*0.8
elif sexo=='F' and idade>33:
    premio2 = premio1*0.65

print('{:.2F}'.format(premio2))