from statistics import geometric_mean


lista = []
qnt_valores = int(input())

for i in range(qnt_valores):
    n = float(input())
    lista.append(n)

print(geometric_mean(lista))