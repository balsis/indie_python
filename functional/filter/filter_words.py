def filter_words(lst):
    return list(filter(lambda x: len(x) == 4 or x.startswith("S"), lst))


words = ['scheme', 'hypnothize', 'exposure', 'Syndrome',
         'Save', 'speculate', 'cane', 'welfare', 'blame', 'core']
print(filter_words(words))
