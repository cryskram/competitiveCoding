def spinWord(s: str) -> str:
    dum = s.split(" ")
    d = []
    for i in dum:
        if len(i) >= 5:
            j = i[::-1]
            d.append(j)
        else:
            d.append(i)

    res = " ".join(d)
    return res


print(spinWord("This is hello world"))
