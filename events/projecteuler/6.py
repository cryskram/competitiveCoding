cases = int(input())

for _ in range(cases):
    case = int(input())
    sumsq = sum(i**2 for i in range(1, case + 1))
    sqsum = sum(i for i in range(1, case + 1)) ** 2

    print(sqsum - sumsq)
