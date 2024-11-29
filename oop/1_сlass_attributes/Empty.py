class Empty:
    pass


my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]

for item in my_list:
    setattr(Empty, item[0], item[1])

print(Empty.__dict__)