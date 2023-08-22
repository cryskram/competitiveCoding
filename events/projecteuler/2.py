# sum of even terms in fibonacci series

cases = int(input())

for _ in range(cases):
    case = int(input())
    n1 = 0
    n2 = 1
    sum = n2
    even_sum = 0

    while sum <= case:
        n1, n2 = n2, sum
        sum = n1 + n2
        if sum % 2 == 0 and sum <= case:
            even_sum += sum

    print(even_sum)
