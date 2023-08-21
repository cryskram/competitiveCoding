def count_sheep(sheep: list) -> int:
    return sum(x for x in sheep if x == True)
