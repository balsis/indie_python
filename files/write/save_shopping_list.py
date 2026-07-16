def save_shopping_list(items):
    with open("shopping.txt", mode="w", encoding="utf-8") as file:
        file.write("Список покупок:\n")
        for i, item in enumerate(items, 1):
            file.write(f"{i}. {item}\n")


save_shopping_list(['Хлеб', 'Молоко', 'Яйца'])
