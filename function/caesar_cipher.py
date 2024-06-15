def shift_letter(letter : str, shift: int):
    'Функция сдвигает символ letter на shift позиций'
    ind = ord(letter)
    a =  ind + shift
    if shift > 26:
        shift %= 26
    while a > 122:
        a = a - 26
    if a < 97:
        a = a + 26
    return chr(a)

def caesar_cipher(text: str, shift2: int):
    'Шифр цезаря'
    result = ''
    for char in text:
        if char.isalpha():
            shift = shift2 % 26  # Учитываем только сдвиг по модулю 26
            result += shift_letter(char, shift)
        else:
            result += ' '
    return result

print(caesar_cipher('one more light', -33))