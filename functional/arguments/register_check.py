def register_check(people: dict) -> int:
    return list(people.values()).count("yes")


people = {'Igor': 'yes', 'Stas': 'no', 'Peter': 'no', 'Mary': 'yes'}
print(register_check(people))
people = {'Igor': 'no', 'Vasya': 'no', 'Peter': 'no', 'Mary': 'no'}
print(register_check(people))
people = {'Igor': 'yes', 'Vasya': 'yes', 'Peter': 'yes',
          'Mary': 'no', 'Alex': 'yes', 'Marina': 'yes'}
print(register_check(people))
