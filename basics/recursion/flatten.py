# пока нерабочее решение
def flatten(a: list) -> list:
    if a == []:
        return []
    if len(a) == 1:
        return a[0]
    if type(a[0]) == int:
        return a[:1] + flatten(a[1:])
    if type(a[0]) == list:
        return flatten(a[0]) + flatten(a[1:])

print(flatten([1, [2, 3, [4]], 5]))
