def number(bus_stops: list[list]) -> int:
    val = 0
    diff = 0
    for i in bus_stops:
        val = i[0] - i[1]
        diff += val

    return diff


print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]))
