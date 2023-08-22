# method 1
def mutate_string(s, pos, c):
    d = list(s)
    d[pos] = c
    return "".join(d)


# method 2
def mutate_string(s, pos, c):
    return s[:pos] + c + s[pos + 1 :]
