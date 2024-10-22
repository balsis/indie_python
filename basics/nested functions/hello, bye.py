def outer() -> None:
    def say_hello() -> None:
        print('hello')

    def say_bye() -> None:
        print('bye')


    say_bye()
    say_hello()
outer()