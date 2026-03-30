def count_word_in_file(filename: str, phrase: str):
    file = open(filename)
    text = file.read().lower()
    count = text.count(phrase)
    file.close()
    return count