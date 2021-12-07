x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

pode_moverse = False

if abs(x1-x2) == 2 and abs(y1-y2) == 1:
    pode_moverse = True
elif abs(x1-x2) == 1 and abs(y1-y2) == 2:
    pode_moverse = True

print(pode_moverse)

