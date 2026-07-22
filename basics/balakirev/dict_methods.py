things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

sorted_things = sorted(things.items(), key=lambda x: x[1], reverse=True)

n = int(input()) * 1000

lst = []
for i in sorted_things.copy():
    weight, thing = i[1], i[0]
    if weight <= n:
        lst.append(thing)
    else:
        continue
    n -= weight

print(*lst)

