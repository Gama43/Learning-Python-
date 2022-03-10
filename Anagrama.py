def vereficar_anagrama(palavra1, palavra2):
    if palavra1 == palavra2:
        anagrama = False
    else:
        if(sorted(palavra1) == sorted(palavra2)):
            anagrama = True
        else:
            anagrama = False
    
    print(anagrama)

palavra1 = str(input())
palavra2 = str(input())

vereficar_anagrama(palavra1, palavra2)

