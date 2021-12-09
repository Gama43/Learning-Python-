nota1 = input()
nota2 = input()
nota3 = input()
nota4 = input()

if nota1 == "A":
    equivalente_n1 = 4
elif nota1 == "B":
    equivalente_n1 = 3
elif nota1 == "C":
    equivalente_n1 = 2
elif nota1 == "E":
    equivalente_n1 = 0

if nota2 == "A":
    equivalente_n2 = 4
elif nota2 == "B":
    equivalente_n2 = 3
elif nota2 == "C":
    equivalente_n2 = 2
elif nota2 == "E":
    equivalente_n2 = 0

if nota3 == "A":
    equivalente_n3 = 4
elif nota3 == "B":
    equivalente_n3 = 3
elif nota3 == "C":
    equivalente_n3 = 2
elif nota3 == "E":
    equivalente_n3 = 0

if nota4 == "A":
    equivalente_n4 = 4
elif nota4 == "B":
    equivalente_n4 = 3
elif nota4 == "C":
    equivalente_n4 = 2
elif nota4 == "E":
    equivalente_n4 = 0

media = (equivalente_n1 + equivalente_n2 + equivalente_n3 + equivalente_n4)/4

if (nota1 == "E"  or nota2 == "E" or nota3 == "E"or nota4 == "E") or media <3:
    estudante = False

else:
    estudante = True

print(estudante)