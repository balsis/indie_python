def count_unique_words(filename):
    with open(filename, encoding="utf-8") as file:
        uniq = []
        words = file.read().strip().split()
        for word in words:
            if word.lower() not in uniq:
                uniq.append(word.lower())
    return len(uniq)


print(count_unique_words("test2.txt"))