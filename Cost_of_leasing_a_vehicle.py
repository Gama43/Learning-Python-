dias = int(input())
km_rodado = float(input())

valor = 45*dias

if km_rodado > 60*dias:
    valor += (km_rodado-60*dias)*0.5

print(valor)