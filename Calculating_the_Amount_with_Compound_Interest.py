import math

capital = float(input())
numeros_de_meses = int(input())
taxa = float(input())

montante = capital * ((1 + taxa / 100) **numeros_de_meses) 


print(round(montante, 2))