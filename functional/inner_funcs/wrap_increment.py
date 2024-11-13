def wrap_increment(value):
    def _inc(value):
        return value+1
    return _inc(value)


print(wrap_increment(41))
