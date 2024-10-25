def overlapping(lst1, lst2):
    for item in lst2:
        if is_member(item, lst1):
            return True
    return False


def is_member(value, lst):
    return value in lst


print(overlapping(['nope', 'nothing', 'in'], ['common']))
print(overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this']))
