# 15 121050

def nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

print(nod(15, 121050))