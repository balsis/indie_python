shopping_list = {}


def add_item(item: str, number: int = 1) -> None:
    if shopping_list.get(item):
        shopping_list[item] = shopping_list[item] + number
    else:
        shopping_list[item] = number




add_item("Bread", 10)
add_item("Potato", 5)
add_item("Milk")
add_item("Orange", 3)
add_item("Orange", 2)
add_item("Milk")
add_item("Bread", 3)

print(shopping_list)