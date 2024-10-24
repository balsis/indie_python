def is_strings_equal(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


print(is_strings_equal("leto", "etol"))
print(is_strings_equal("qwerty", "rtyewq"))
print(is_strings_equal("aabc", "bcab"))
