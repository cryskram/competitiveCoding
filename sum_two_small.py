def sum_two_smallest_numbers(numbers):
    newList = sorted(numbers)
    return newList[0] + newList[1]


if __name__ == "__main__":
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
