def rotate_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    if shift > 26:
        shift %= 26
    elif shift < -26:
        shift %= -26
    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = letters.index(letter) + shift
    if index > 26:
        index %= 26
    return letters[index]


def caesar_cipher(phrase: str, key: int) -> str:
    "Шифр Цезаря"
    return "".join([rotate_letter(i, key) if i.isalpha() else i for i in phrase])


print(caesar_cipher('lost in the echo', 1))
print(caesar_cipher('lost in the echo', -120))
