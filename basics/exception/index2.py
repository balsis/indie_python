words = ["Python", "мы любим", "тебя"]

for index in range(7):
    try:
        print(index, words[index])
    except IndexError:
        print(f"Индекс {index} вышел за границы списка")
print('Знай это')



