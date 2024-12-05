def even_items(lst):
    return [number  for index, number in enumerate(lst, start = 1) if index % 2 ==0]

print(even_items([3, 7, 5, 6, 3, 8, 9]))
