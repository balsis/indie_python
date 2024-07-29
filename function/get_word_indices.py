
def get_word_indices(my_list: list):
    dct = {}
    for i, value in enumerate(my_list):
        for j, string in enumerate(value.lower().split()):
            if string not in dct:
                dct[string] = []
            dct[string].append(i)
    return dct

print(get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']))

print(get_word_indices(['Look at my horse',
                         'my horse',
                         'is amazing']))

print(get_word_indices([]))