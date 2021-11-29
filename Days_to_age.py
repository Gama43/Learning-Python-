n = int(input())

ano = n // 365
n = n - ano * 365

mes = n // 30
n = n - mes*30

dia = n

print('''{:.0f} ano(s)
{:.0f} mes(ses)
{:.0f} dia(s)'''.format(ano, mes, dia))