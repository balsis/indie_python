ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}

person = input()

age = ages.get(person)

if age:
    print(f'{person} is {age} years old.')
else:
    print(f"{person}'s age is unknown.")