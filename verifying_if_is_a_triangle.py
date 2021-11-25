lado01 = float(input())
lado02 = float(input())
lado03 = float(input())


triangulo = abs(lado02 - lado03) < lado01 < lado02 + lado03 
print(triangulo)