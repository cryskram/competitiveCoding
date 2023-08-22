# return masked string
def maskify(cc: str) -> str:
    if len(cc) == 0:
        return ""
    elif len(cc) == 1 or len(cc) == 2 or len(cc) == 3 or len(cc) == 4:
        return cc
    else:
        dummy = ""
        for i in range(len(cc[:-4])):
            dummy += "#"
        return dummy + cc[-4:]


if __name__ == "__main__":
    print(maskify("skippy"))
