from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    "Находит первый дубль в списке"
    dct = {}
    for i in range(len(words)):
        if words[i] in dct:
            return words[i]
        else:
            dct[words[i]] = 1
    return None


print(get_first_repeated_word(['ab', 'ca', 'bc', 'Ab', 'cA', 'aB', 'bc']))
