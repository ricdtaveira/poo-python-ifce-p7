from random import randint

randomlist = list()

while True:
    randomlist.append(randint(1,60))
    randomset = set(randomlist)
    randomlist = list(randomset)
    randomlist.sort()

    if len(randomlist) == 6:
        break

print(randomlist)