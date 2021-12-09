valor_bruto = float(input())

if valor_bruto < 500:
    desconto = valor_bruto * 0.2
    print(f"{valor_bruto - desconto:.2f}")

elif 500 <= valor_bruto <1000:
    desconto= valor_bruto * 0.3
    print(f"{valor_bruto - desconto:.2f}")

elif valor_bruto >=1000:
    desconto = (valor_bruto - 1000) * 0.45 + 1000 * 0.3
    print(f"{valor_bruto - desconto:.2f}")