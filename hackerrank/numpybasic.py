# without numpy

# if __name__ == "__main__":
#     n = list(map(int, input().split()))

#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     print(a + b)
#     print(a - b) # causes the error
#     print(a * b)
#     print(a // b)
#     print(a**b)

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))
