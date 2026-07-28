def get_data_fig(*args, **kwargs):
    d = (sum(args), )
    for key in ("tp", "color", "closed", "width"):
        if key in kwargs:
            d += (kwargs[key],)
    return d


d = list(map(int, input().split()))
print(*get_data_fig(*d))
print(*get_data_fig(*d, tp=True))
print(*get_data_fig(*d, color=7, tp=True))
print(*get_data_fig(*d, width=2.0, closed=False))