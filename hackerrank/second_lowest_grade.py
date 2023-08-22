if __name__ == "__main__":
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])

    scores = []
    for x in data:
        scores.append(x[1])

    scores.sort()
    lowest = scores[0]
    sLowest = 0
    for x in scores:
        if x != lowest:
            sLowest = x
            break
        else:
            continue

    names = []
    for x in data:
        if sLowest in x:
            names.append(x[0])
        else:
            continue

    names.sort()
    for name in names:
        print(name)

    # print(names)
