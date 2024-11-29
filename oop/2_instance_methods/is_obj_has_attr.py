def is_obj_has_attr(obj, attr):
    return True if hasattr(obj, attr) else False

class House:
    color = 'white'
    rooms = 4

print(is_obj_has_attr(House, 'age'))
print(is_obj_has_attr(House, 'kids'))
print(is_obj_has_attr(House, 'cat'))


class Duck:
	weight = 5
	height = 10


print(is_obj_has_attr(Duck, 'weight'))
print(is_obj_has_attr(Duck, 'name'))
print(is_obj_has_attr(Duck, 'height'))

class House:
    color = 'white'
    rooms = 4

print(is_obj_has_attr(House, 'color'))
print(is_obj_has_attr(House, 'rooms'))
print(is_obj_has_attr(House, 'room'))




