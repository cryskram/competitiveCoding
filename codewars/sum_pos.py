def positive_sum(arr: list) -> int:
    return sum([x for x in arr if x > 0])


print(positive_sum([1, -4, 7, 12]))
