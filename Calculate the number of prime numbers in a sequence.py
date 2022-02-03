x = int(input())
y = int(input())

qtd_primos = 0

for i in range(x, y+1):

    qtd_primos += 1

    for c in range(2, i):
        if (i % c == 0):
            qtd_primos -= 1
            break

print(qtd_primos)