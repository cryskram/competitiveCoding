# def alphanumeric(password: str) -> bool:
#     dum = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
#     if len(password) > 0:
#         if " " not in password and "_" not in password:
#             for i in password:
#                 if i in dum:
#                     return True

#     return False

import re


def alphanumeric(input_string):
    # Define a regular expression pattern to match alphanumeric strings
    pattern = r"^[a-zA-Z0-9]+$"

    # Use the re.match() function to check if the input matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False


print(alphanumeric("PassW0rd"))
