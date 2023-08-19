# partially working


def tower_builder(n_floors: int) -> list:
    newList = []
    spaces = " "
    stars = "*"
    dum = ""
    if n_floors == 1:
        newList.append(stars)
    if n_floors == 2:
        for i in range(n_floors - 1):
            dum = dum + spaces
        dum = dum + stars
        for i in range(n_floors - 1):
            dum += spaces

        newList.append(dum)
    if n_floors == 3:
        for j in range(n_floors - 1):
            for i in range(n_floors - 1):
                dum = dum + spaces
            dum = dum + stars
            for i in range(n_floors - 1):
                dum += spaces

            newList.append(dum)

    return newList


print(tower_builder(3))
