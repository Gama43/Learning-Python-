n = int(input())

maior = media = tot_dentro = 0

for i in range(0, n):
    praia, distancia = input().split(';')
    distancia = int(distancia)

    if distancia > maior:
        maior = distancia 
        nome_maior = praia 

    if 15 <= distancia <= 20:
        tot_dentro += 1
    
    media += distancia

media = media / n

print(f"{nome_maior};{tot_dentro};{media:.1f}")

