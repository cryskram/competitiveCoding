def josephus(items: list, k: int) -> list:
    dum = []
    idx = 0
    while len(items) > 0:
        idx = (idx + k - 1) % len(items)
        dum.append(items.pop(idx))
    return dum


print(josephus([1, 2, 3, 4, 5, 6, 7], 3))
