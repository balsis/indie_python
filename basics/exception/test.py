lst = []

while True:
    command = input().lower()
    if command == 'exit':
        break
    if command == 'add':
        number = int(input())
        lst.append(number)
        print(f'Значения списка = {lst}')
    elif command == 'get':
        index = int(input())
        print(lst[index])
    elif command == 'delete':
        value = int(input())
        lst.remove(value)
        print(f'Значения списка = {lst}')
    else:
        continue
print('Завершили работу')