def find_lines_len_more_6(file_name:str) -> int:
    with open(file_name, "r") as f:
        count = 0
        for i in f.read().splitlines():
            if len(i)>6:
                count+=1
        return count

print(find_lines_len_more_6("lines.txt"))
