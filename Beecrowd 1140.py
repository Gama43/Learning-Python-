for i in range(5):
    frase = input()
    frase_minuscula = frase.lower()
    palavras = frase_minuscula.split()
    for palavra in palavras:
        if palavra[0] != frase [0]:
            print('N')
            break
        else:
            print('Y')