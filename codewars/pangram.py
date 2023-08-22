def is_pangram(s: str) -> bool:
    dum1 = "qwertyuiopasdfghjklzxcvbnm"
    res = False
    for i in dum1:
        if i not in s.lower():
            return False

    return True


# def is_pangram(sentence):
#     alphabet = set("abcdefghijklmnopqrstuvwxyz")

#     # Convert the input sentence to lowercase and remove non-letter characters
#     clean_sentence = "".join(char.lower() for char in sentence if char.isalpha())

#     return set(clean_sentence) == alphabet


print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))
