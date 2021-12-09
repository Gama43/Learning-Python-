salario = float(input())

if salario <= 720:
    inss = salario * 0.0765
elif salario <= 1200:        # Se chegou aqui é porque decididamente salario > 720
    inss = salario * 0.09
elif salario <= 2400:        # Se chegou aqui é porque decididamente salario > 1200
    inss = salario * 0.11
else:                        # Se chegou aqui é porque decididamente salario > 2400
    inss = 2400 * 0.11
print(inss)