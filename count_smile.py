def count_smileys(arr: list) -> int:
    count = 0
    for i in arr:
        if i[0] == ":" or i[0] == ";":
            if len(i) == 2:
                if i[1] == ")" or i[1] == "D":
                    count += 1
            if len(i) == 3:
                if i[1] == "-" or i[1] == "~":
                    if i[2] == ")" or i[2] == "D":
                        count += 1

    return count


print(count_smileys([";D", ":-(", ":-)", ";~)"]))
