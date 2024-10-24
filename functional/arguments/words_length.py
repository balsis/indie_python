from typing import List


def words_length(lst: List) -> List:
    return [len(_) for _ in lst]


print(words_length(['Hello', 'world!']))
