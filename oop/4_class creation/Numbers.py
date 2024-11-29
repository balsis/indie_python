class Numbers:
	def __init__(self, *args):
		self.lst = [*args]

	# print(self.lst)
	def add_number(self, numeric):
		self.lst.append(numeric)

	def get_positive(self):
		return [i for i in self.lst if i > 0]

	def get_negative(self):
		return [i for i in self.lst if i < 0]

	def get_zeroes(self):
		return [i for i in self.lst if i == 0]


nums = Numbers()
print(nums.get_positive())
print(nums.get_negative())
print(nums.get_zeroes())

nums.add_number(5)
nums.add_number(3)
nums.add_number(4)

print(nums.get_positive())
print(nums.get_negative())
print(nums.get_zeroes())
