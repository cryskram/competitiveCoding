def plusOne(digits: list[int]) -> list[int]:
    dum = ""
    for i in digits:
        dum += str(i)

    s = " ".join((str(int(dum) + 1))).split()

    return [int(x) for x in s]


print(plusOne([1, 2, 3]))
