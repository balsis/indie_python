dct = {}
while True:
    inp = input().split()
    if inp[0] == "конец":
        break
    dct.setdefault(inp[0].replace(',', ''), []).append(int(inp[1]))
dct2 = {}
for key, values in dct.items():
    dct2[key] = sum(values) / len(values)

dct3 = sorted(dct2.items(), key=lambda x: (-x[1], x[0]))
for i in dct3:
    print(f"{i[0]} {i[1]}")