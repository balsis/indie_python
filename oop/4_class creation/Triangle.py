class Triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def is_exists(self):
		return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

	def is_equilateral(self):
		return self.a == self.b == self.c and self.is_exists() == True

	def is_isosceles(self):
		return True if self.is_exists() == True and (
				self.a == self.b or self.b == self.c or self.c == self.a) else False


triangle = Triangle(3, 4, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")

print('----------------------------------------')

triangle = Triangle(5, 5, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")

print('----------------------------------------')

triangle = Triangle(5, 4, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")

print('----------------------------------------')

triangle = Triangle(5, 16, 5)
print(f"Is Triangle exist: {triangle.is_exists()}")
print(f"Is Equilateral: {triangle.is_equilateral()}")
print(f"Is Isosceles: {triangle.is_isosceles()}")
