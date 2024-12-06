def gen_arithmetic_progression(first, difference):
    result =  first
    while True:
        yield result
        result += difference


count = 1
for value in gen_arithmetic_progression(5, 7):
    print(value)
    count += 1
    if count > 5:
        break