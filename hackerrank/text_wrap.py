def wrap(string: str, width: int):
    dum = []
    s = ""
    for i in string:
        if len(s) == width:
            dum.append(s)
            s = i
        else:
            s += i

    dum.append(s)

    return "\n".join(dum)


print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))
