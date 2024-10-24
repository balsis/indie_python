def create_palindrome(phrase: str):
    phrase = phrase.lower()
    reversed_phrase = phrase[::-1]
    return phrase if phrase == reversed_phrase else f'{phrase}_i_{reversed_phrase}'

print(create_palindrome('Rotator'))
print(create_palindrome('Hello'))
