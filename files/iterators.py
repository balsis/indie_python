def get_unique_words(filename):
    DEL_CHARS = '!"#$%&\'()*+,-./:;<=>’?@[\\]^_`{|}~—'
    file = open(filename)
    trans_table = str.maketrans('', '', DEL_CHARS)
    print(trans_table)
    unique_words = set()
    for line in file:
        new = line.strip()
        lst = [letter for letter in new if letter not in DEL_CHARS]
        f = "".join(lst).lower().split()
        for i in f:
            unique_words.add(i)
    unique_words2 = sorted(list(unique_words))
    file.close()
    return unique_words2


print(get_unique_words("quotes.txt"))
