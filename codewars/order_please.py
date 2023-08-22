def order(sentence):
    words = sentence.split()
    return " ".join(
        sorted(words, key=lambda word: next(char for char in word if char.isdigit()))
    )


print(order("is2 Thi1s T4est 3a"))
