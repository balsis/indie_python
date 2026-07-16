def print_first_two_lines(filename: str):
    file = open(filename)
    print(file.readline().strip())
    print(file.readline().strip())
