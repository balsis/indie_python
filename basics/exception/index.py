words = ["Python", "мы любим", "тебя"]
try:
    for index in range(5):
        print(index, words[index])
except IndexError:
    print(f"Индекс {index} вышел за границы списка")
print('Знай это')