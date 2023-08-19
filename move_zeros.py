def move_zeros(lst: list) -> list:
    newList = []
    for i in lst:
        if i != 0:
            newList.append(i)

    for i in range(len(lst) - len(newList)):
        newList.append(0)

    return newList


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
