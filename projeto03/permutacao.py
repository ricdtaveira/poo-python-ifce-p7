from itertools import permutations

caracteres = ["Joao", "Maria", "Ricardo", "Rebeca", "Celma"]
count=1
for subset in permutations(caracteres, 3):
    print(count, subset)
    count=count + 1