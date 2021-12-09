comprimento = float(input())
largura = float(input())
numero_de_gavetas = int(input())
tipo_de_madeira = input()

area = largura * comprimento
mesa = 200
metro_q = area*100

if area > 2:
    valor = metro_q + 50

elif area < 2:
    valor = metro_q

if tipo_de_madeira == "mogno":
    valor += 150

elif tipo_de_madeira == "carvalho":
    valor += 125

elif tipo_de_madeira == "pinus":
    valor += 50

custo_gaveta = 30 * numero_de_gavetas

valor_total = custo_gaveta + valor

print(valor_total)

