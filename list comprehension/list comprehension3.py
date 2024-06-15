from string import ascii_uppercase

# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита ['A', 'B', 'C', 'D', ...].

print([ascii_uppercase[i] for i in range(int(input()))])

# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]

print([ascii_uppercase[i] * (i + 1) for i in range(int(input()))])
