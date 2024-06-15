# Перед вами словарь workers
# Ваша задача поднять зарплату Бреду до 8500 и затем вывести измененный словарь workers

workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}
for worker in workers:
    if workers[worker]['name'] == 'Brad':
        workers[worker]['salary'] = 8500

print(workers)