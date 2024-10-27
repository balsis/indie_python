alpha = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(string: str) -> bool:
    return set(string.lower().replace(".", "").replace("!", "").replace(" ", '')) == set(alpha)


print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("How quickly daft jumping zebras vex!"))
