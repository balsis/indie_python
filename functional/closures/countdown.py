def countdown(n):
    save_n = n
    def inner():
        nonlocal n
        if n <= 0:
            print(f"Превышен лимит, вы вызвали более {save_n} раз")
        else:
            print(n)
            n -= 1
            return n
    return inner

a = countdown(2)
b = countdown(2)
a()
b()
b()
b()
a()
a()
