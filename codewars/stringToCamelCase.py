def to_camel_case(text: str) -> str:
    d = text.replace("-", " ").replace("_", " ").split()
    dum = []
    for i in range(len(d)):
        if i > 0:
            dum.append(d[i].capitalize())
        else:
            dum.append(d[i])

    return "".join(dum)


print(to_camel_case("the-warrior"))
