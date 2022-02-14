qtd_n = int(input())

maior = 0

for i in range(1,qtd_n+1):
    n = int(input())
    if n > maior:
        maior = n
        linha = i

print(maior, linha)