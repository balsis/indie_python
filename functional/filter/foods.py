foods = [
    {'name': "Стейк Рибай", 'type_food': "Основное", 'price': 75.95},
    {'name': "Ассорти из гигантских креветок", 'type_food': "Закуска", 'price': 2029.95},
    {'name': "Оливье", 'type_food': "Салат", 'price': 329.95},
    {'name': "Жареный канадский бекон", 'type_food': "Закуска", 'price': 239.95},
    {'name': "Крабовый пирог", 'type_food': "Закуска", 'price': 532.95},
    {'name': "Цезарь", 'type_food': "Салат", 'price': 14.95},
    {'name': "Пирог из лобстера", 'type_food': "Закуска", 'price': 230.95},
    {'name': "Огурчики", 'type_food': "Закуска", 'price': 123.95},
    {'name': "Мимоза", 'type_food': "Салат", 'price': 223.95},
    {'name': "Овощной", 'type_food': "Салат", 'price': 310.95},
    {'name': "Картошка фри", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Спаржа", 'type_food': "Гарнир", 'price': 455.95},
    {'name': "Стейк Техасский", 'type_food': "Основное", 'price': 1631.95},
    {'name': "Грибы", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Лосось на гриле", 'type_food': "Основное", 'price': 936.95},
    {'name': "Крабовый", 'type_food': "Салат", 'price': 563.95}
]

result = list(map(lambda x: x["name"], filter(lambda x: x if x['type_food'] == 'Салат' else None, foods)))
print(result)
