if __name__ == "__main__":
    n = int(input())
    t = tuple(map(int, input().split()))
    hashval = hash(t)
    print(hashval)
