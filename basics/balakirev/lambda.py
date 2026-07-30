def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


digs = list(map(int, input().split()))
# 5 4 -3 4 5 -24 -6 9 0

lst = filter_lst(digs)
print(*lst)
lst = filter_lst(digs, lambda x: x < 0)
print(*lst)
lst = filter_lst(digs, lambda x: x >= 0)
print(*lst)
lst = filter_lst(digs, lambda x: x in range(3,6))
print(*lst)

