cache_values = {}


def factorial(number: int):
    if number in cache_values:
        print(f"Get from cache value factorial({number})")
        return cache_values[number]
    else:
        fact = 1
        for i in range(1, number+1):
            fact *= i
        cache_values[number] = fact
        return fact


print(factorial(5))
print(factorial(6))
print(factorial(5))