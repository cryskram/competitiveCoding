n = int(input())
s = set(map(int, input().split()))
commands = [input().split() for _ in range(int(input()))]

for command in commands:
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))
