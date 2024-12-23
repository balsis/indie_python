def find_min(lst):
    min_el = lst[0]
    if len(lst) == 1:
        return lst[0]
    else:
        other_min = find_min(lst[1:])
        if min_el > other_min:
            return other_min
        else:
            return min_el


numbers = [-230, 101, 323, -200, 17, -5, 10, -22]
print(find_min(numbers))
