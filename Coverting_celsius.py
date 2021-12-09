origem = input()
valor_entrada = float(input())
destino = input()

valor_celsius = float()
resutado = float()


if origem =="f":
    valor_celsius = (valor_entrada - 32)/1.8
    
elif origem == "k":
    valor_celsius = valor_entrada - 273.15
elif origem == "r":
    valor_celsius = (valor_entrada - 491.67) * (5/9)
elif origem == "c":
    valor_celsius = valor_entrada

if destino == "c":
    resultado = valor_celsius

elif destino == "f":
    resultado = (valor_celsius *1.8) +32

elif destino =="k":
    resultado = valor_celsius + 273.15

elif destino == "r":
    resultado = (valor_celsius +273.15) * (9/5)

print(resultado)
