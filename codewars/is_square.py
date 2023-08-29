def is_square(n: int):
    if n < 0:
        return False
    return int(n**0.5) ** 2 == n


print(is_square(-1))
