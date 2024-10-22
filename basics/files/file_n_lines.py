def file_n_lines(file_name: str, n: int) -> None:
    file = open(file_name, 'r', encoding='utf-8')
    for i in range(n):
        print(file.readline().strip())

file_n_lines('hello.txt', 3)