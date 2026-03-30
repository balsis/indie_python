def longest_palindrome(filename: str):
    max_length, this_word = 0, None

    file = open(filename)
    text = file.read()
    for word in text.split():
        if word.lower() == word.lower()[::-1] and len(word) > max_length:
            this_word, max_length = word, len(word)

    return this_word


print(longest_palindrome('secret_code.txt'))
