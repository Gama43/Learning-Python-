n_pessoas = int(input())
n_maria = 0

for i in range(n_pessoas):
    nomes = input()
    nomes = nomes.split()
    for i in nomes:
        if i == "Maria":
            n_maria += 1

print(n_maria)