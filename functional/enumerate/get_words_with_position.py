def get_words_with_position(words: str):
    return [(word, index) for index, word in enumerate(words.split(), start = 1)]


get_words_with_position('variation random electronics competence collapse')
print(get_words_with_position('Куда ты тянешь свои ручки'))
