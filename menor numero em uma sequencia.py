qtd_n = int(input())

menor = 1000

for i in range (0,qtd_n):
    n = int(input())

    if n < menor:
        menor = n

print(menor)