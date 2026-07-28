import string

allowed = string.ascii_letters + string.digits + "_"

def is_valid_email(email: str):
    check = "@" in email and "." in email
    email = email.replace("@", "").replace(".", "")
    flag = True
    for char in email:
        if char not in allowed:
            flag = False
    print("ДА" if check and flag else "НЕТ")


n = input()

is_valid_email(n)

