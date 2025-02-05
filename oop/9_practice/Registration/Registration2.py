from string import digits, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(value):
        for digit in digits:
            if digit in value:
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        has_upper = any(letter.isupper() for letter in value)
        has_lower = any(letter.islower() for letter in value)
        return has_upper and has_lower

    @staticmethod
    def is_include_only_latin(value):
        allowed_chars = ascii_letters + digits
        for char in value:
            if char not in allowed_chars:
                return False
        return True

    @staticmethod
    def check_password_dictionary(value: str):
        with open(file = "easy_passwords.txt") as passwords:
            for word in passwords:
                if word.strip() in value:
                    return True
            return False

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        elif "@" not in value:
            raise ValueError
        elif "." not in value.split("@")[1]:
            raise ValueError
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        elif not (5 < len(value) < 12):
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        elif not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value


# Ниже код для проверки класса Registration


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')