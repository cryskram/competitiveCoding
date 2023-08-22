def count_substring(string: str, sub: str) -> int:
    return string.count(sub)


if __name__ == "__main__":
    original_string = input()
    substring = input()

    count = original_string.count(substring)

    print(count)
