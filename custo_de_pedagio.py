import math
 
comprimento_da_estrada,distancia_entre_pedagios = [int(w) for w in input().split()]

custo_por_km,valor_do_pedagio = [int(w) for w in input().split()]

numero_de_pedagios = comprimento_da_estrada / distancia_entre_pedagios

custo1 = numero_de_pedagios * valor_do_pedagio

custo2 = (comprimento_da_estrada * custo_por_km)

print(custo1+custo2)