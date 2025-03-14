class User:
    def __init__(self, username, passsword):
        self.username = username
        self.password = passsword

    def get_info(self):
        return f'Имя пользователя: {self.username}'


class Authentication(User):
    def authenticate(self, username, password):
        return self.username == username and self.password == password


class AuthenticatedUser(Authentication, User):
    pass


# Ниже расположены проверки для кода


assert issubclass(AuthenticatedUser, User) is True
assert issubclass(AuthenticatedUser, Authentication) is True

user1 = AuthenticatedUser('user1', 'password1')
assert user1.get_info() == 'Имя пользователя: user1'
assert user1.authenticate('user1', 'password2') is False
assert user1.authenticate('user1', 'password1') is True

ted = AuthenticatedUser('ted_lawyer', 'alligator3')
print(ted.get_info())