def get_letters(stroka:str):
    return list(map(lambda x: (str.upper(x), str.lower(x)), stroka))

print(get_letters('TykPe'))
