def list_sum_recursive(lst):
    if len(lst) == 0:
        print(0)
        return 0
    if len(lst) == 1:
        print('0=', lst[0])
        return lst[0]
    print('rec=', lst[0] + list_sum_recursive(lst[1:]))
    return lst[0] + list_sum_recursive(lst[1:])


lst = [1, 2, 3]
# lst = list(map(int, input().split()))
print(list_sum_recursive(lst))
