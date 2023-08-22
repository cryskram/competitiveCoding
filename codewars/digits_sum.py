def digital_root(n: int) -> int:
    sum = 0
    while n > 0:
        dig = n % 10
        sum += dig
        n //= 10

    val = sum
    if val > 9:
        val = digital_root(val)

    return val


print(digital_root(2215))
