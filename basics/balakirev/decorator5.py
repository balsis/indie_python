t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        while "--" in res:
            res = res.replace("---", "-").replace("--", "-")
        return res

    return wrapper


@decorator
def transformation(n, sep="-"):
    new_str = ""
    for char in n:
        if char in t:
            new_str += t[char]
        elif char in ": ;.,_":
            new_str += "-"
        elif char == " ":
            new_str += sep
        else:
            new_str += char
    return new_str


s = input().lower()

print(transformation(s))
