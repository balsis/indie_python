class CustomLabel:
	def __init__(self, text, **kwargs):
		self.text = text
		for key, value in kwargs.items():
			self.__dict__[key] = value

	def config(self, **kwargs):
		self.__dict__.update(**kwargs)


label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
print(label1.__dict__)
label1.config(color='red', bg=100)
print(label1.__dict__)
