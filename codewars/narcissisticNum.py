def narcissistic(value: int) -> bool:
    n = value
    sum = 0
    s = len(str(value))
    while value > 0:
        sum += (value % 10) ** s
        value //= 10

    return n == sum


print(narcissistic(1938))
