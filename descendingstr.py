def descending_order(num: int) -> int:
    # Convert the number to a list of its digits
    digits = [int(digit) for digit in str(num)]

    # Sort the digits in descending order
    sorted_digits = sorted(digits, reverse=True)

    # Convert the sorted digits list back to an integer
    result = int("".join(map(str, sorted_digits)))

    return result


print(descending_order(42145))
