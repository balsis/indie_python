def get_combin(n, k):
    if k == 0:
        return 1
    if k == n:
        return 1
    else:
        return get_combin(n-1, k) + get_combin(n-1, k-1)


print(get_combin(6, 3))
