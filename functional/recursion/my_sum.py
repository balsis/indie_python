def my_sum(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0]+my_sum(lst[1:])

# [1, 2, 3] -> 1) 1 + my_sum([2, 3])
#              2)  1 + 2 + my_sum([3]) -> return 3
#              3) 1 + 2 + 3

