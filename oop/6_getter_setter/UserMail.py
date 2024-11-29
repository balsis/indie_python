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


jim = UserMail("aka47", 'hello@com.org')
assert jim.login == "aka47"
assert jim._UserMail__email == "hello@com.org"
assert isinstance(jim, UserMail)
assert isinstance(type(jim).email, property), 'Вы не создали property email'

jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
jim.email = 'hello@@re.ee'  # печатает ErrorMail:hello@@re.ee
jim.email = 'hello@re.w3'
print(jim.email)
assert jim.email == 'hello@re.w3'

k = UserMail('belosnezhka', 'prince@wait.you')
assert k.email == 'prince@wait.you'
assert k.login == 'belosnezhka'
assert isinstance(k, UserMail)

k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
k.email = 'prince@still@.wait'  # печатает ErrorMail:prince@still@.wait
k.email = 'prince@stillwait'  # печатает ErrorMail:prince@stillwait
k.email = 'prince@still.wait'
assert k.get_email() == 'prince@still.wait'
k.email = 'pri.nce@stillwait'  # печатает ErrorMail:pri.nce@stillwait
assert k.email == 'prince@still.wait'
