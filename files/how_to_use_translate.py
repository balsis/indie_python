import string

mapping = str.maketrans("", "", string.punctuation)
print(mapping)

stringa = "fdsfsdfsd, fdsfsd, asdf!%"

print(stringa.translate(mapping).replace(" ", ""))