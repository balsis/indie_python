# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
# Сложным паролем будет считаться комбинация символов, в которой :
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

def check_password(password):
    a, b, c = [], [], []
    for i in password:
        if i.isdigit():
            a.append(i)
        if i.isupper():
            b.append(i)
        if i in '!@#$%*':
            c.append(i)
    if len(password) >= 10 and len(a) >= 3 and len(b) >= 1 and len(c) >= 1:
        print('Perfect password')
    else:
        print('Easy peasy')


check_password("Qwerty1357!")
