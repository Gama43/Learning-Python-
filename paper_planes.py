num_competidores, qtd_total_folhas, qtd_folhas_competidor = [int(w) for w in input().split()]

if num_competidores * qtd_folhas_competidor <= qtd_total_folhas:
    folhas = True
    if folhas == True:
        print("S")
else:
    folhas = False
    if folhas == False:
        print("N")