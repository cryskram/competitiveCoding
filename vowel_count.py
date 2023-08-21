def get_count(s: str) -> int:
    vowels = "aeiou"
    val = 0
    for i in s:
        if i in vowels:
            val += 1

    return val
