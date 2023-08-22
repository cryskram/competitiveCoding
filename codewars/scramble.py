def scramble(str1, str2):
    char_count = [0] * 26

    for char in str1:
        char_count[ord(char) - ord("a")] += 1

    for char in str2:
        char_index = ord(char) - ord("a")
        if char_count[char_index] <= 0:
            return False
        char_count[char_index] -= 1

    return True


print(scramble("cedewaraaossoqqyt", "codewars"))
