def func(phrase):
    try:
        func(phrase)
    except RecursionError:
        print("Кто-то должен остановить это безумие")


func('Это рекурсия, детка!')