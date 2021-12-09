n = float(input())

fracao = n - int(n)

if (fracao<0.25):
    n = n - fracao
elif(0.25<=fracao<0.50):
    n = n + (0.5 - fracao)
elif(0.5<fracao<0.75):
    n = n + (0.5 - fracao)
elif(fracao>=0.75):
    n = n + (1 - fracao)

print(n)