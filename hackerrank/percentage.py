if __name__ == "__main__":
    n = int(input())
    marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        marks[name] = scores
    query = input()

    req = marks.get(query)
    avg = sum(x for x in req) / len(req)

    print("{:.2f}".format(avg))
