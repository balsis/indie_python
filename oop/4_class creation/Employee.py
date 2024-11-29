class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def display_person_info(self):
		print(f'Person: {self.name}, {self.age}')


class Company:
	def __init__(self, company_name, location):
		self.company_name = company_name
		self.location = location

	def display_company_info(self):
		print(f'Company: {self.company_name}, {self.location}')


class Employee:
	def __init__(self, name, age, company_name, location):
		self.personal_data = Person(name, age)
		self.work = Company(company_name, location)


# Ниже код для проверки классов Person, Company и Employee

ivan = Person('Ivan', 32)
assert ivan.name == 'Ivan'
assert ivan.age == 32
ivan.display_person_info()

zara = Company('Zara', 'Prague')
assert zara.company_name == 'Zara'
assert zara.location == 'Prague'
zara.display_company_info()

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
assert isinstance(emp.personal_data, Person)
assert isinstance(emp.work, Company)

assert emp.personal_data.name == 'Jessica'
assert emp.personal_data.age == 28
emp.personal_data.display_person_info()

assert emp.work.company_name == 'Google'
assert emp.work.location == 'Atlanta'
emp.work.display_company_info()

emp2 = Employee('Kolya', 11, 'Facebook', 'Seattle')
assert isinstance(emp2.personal_data, Person)
assert isinstance(emp2.work, Company)

assert emp2.personal_data.name == 'Kolya'
assert emp2.personal_data.age == 11
emp2.personal_data.display_person_info()

assert emp2.work.company_name == 'Facebook'
assert emp2.work.location == 'Seattle'
emp2.work.display_company_info()
