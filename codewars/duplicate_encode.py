def duplicate_encode(s: str) -> str:
    d = ""
    s = s.lower()
    for i in s:
        if s.count(i) > 1:
            d += ")"
        else:
            d += "("

    return d


print(duplicate_encode("(( @"))
