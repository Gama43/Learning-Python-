n_termo = int(input())
n1 = 1
n2 = 1
soma = 0

for i in range(1, n_termo+1):
    n1 = n2
    n2 = soma
    soma = n1+n2
print(soma)
