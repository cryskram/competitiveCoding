def print_formatted(number):
    l = len(bin(number)[2:])
    for i in range(1, number + 1):
        d = str(i).rjust(l)
        o = oct(i)[2:].rjust(l)
        h = hex(i)[2:].rjust(l)
        b = bin(i)[2:].rjust(l)
        print(d, o, h.upper(), b)


if __name__ == "__main__":
    n = int(input())
    print(print_formatted(n))
