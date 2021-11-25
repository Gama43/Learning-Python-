import math

distancia = float(input())
combustivel_gasto = float(input())
consumo = distancia / combustivel_gasto
print('{:.3f} km/l'.format(consumo))