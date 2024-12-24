def sum_digits(digit):
    # print(digit)
    if digit % 10 == digit:
        return digit
    else:
        digit %= 10
        return sum_digits(digit)

#
# print(sum_digits(15))
a =  15
print(a // 10 + a % 10)