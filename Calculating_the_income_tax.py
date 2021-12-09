salario_bruto = float(input())
numero_de_dependentes = int(input())

desconto_por_dependente = numero_de_dependentes * 137.99

if salario_bruto <= 720:
    inss = salario_bruto * 0.0765
elif salario_bruto <= 1200:
    inss = salario_bruto * 0.09
elif salario_bruto <= 2400:
    inss = salario_bruto * 0.11
else:
    inss = 2400 * 0.11

if salario_bruto < 1372.83:
    aliquota = 0
    deducao = 0
if salario_bruto >= 1372.83 <=2743.25:
    aliquota = 0.15
    deducao = 205.92
if salario_bruto > 2743.25:
    aliquota = 0.275
    deducao = 548.83

print((salario_bruto - desconto_por_dependente - inss)*aliquota - deducao)