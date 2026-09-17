import secrets
import string


def generate_password(len_password: int, digits: bool = True, special_chars: bool = True) -> str:
    letters = string.ascii_letters

    if digits:
        letters += string.digits

    if special_chars:
        letters += string.punctuation

    password = ""

    for i in range(len_password):
        password += secrets.choice(letters)

    return password