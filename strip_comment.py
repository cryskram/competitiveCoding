def strip_comments(s: str, markers: list) -> str:
    dum = [x for x in s.split("\n")]
    s1 = ""
    for i in dum:
        for j in i:
            if j in markers and j != s[0]:
                break
            else:
                s1 += j
        s1 = s1.strip() + "\n"

    val = s1.rstrip("\n")
    return val


print(strip_comments(" a #b\nc\nd $e f g", ["#", "$"]))
