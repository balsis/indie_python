def is_palindrome(word: str):
    word = word.lower()
    if len(word) == 0 or len(word) ==1:
        return True
    if word[0] != word[len(word)-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

print(is_palindrome('abba'))
print(is_palindrome('Qwerty'))
print(is_palindrome('Racecar'))
