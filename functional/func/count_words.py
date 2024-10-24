def count_words(phrase: str) -> int:
    return len(phrase.split())

print(count_words('I like learn python'))
print(count_words("Find definitions and references for functions and other symbols in this file by clicking a symbol below or in the code"))
print(count_words(' hello   bro  '))
