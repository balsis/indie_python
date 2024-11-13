def get_info_about_object(func: object):
    print(dir(func))
    print(f'Всего у объекта {len(dir(func))} атрибутов и методов')


def print_goods(lst):
    pass


get_info_about_object(print_goods)
