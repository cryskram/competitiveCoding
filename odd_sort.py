def sort_array(source_array: list) -> list:
    oddList = []
    for i in source_array:
        if i % 2 != 0:
            oddList.append(i)
    oddList.sort()

    oddIdx = 0
    final = []

    for i in source_array:
        if i % 2 != 0:
            final.append(oddList[oddIdx])
            oddIdx += 1
        else:
            final.append(i)

    return final


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
