vec = [2,5,1,9,3,7]
val=0
for idx, x in enumerate(vec):
    if val < x:
        val = vec[idx]

print (val)

