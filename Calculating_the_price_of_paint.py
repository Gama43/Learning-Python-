metros = float(input())
galoes = round(max(1, metros/64.8))
valor = galoes*25
valor = int(valor)
metros = int(metros)
print('- área de cobertura: {}'.format(metros), '\n- número de galões: {}'.format(galoes), '\n- valor a ser pago: R$ {:.2f}'.format(valor))