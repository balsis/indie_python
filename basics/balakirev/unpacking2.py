def merge_dicts(*dict_args, ignored_keys=None):
    d = {}
    for arg in dict_args:
        d.update(arg)
    if ignored_keys is not None or ignored_keys is []:
        for key in ignored_keys:
            d.pop(key)
    return d

d1 = {"id": 1, "title": "Белая ночь", "author": "Михаил Боярский"}
d2 = {"id": 2, "name": "Группа крови", "author": "Виктор Цой"}
d3 = {"id": 3, "track": "На заре", "author": "Альянс"}

songs = merge_dicts(d1, d2, d3, ignored_keys=('id',))

print(songs)