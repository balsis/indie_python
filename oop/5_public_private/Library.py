class Library:
	def __init__(self, books: list):
		self.__books = books

	def __check_availability(self, name):
		return name in self.__books

	def search_book(self, name):
		return self.__check_availability(name)

	def return_book(self, name):
		self.__books.append(name)

	def _checkout_book(self, name):
		if self.__check_availability(name):
			self.__books.remove(name)
			return True
		return False

# Ниже код для проверки методов класса Library
library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')