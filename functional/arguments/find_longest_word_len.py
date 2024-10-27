def find_longest_word_len(lst):
    longest = ""
    for i in lst:
        if len(i) > len(longest):
            longest = i

    return len(longest)


print(find_longest_word_len(['hello', 'world', 'Python', 'reserve']))
print(find_longest_word_len(['default', 'ghostwriter', 'bother', 'applaud', 'skate', 'way']))
print(find_longest_word_len(['brain', 'candle', 'rare', 'shy']))
