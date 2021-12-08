nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 9.0:
    print("Ótimo")
elif 7.5 <= media < 9.0:
    print("Bom")
elif 6.0 <= media < 7.5:
    print("Satisfatório")
elif 0.0 <= media < 6.0:
    print("Insuficiente")
