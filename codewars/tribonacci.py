def tribonacci(signature: list, n: int):
    count = 0
    newList = []
    if n == 0:
        return newList
    elif n == 1:
        newList.append(signature[0])
        return newList
    else:
        while count < n:
            newList.append(signature[0])
            nth = signature[0] + signature[1] + signature[2]
            signature[0] = signature[1]
            signature[1] = signature[2]
            signature[2] = nth
            count += 1

        return newList


if __name__ == "__main__":
    print(tribonacci([1, 1, 1], 1))
