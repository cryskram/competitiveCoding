# incomplete


def dirReduc(arr: list) -> list:
    newList = []
    for i in arr:
        i = i.upper()
        newList.append(i)

    for i in newList:
        for j in newList:
            # todo
            pass

    return newList


print(dirReduc(["NORTH", "SOUTH", "south", "east", "west", "north", "west"]))
