if __name__ == "__main__":
    commands = [input().split() for _ in range(int(input()))]

    dum = []

    for command in commands:
        if command[0] == "insert":
            dum.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(dum)
        elif command[0] == "remove":
            dum.remove(int(command[1]))
        elif command[0] == "append":
            dum.append(int(command[1]))
        elif command[0] == "sort":
            dum.sort()
        elif command[0] == "pop":
            dum.pop()
        elif command[0] == "reverse":
            dum.reverse()
