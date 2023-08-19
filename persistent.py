def persistence(n):
    if n < 10:
        return 0

    count = 0
    while n >= 10:
        pro = 1
        while n > 0:
            pro *= n % 10
            n //= 10
        n = pro
        count = count + 1

    return count


print(persistence(10))
