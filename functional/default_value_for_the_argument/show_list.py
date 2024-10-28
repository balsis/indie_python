def show_list(include_quantities: bool = True) -> None:
    for item, numbers in shopping_list.items():
        print(f"{numbers}x{item}") if include_quantities else print(item)


shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}
show_list()
show_list(include_quantities = False)
