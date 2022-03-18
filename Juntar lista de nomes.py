lista = []
tam1 = int(input())

for i in range(tam1):
    nomes = input()
    lista.append(nomes)

lista2 = []
tam2 = int(input())

for i in range(tam2):
    nomes = input()
    lista2.append(nomes)

lista_unida = lista + lista2
lista_organizada = sorted(lista_unida)

[print(nomes) for nomes in lista_organizada]

