import os

# Получаем все переменные окружения
env_vars = os.environ

# Выводим их
for key, value in env_vars.items():
    print(f"{key}: {value}")