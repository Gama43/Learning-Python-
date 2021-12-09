aniversario1 = int(input())
aniversario2 = int(input())
aniversario3 = int(input())

if aniversario1 != aniversario2 and aniversario1!=aniversario3 and  aniversario2 != aniversario3:
    festas = 3

elif aniversario1 == aniversario2 and aniversario1 == aniversario3:
    festas = 1

elif aniversario1 == aniversario2 or aniversario1 == aniversario3 or aniversario2 == aniversario3:
    festas = 2

print(festas)