users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}

class UserNotFoundError(Exception):
    pass


def get_user(username):
    try:
        return users.get(username).get("name")
    except AttributeError:
        raise UserNotFoundError('User not found')
try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)