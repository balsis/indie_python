def my_func(collection, n):
    collection = list(collection)
    for i in range(1, n + 1):
        collection.append(i)
    return collection


a = [10, 20, 30]
res = my_func(a, 3)
print(a)
print(res)
