def filter_long_words(lst, number):
    return [i for i in lst if len(i) > number]


print(filter_long_words(['sister', 'arena', 'formal', 'arena', 'spill'], 5))
print(filter_long_words(['Python', 'stole', 'my', 'heart'], 4))
print(filter_long_words(['ex', 'care', 'room', 'law'], 3))
