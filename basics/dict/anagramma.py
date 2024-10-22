# Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
# Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO

str1, str2 = input(), input()
dct1, dct2 = {}, {}

for i in str1:
    dct1[i] = dct1[i] + 1 if i in dct1 else 1

for i in str2:
    dct2[i] = dct2[i] + 1 if i in dct2 else 1

print("YES") if dct1 == dct2 else print("NO")

