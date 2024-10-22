def get_body_mass_index(weight, height):
    index = weight / (height/100) ** 2
    if index < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= index <= 25:
        print('Норма')
    else:
        print('Избыточная масса тела')

get_body_mass_index(85, 175)