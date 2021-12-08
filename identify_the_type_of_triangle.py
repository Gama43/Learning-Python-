a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("equilátero")
elif a == b or a == c or b == c:
    print("isósceles")
else:
    print("escaleno")


