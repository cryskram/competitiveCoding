def solve(s: str):
    dum = s.split(" ")
    new = [i.capitalize() for i in dum]

    return " ".join(new)


print(solve("132 456 Wq  m e"))
#    len("132 456 Wq  m e") == len(solve("132 456 Wq  m e")))
