def make_negative(num: int) -> int:
    if num <= 0:
        return num
    else:
        return int("-" + str(num))
