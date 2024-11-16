def make_repeater(n):

    def inner(phrase):
        return phrase*n

    return inner


repeat_5 = make_repeater(5)
print(repeat_5('Hello'))
print(repeat_5('World'))

repeat_2 = make_repeater(2)
print(repeat_2('Pizza'))
print(repeat_2('Pasta'))