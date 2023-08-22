def get_sum(a, b):
    sum = 0
    big = 0
    small = 0
    if a > b:
        big = a
        small == b
    elif a < b:
        big = b
        small = a

    for i in range(small, big + 1):
        sum += i

    return sum


print(get_sum(-10, -2))
