def info_kwargs(**kwargs):
    for i in sorted(kwargs.items()):
        print(*i, sep = " = ")


info_kwargs(first_name = "John", last_name = "Doe", age = 33)


def past(h, m, s):
    return 1000 * (s + m * 60 + h + 3600)
