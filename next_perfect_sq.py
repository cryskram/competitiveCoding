import math


def is_perfect_square(number):
    # Calculate the square root
    square_root = math.isqrt(number)

    # Check if the square of the square root is equal to the original number
    return square_root * square_root == number


def find_next_square(sq):
    if not is_perfect_square(sq):
        return -1

    next_square = sq + 1
    while True:
        if is_perfect_square(next_square):
            return next_square
        next_square += 1


print(find_next_square(169))
