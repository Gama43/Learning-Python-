import math

a = int(input("digite o valor de a: "))
b = int(input("digite o valor de a: "))
c = int(input("digite o valor de a: "))

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print(x1, x2)