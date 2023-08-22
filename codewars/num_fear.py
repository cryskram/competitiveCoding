def am_i_afraid(day: str, num: int) -> bool:
    if day == "Monday" and num == 12:
        return True
    elif day == "Tuesday" and num > 95:
        return True
    elif day == "Wednesday" and num == 34:
        return True
    elif day == "Thursday" and num == 0:
        return True
    elif day == "Friday" and num % 2 == 0:
        return True
    elif day == "Saturday" and num == 56:
        return True
    elif day == "Sunday" and (num == 666 or num == -666):
        return True
    else:
        return False


print(am_i_afraid("Monday", 12))
