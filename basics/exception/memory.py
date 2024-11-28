try:
    print(list(range(10000000000)))
except MemoryError:
    print("У питона память сломалась")
