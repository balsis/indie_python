def are_anagrams(s1, s2, *, start=0, end=-1, ignore_case=True):
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    if end == -1:
        s1 = s1[start:]
        s2 = s2[start:]
    else:
        s1 = s1[start:end]
        s2 = s2[start:end]
    return sorted(s1) == sorted(s2)

res1 = are_anagrams("Кот", "ток") # True
res2 = are_anagrams("ТИКТОК", "кит", end=3) # True
res3 = are_anagrams("Кот", "ток", ignore_case=False) #False
print(res1)
print(res2)
print(res3)