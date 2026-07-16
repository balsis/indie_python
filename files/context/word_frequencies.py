def word_frequencies(filename):
    with open(filename, encoding="utf-8") as file:
        dct = {}
        words = file.read().strip().split()
        for i in words:
            if i.upper() not in dct:
                dct[i.upper()] = 1
            else:
                dct[i.upper()] += 1
    return dct


print(word_frequencies("test1.txt"))