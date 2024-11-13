def double_odd_numbers(numbers):
    def double(num):
        return num * 2

    def is_odd(num):
        return True if num % 2 != 0 else False

    return [double(num) for num in numbers if is_odd(num)]


print(double_odd_numbers([1, 2, 3, 4, 5]))
print(double_odd_numbers([6, 8, 10, 2]))
print(double_odd_numbers([-43, 91, 932, 9201, 32, 93]))
