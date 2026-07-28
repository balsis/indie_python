def count_chars(s:str, chars: str, return_type: type[tuple | list | set] = tuple, ignore_case: bool = True):
    s = s.lower() if ignore_case else s
    chars = chars.lower() if ignore_case else chars

    dct = {char: s.count(char) for char in chars}
    if return_type == tuple:
        return (*dct.values(),)
    elif return_type == list:
        return list(dct.values())
    else:
        return set(dct.values())






