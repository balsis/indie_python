dict = {'Дили' : set(), 'Вили' : set(), 'Били' : set()}

while True:
    inp = input()
    if inp == "конец":
        break
    name, commentator = inp.split(": ")

    dict[name].add(commentator)
print(dict)

for i, j in sorted(dict.items(), key= lambda x: -(len(x[1]))):
    print(f'Количество уникальных комментаторов у {i} - {len(j)}')