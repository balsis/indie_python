def gen_factorial():
    result, i = 1, 1
    while True:
        result *= i
        i += 1
        yield result


count = 1
for value in gen_factorial():
    print(value)
    count += 1
    if count > 10:
        break
