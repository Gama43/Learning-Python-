lista = []

for i in range(4):
    n = int(input())
    lista.append(n)
   
    lista_unica = list(set(lista))

print(len(lista_unica))