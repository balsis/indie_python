def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return sorted(result)

    return wrapper


@decorator
def get_list(s):
    return list(map(int, s.split()))


n = input()
lst = get_list(n)
print(*lst)
