# def first_repeated_word(word: str):
#     'Находит первый дубль в строке'
#     words = word.split()
#     for i in words:
#         if words.count(i) > 1:
#             return i

def first_repeated_word(word: str):
    'Находит первый дубль в строке'
    words = word.split()
    lst = []
    for i in words:
        if i not in lst:
            lst.append(i)
        else:
            return i


print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc"))
print(first_repeated_word("ab ca bc ca ab bc"))