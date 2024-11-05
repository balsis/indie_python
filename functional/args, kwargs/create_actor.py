def create_actor(name: str = "Райан", surname: str = "Рейнольдс", age: int = 47, **kwargs):
    return {
        'name': name,
        'surname': surname,
        'age':age,
        **kwargs
    }


print(create_actor(height = 190, movies = ['Дедпул', 'Главный герой']))
