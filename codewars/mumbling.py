# def accum(s: str) -> str:
#     d = ""
#     for i in range(len(s)):
#         d = d + s[i].upper() + (s[i].lower() * i) + "-"

#     return d[:-1]


# def accum(s: str) -> str:
#     d = ""
#     for idx, char in enumerate(s):
#         d = d + char.upper() + char * idx + "-"

#     return d


def accum(s: str) -> str:
    return "-".join(char.upper() + char * idx for idx, char in enumerate(s))


print(accum("RqaEzty"))
