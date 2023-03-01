import re


def check_password_for_valid(password):
    length_patter = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password")

    if not re.fullmatch(length_patter, password):
        return (False, "Password must have at least 8 symbols")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least lowercase letter")

    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least uppercase letter")

    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least 1 number")

    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least 1 special symbol like this: @%#!&*^ ")

    return (True, "Password is valid")


while True:
    password = input("Please enter password: ")
    password_chech_res = check_password_for_valid(password)
    if check_password_for_valid[0]:
        print(check_password_for_valid[1])
        break
    print(check_password_for_valid[1])
