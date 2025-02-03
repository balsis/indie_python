class User:
    def __init__(self, name, role):
        self.name =  name
        self.role = role

class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        return True if role in Access.__access_list else False

    @staticmethod
    def get_access(user):
        if isinstance(user, User) and Access.__check_access(user.role):
            print(f'User {user.name}: success')
        elif not isinstance(user, User):
            print("AccessTypeError")
        else:
            print('AccessDenied')

user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError