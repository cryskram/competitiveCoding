n, m = map(int, input().split())
arr = set([int(i) for i in input().split(" ")])
a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]

score = 0

for x in arr:
    if x in a:
        score += 1
    elif x in b:
        score += -1
    else:
        score += 0

print(score)
