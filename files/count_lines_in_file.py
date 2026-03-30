
def count_lines_in_file(filename: str):
    file = open(file=filename, mode="r")
    text = file.read()
    text_list = text.split('\n')
    text_len = 0 if text_list[0] == "" else len(text_list)
    file.close()
    return text_len

print(count_lines_in_file("i_love_python.txt"))