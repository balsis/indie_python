def words_length(temp: list) -> list:
    for i in temp[:]:
        temp.append(len(i))
        temp.remove(i)
    return temp

words = ['Hello', 'world!']
# words_length(words)
# print(words)
print(words_length(words))

