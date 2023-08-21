def josephus_survivor(n: int, k: int):
    dum = [x for x in range(1, n + 1)]
    s = []
    idx = 0
    while len(dum) > 0:
        idx = (idx + k - 1) % len(dum)
        s.append(dum.pop(idx))
    return s[-1]


print(josephus_survivor(7, 3))
