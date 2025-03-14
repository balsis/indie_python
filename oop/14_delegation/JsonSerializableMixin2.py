import json


class JsonSerializableMixin:
    def to_json(self):
        temp = self.to_dict()
        return json.dumps(temp)

    def to_dict(self):
        extra = json.dumps(self, default = lambda x: x.__dict__)
        return json.loads(extra)



# Ниже код для проверки миксина JsonSerializableMixin

class Person(JsonSerializableMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(JsonSerializableMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(JsonSerializableMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_json() == '{"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}'

walter = Person("Walter White", 30, address)
walter.hobby = ['Chemistry', 'Cooking']
walter.is_danger = True

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
walter.company = Company("SCHOOL", company_address)
assert walter.to_json() == '{"name": "Walter White", "age": 30, "address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, "company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}}'

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
walter.is_lucky = False

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_json() == '{"name": "Gustavo Fring", "age": 55, "address": {"street": "Los Pollos Hermanos", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}, "friends": [{"name": "Walter White", "age": 30, "address": {"street": "123 Main St", "city": "Albuquerque", "state": "NM", "zip_code": "987654"}, "hobby": ["Chemistry", "Cooking"], "is_danger": true, "company": {"name": "SCHOOL", "address": {"street": "3828 Piermont Dr", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}, "is_lucky": false}, {"name": "Jesse Bruce Pinkman", "age": 27, "address": {"street": "456 Oak St", "city": "Albuquerque", "state": "NM", "zip_code": "12345"}}]}'
print('Good')