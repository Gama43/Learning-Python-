salario_atual = float(input())
salario_minimo = float(input())

qtd_minimo = salario_atual / salario_minimo

if(qtd_minimo<=3):
    salario_atual = salario_atual * 1.2
elif(qtd_minimo<=5):
    salario_atual = salario_atual * 1.15
else:
    salario_atual = salario_atual * 1.1

if(salario_atual<1.5*salario_minimo):
    salario_atual = 1.5 * salario_minimo
if(salario_atual>20*salario_minimo):
    salario_atual = 20 * salario_minimo

print(f"{salario_atual:.2f}")