def is_isogram(s: str) -> bool:
    s = s.lower()
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)

    return True


print(is_isogram("vagesh"))
