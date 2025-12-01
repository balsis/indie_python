def get_recipe(dish_name):
    recipes = {
        "паста": {"макароны": 100, "соус": 50, "сыр": 30},
        "салат": {"помидоры": 50, "огурцы": 50, "масло": 20},
        "бутерброд": {"хлеб": 2, "сыр": 1, "ветчина": 1}
    }
    return recipes.get(dish_name.lower())

def scale_recipe(recipe, portions):
    return {ingredient: amount * portions for ingredient, amount in recipe.items()}