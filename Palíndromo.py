frase = str(input())

novafrase = ''

for i in frase:
    if i.isalpha():
        novafrase +=i

novafrase = novafrase.split()
frase = ''.join(novafrase)
frase2 = ''.join((reversed(frase)))

if frase == frase2:
    frase = True
else:
    frase = False

print(frase)