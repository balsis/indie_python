x = 40

def my_func():
    global x
    print(x)
    x *= 2


print(x)
my_func()
print(x)