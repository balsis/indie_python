
# 8 11 -53 2 10 11
lst = list  (
    map(int, input().split())
)

for index in range(len(lst) -1):
    srez = lst[index + 1:]
    minim_srez = min(srez)
    minim_srez_index  = lst.index(minim_srez, index)
    if lst[index] > minim_srez:
        lst[index], lst[minim_srez_index] = minim_srez, lst[index]


print(*lst)