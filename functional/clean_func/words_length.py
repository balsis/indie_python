def words_length(words):
    for i in range(len(words)):
        words[i] = len(words[i])

words = ['Hello', 'world!']
words_length(words)
print(words)

