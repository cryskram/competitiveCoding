# power digit sum

cases = int(input())

for _ in range(cases):
    case = int(input())
    val = 2**case
    sum = 0

    while val > 0:
        sum += val % 10
        val //= 10

    print(sum)
