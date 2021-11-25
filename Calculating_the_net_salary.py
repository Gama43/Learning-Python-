import math

import math

horas_regulares = int(input())
horas_extras = int(input())

valor_hora = 12.5

salario_bruto = (valor_hora * horas_regulares) + ((valor_hora + 2.5) * horas_extras)

ir = (13/100) * salario_bruto
inss = (9/100) * salario_bruto
salario_liquido = salario_bruto - ir - inss

print('- Salário Bruto : R$ {:.2f}'.format(salario_bruto))
print('- IR (13%) : R$ {:.2f}'.format(ir))
print('- INSS (9%) : R$ {:.2f}'.format(inss)) 
print('- Salário Líquido : R$ {:.2f}'.format(salario_liquido))