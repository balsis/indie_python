s = "Python is the best language!"


def repl(char):
    if char in ('b', 'i', 't', 'B', 'I', 'T'):
        return "#"
    else:
        return char

new_s = "".join(map(repl, s))
print(new_s)