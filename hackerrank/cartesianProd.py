# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# res = [(x, y) for x in a for y in b]
# res.sort()
# dum = ""
# for i in res:
#     dum += str(i) + " "

# print(dum)


# using itertools
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = list(product(a, b))
res.sort()
dum = ["".join(str(i)) for i in res]

print("\n".join(dum))
