def file_read(file_name: str) -> None:
    file = open(file_name, 'r', encoding='utf-8')
    print(file.read())


file_read('111.txt')