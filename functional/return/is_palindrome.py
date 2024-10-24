def is_palindrome(phrase: str) -> bool:
    phrase = phrase.lower().replace(" ", '')
    reversed_phrase = phrase[::-1]
    return phrase == reversed_phrase


assert is_palindrome("Never Odd or Even") == True
assert is_palindrome("abc") == False
assert is_palindrome("kayak") == True
assert is_palindrome("KayAk") == True
