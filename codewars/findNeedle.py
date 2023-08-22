def findNeedle(arr: list) -> int:
    val = 0
    for i in range(len(arr)):
        if arr[i] == "needle":
            val = i

    return "found the needle at position {}".format(val)
