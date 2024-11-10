average = lambda *args: sum(args)/len(args)


print(average.__name__)
print(average(4, 5, 6))