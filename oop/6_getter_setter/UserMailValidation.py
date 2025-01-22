class UserMail:
	def __init__(self, login, email):
		self.login = login
		self.__email = email

	def get_email(self):
		return self.__email

	def set_email(self, email):
		if isinstance(email, str) and email.count("@") == 1 and email.count(".") == 1 and email.index("@") < email.index(
				"."):
			self.__email = email

		else:
			print(f"ErrorMail:{email}")

	email = property(fget=get_email, fset=set_email)