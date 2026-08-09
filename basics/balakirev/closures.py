def logger(func):
    print(f"[ДЕКОРИРОВАНИЕ] Получена функция: {func.__name__} с ID={id(func)}")
    def wrapper(*args, **kwargs):
        print(f"[ВЫЗОВ] Сейчас вызовем замкнутую функцию с ID={id(func)}")
        result = func(*args, **kwargs)
        print("[ВЫЗОВ] Завершили")
        return result
    #print(wrapper.__closure__)
    print(f"[ДЕКОРИРОВАНИЕ] Создана обёртка wrapper с ID={id(wrapper)}")
    return wrapper


# Применяем декоратор
@logger
def say_hello(name):
    print(f"  Привет, {name}!")
    return "OK"


# Теперь вызываем
print("\n--- ВЫЗОВ 1 ---")
say_hello("Алексей")

# Исходная функция спрятана внутри замыкания
print("\n--- ИНСПЕКЦИЯ ЗАМЫКАНИЯ ---")
print(f"Обёртка указывает на ячейки: {say_hello.__closure__}")
print(f"В ячейке лежит: {say_hello.__closure__[0].cell_contents}")
# (если без wraps, то wrapped нет, но ID совпадут)
print("\n--- ВЫЗОВ 2 ---")
say_hello("Мария")