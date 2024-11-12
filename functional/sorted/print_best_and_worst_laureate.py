def print_best_and_worst_laureate(dct):
    counter = {}
    for k, v in dct.items():
        if v not in counter:
            counter[v] = 1
        else:
            counter[v] += 1
    sorted_counter = sorted(counter.items(), key = lambda x: x[1])


    last_element = len(sorted_counter)-1
    print(*sorted_counter[last_element], sep = ", ")
    print(*sorted_counter[0], sep = ", ")

laureates = {'За лучший фильм': 'Оппенгеймер',
             'За лучшую музыку к фильму': 'Оппенгеймер',
             'За лучший звук': 'Зона интересов',
             'За лучшие визуальные эффекты': 'Бедные-несчастные',
             'За лучший дизайн костюмов': 'Бедные-несчастные',
             'За лучшую операторскую работу': 'Бедные-несчастные',
             'За лучший монтаж': 'Оппенгеймер',
             'За лучший оригинальный сценарий': 'Оппенгеймер',
             'За лучший фильм на иностранном языке': 'Зона интересов'}

print_best_and_worst_laureate(laureates)
