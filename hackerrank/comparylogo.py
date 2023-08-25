def makelogo(s: str):
    mydict = dict.fromkeys(set(s), 0)

    for i in s:
        mydict[i] = s.count(i)

    newDict = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
    for x in newDict[:3]:
        print("{} {}".format(x[0], x[1]))


if __name__ == "__main__":
    s = input()
    makelogo(s)
