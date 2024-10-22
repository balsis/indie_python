def count_AGTC(dna):
    a, g, t, c = dna.count('A'), dna.count('G'), dna.count('T'), dna.count('C')
    return a, g, t, c

# код ниже не стоит удалять, он нужен для проверки
assert count_AGTC('AGGTC') == (1, 2, 1, 1)
assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
assert count_AGTC('CCT') == (0, 0, 1, 2)
print('Проверки пройдены')