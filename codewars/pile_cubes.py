def find_nb(m):
    cur = 0
    n = 1

    while cur < m:
        cur = cur + n**3
        if cur == m:
            return n

        n = n + 1

    return -1


print(find_nb(1071225))
