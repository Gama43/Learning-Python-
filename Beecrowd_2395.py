import math

a, b, c = [int(w) for w in input().split()]

x, y, z = [int(w) for w in input().split()]

quantidade_maxima = (x//a)*(y//b)*(z//c)

print('{:.0F}'.format(quantidade_maxima))