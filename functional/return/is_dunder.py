def is_dunder(string: str) -> bool:
    cleaned_string = string.replace("_", "")
    return (string.count('_') == 4 and
            cleaned_string.isalpha() and
            len(cleaned_string) > 2)

print(is_dunder('__str__'))
print(is_dunder('__s__'))
print(is_dunder('__abvc3__'))
print(is_dunder('__123__'))
