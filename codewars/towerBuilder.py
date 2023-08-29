def tower_builder(n_floors: int):
    d = []
    count = 1
    while n_floors > 0:
        d.append(" " * (n_floors - 1) + "*" * count + " " * (n_floors - 1))
        n_floors -= 1
        count += 2

    return d


print(tower_builder(3))
