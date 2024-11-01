def do_it_something(lst):
    lst[0] = "Курица"
    lst[1] = "карри"
    return lst


values = ['Ребрышки', 'гриль', 'это', 'очень', 'вкусно']
new_values = do_it_something(list(values))
print(values)
print(new_values)