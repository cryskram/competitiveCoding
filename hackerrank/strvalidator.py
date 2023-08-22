if __name__ == "__main__":
    s = input()
    r = False

    for i in range(len(s)):
        if s[i].isalnum():
            r = True
            break
        else:
            r = False
    print(r)

    for i in range(len(s)):
        if s[i].isalpha():
            r = True
            break
        else:
            r = False

    print(r)

    for i in range(len(s)):
        if s[i].isdigit():
            r = True
            break
        else:
            r = False

    print(r)

    for i in range(len(s)):
        if s[i].islower():
            r = True
            break
        else:
            r = False

    print(r)

    for i in range(len(s)):
        if s[i].isupper():
            r = True
            break
        else:
            r = False

    print(r)
