import random

ls = []
for i in range(10):
    ls.append(random.randint(0, 10))
print(ls)

lsmin = ls[0]
for ele in ls:
    if ele <= lsmin:
        lsmin = ele

print(lsmin, ls.index(lsmin))
