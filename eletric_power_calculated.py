energia = int(input())

if energia <= 30:
    valor = energia*0.09556

elif 30<energia<=100:
    valor = (energia - 30) * 0.16698 + 2.8668

elif  100< energia <=200:
    valor = (energia - 100) * 0.25052 + 2.8668 + 11.6886

elif energia >200:
    valor = (energia - 200) * 0.27836 + 2.8668  + 11.6886  + 25.052

print(f"{valor :.2f}")