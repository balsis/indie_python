def find_lines_len_more_6(filename: str):
    with open(filename, encoding="utf-8") as file:
        text = file.readlines()
        num = 0
        for line in text:
            if len(line.strip()) > 6:
                num += 1

        return num