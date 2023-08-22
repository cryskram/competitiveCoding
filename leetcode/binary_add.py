def addBinary(a: str, b: str) -> str:
    i = bin(int(a)) + bin(int(b))
    return str(i)


print(addBinary(11, 1))
