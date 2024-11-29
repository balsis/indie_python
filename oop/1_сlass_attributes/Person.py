class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True

attributes_to_check = input().split()
for i in attributes_to_check:
    print(i, '-YES', sep='') if hasattr(Person, i.lower()) else print(i, '-NO', sep='')