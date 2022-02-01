numero = int(input())

primo = True
raiz = int(numero**(1/2))
if numero == 1:
    primo = False

else:
    for divisor in range(2, raiz+1):
        if numero%divisor == 0:
            primo = False

print(primo)