def create_info(employees, identifiers):
    employees = sorted(employees)
    identifiers = sorted(identifiers)
    return dict(zip(identifiers,employees))


names = [
    'Pankratiy', 'Lidochka', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

ids = [77, 4, 20, 37, 32, 96]
print(create_info(names, ids))