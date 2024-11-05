def concatenate(**kwargs):
    return "".join([str(i) for i in kwargs.values()])

print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
print(concatenate(first='i got ', second=5, third=" stars"))
print(concatenate(t='Happy', y="Meal", w="Cost", m=10, b='Buks'))
print(concatenate(q='iHave', w="next", e="Coins", r=[10, 5, 10, 7]))
