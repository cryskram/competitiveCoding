def algo(n):
    primes = []
    num = 2

    while len(primes) < n:
        prime = True
        for i in primes:
            if i * i > num:
                break
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(num)
        num += 1

    return primes


cases = int(input())
for _ in range(cases):
    case = int(input())
    print(algo(case))
