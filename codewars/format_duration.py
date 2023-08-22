import datetime


def format_duration(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365

    # return f"{years} years, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds"
    return str(datetime.timedelta(seconds=seconds))


print(format_duration(37564662327))
