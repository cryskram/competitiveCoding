def duplicate_count(text: str):
    count = 0
    text = text.lower()
    for i in set(text):
        if text.count(i) > 1:
            count += 1

    return count


print(duplicate_count("indivisibilities"))
