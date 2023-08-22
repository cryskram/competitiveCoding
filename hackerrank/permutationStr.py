from itertools import permutations

n = input().split()

res = list(permutations(n[0], int(n[1])))
res.sort()
dum = ["".join(x).upper() for x in res]

print("\n".join(dum))
