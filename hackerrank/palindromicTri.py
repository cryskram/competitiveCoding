def construct(n: int):
    for i in range(1, n + 1):
        for j in range(n):
            print(i, j)


if __name__ == "__main__":
    case = int(input())
    construct(case)
