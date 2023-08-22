# not working


def duplicate_encode(word: str) -> str:
    count = 0
    dum = ""
    for i in word:
        for j in word:
            if i == j:
                count += 1
        if count > 2:
            i = i.replace(i, ")")
        else:
            i = i.replace(i, "(")

        dum = dum + i

    return dum


print(duplicate_encode("Success"))
