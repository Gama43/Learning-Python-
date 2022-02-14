qtd_n = int(input())

menor = 100

for i in range(0,qtd_n):
    n = int(input())
    if n < menor:
        segundo_menor = menor
        menor = n
    else:
        if n < segundo_menor:
            segundo_menor = n

print(segundo_menor)