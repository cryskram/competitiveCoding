# not working


def to_jaden_case(string: str) -> str:
    dum = ""
    for i in range(len(string)):
        if string[i] == " ":
            j = string[i + 1].replace(string[i + 1], string[i + 1].upper())
            dum += string[i + 1] + j
        else:
            dum += string[i]
    return dum


print(to_jaden_case("This is cool"))
