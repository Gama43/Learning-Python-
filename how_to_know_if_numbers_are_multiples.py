a, b = [int(w) for w in input().split()]

if (b%a == 0) or (a%b ==0):
     multiplo =  True
     if multiplo == True:
         print("Sao Multiplos")
else:
    multiplo= False
    if multiplo == False:
        print("Nao sao Multiplos")
