if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    newList = list(arr)

    newList.sort()
    newList.reverse()
    firstCount = newList.count(newList[0])
    runnerup = 0
    for i in newList:
        if i != newList[0]:
            runnerup = i
            break
        else:
            continue

    print(runnerup)
