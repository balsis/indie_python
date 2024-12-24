def sum_digits(digit):
    if digit // 10 == 0:
        return digit
    else:
        return digit % 10 + sum_digits(digit // 10)


#
print(sum_digits(15))
# -------------------

# a = 15
# a // 10 - остаток
# a % 10 - последнее число
