import recipes

def main():
    dish = input("Введите название блюда (паста, салат, бутерброд): ")
    recipe = recipes.get_recipe(dish)

    if recipe is None:
        print("Такого рецепта нет.")
        return

    portions = int(input("Сколько порций вы хотите? "))
    scaled = recipes.scale_recipe(recipe, portions)

    print(f"\nИнгредиенты на {portions} порций:")
    for ingredient, amount in scaled.items():
        print(f"- {ingredient}: {amount} г")

main()