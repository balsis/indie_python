DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
}

def alphabet():
    for k, v in DICTIONARY.items():
        yield k,v


g = alphabet()
letter, word = next(g)
print(letter, word)
print(next(g))
print(next(g))
