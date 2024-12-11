def speller(word):
    if len(word) > 0:
        speller(word[1:])
        print(word[0], end = '\n')


speller('Artem')
