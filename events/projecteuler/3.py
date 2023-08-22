cases = int(input())

for _ in range(cases):
    case = int(input())

    i = 2
    while i * i <= case:
        if case % i:
            i += 1
        else:
            case //= i

    print(case)
