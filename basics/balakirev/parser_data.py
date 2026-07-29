

def parser_data(text, /, max_count=0, *, ignore_sign=False):
    lst = []
    cur_char = ""
    for index, char in enumerate(text):
        if char.isdigit():
            cur_char += char
        if not char.isdigit():
            if cur_char.isdigit():
                lst.append(cur_char)
            cur_char = ""


    return lst

res1 = parser_data("Числа: -10, -+40, 4-53, 1, 2-3 -0.01")
print(res1)

# res1: ['-10', '+40', '4', '-53', '1', '2', '-3', '-0', '01']