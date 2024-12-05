def find_different_indexes(str1, str2):
    different_indexes = []
    print(list(zip(str1, str2)))
    for index, (char1, char2) in enumerate(zip(str1, str2)):
        if char1 != char2:
            different_indexes.append(index)

    return different_indexes


print(find_different_indexes('abcd', 'artd'))
# print(find_different_indexes('abcd', 'abcd'))
