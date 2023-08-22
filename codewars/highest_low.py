def high_and_low(numbers: str):
    data = [x for x in numbers if x != " "]
    intData = [int(i) for i in data]
    return f"{intData[-1]} {intData[0]}"


print(high_and_low("1 2 3 4 5"))
