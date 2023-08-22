import numpy as np

n = input().split()
np.set_printoptions(legacy="1.13")  # only for formating in hackerrank
a = np.array([float(x) for x in n])
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
