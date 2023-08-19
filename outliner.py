def find_outlier(integers: list) -> int:
    evenCount, oddCount = 0, 0
    for i in integers:
        if i % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    if evenCount > oddCount:
        # find the odd one
        for i in integers:
            if i % 2 != 0:
                return i

    else:
        # find even
        for i in integers:
            if i % 2 == 0:
                return i


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
