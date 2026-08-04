


def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        lst1 = res[0]
        lst2 = res[1]

        dct = {lst1[i]: lst2[i] for i in range(len(lst2))}
        return dct

    return wrapper


@decorator
def my_func(str1: str, str2: str):
    return str1.split(), str2.split()


d = my_func("house river tree car", "дом река дерево машина")

print(*sorted(d.items()))
