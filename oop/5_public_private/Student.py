class Student:
	def __init__(self, name, age, branch):
		self.__name = name
		self.__age = age
		self.__branch = branch

	def __display_details(self):
		print(f'Имя: {self.__name}\n'
		      f'Возраст: {self.__age}\n'
		      f'Направление: {self.__branch}')

	def access_private_method(self):
		self.__display_details()

# ниже код для проверки класса Student


adam = Student("Adam Smith", 25, "Information Technology")
piter = Student("Piter Parker", 34, "Information Security")

adam.access_private_method()
assert piter._Student__age == 34, 'Где приватный атрибут __age?'
assert piter._Student__branch == "Information Security", 'Где приватный атрибут __branch?'
assert piter._Student__name == "Piter Parker", 'Где приватный атрибут __name?'
piter.access_private_method()
adam._Student__display_details()
piter._Student__display_details()