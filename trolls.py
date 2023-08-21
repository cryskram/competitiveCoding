def disemvowel(string: str) -> str:
    dum = "aeiouAEIOU"
    dum1 = ""

    for i in string:
        if i in dum:
            i = i.replace(i, "")
        else:
            dum1 += i

    return dum1


print(disemvowel("This is COol"))
