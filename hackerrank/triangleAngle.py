import math


def find_angle(a: int, b: int):
    theta = round(math.degrees(math.atan(a / b)))
    return str(theta) + chr(176)


if __name__ == "__main__":
    ab = input()
    bc = input()
    print(find_angle(int(ab), int(bc)))
