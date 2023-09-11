def drop_cap(words: str) -> str:
    x = []
    for word in words.split(" "):
        if len(word) <= 2:
            x.append(word)
        else:
            x.append(word.title())

    return " ".join(x)


print(drop_cap("   space WALK   "))
