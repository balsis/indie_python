def parser_data(text, /, max_count=0, *, ignore_sign=False):
    lst = []
    cur_char = ""
    sign = ""

    for char in text:

        if char in "+-":
            if cur_char:
                if ignore_sign:
                    cur_char = cur_char.lstrip("+-")
                lst.append(cur_char)

                if max_count and len(lst) >= max_count:
                    return lst

                cur_char = ""

            sign = char

        elif char.isdigit():
            if not cur_char:
                cur_char += sign
                sign = ""

            cur_char += char

        else:
            if cur_char:
                if ignore_sign:
                    cur_char = cur_char.lstrip("+-")

                lst.append(cur_char)

                if max_count and len(lst) >= max_count:
                    return lst

                cur_char = ""

            sign = ""

    if cur_char:
        if ignore_sign:
            cur_char = cur_char.lstrip("+-")
        lst.append(cur_char)

    return lst[:max_count] if max_count else lst


res1 = parser_data("Числа: -10, -+40, 4-53, 1, 2-3 -0.01")
print(res1)

# res1: ['-10', '+40', '4', '-53', '1', '2', '-3', '-0', '01']
