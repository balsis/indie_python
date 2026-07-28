
def filter_by_length(*args, min_length=0, max_length):
    return [item for item in args if len(item) >= min_length and len(item) <= max_length]



arg = ['Саровский', 'Рублёв', 'Брюллов', 'Репин', 'Лобачевский', 'Менделеев', 'Павлов', 'Ландау', 'Суворов']
result = filter_by_length(arg, min_length=5, max_length=10)
print(result)