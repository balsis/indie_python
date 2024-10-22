MIN_DRIVING_AGE = 18

def allowed_driving(name: str, age: int) -> None:
    print(f'{name} может водить') if age >= MIN_DRIVING_AGE else print(f'{name} еще рано садиться за руль')

allowed_driving('bob', 18)