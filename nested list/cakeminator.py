r,c = map(int, input().split()) # r - строки; c- стоолбцы
tort = []
for i in range(r):
	tort.append(input())

mass = [[False]*c for i in range(r)]

for i in range(r):
	if 'S' not in tort[i]:
		for j in range(c):
			mass[i][j]= True
for j in range(c):
	is_find = False
	for i in range(r):
		if tort[i][j] == "S":
			is_find = True
			break
	if not is_find:
		for i in range(r):
			mass[i][j] = True
count = 0
for row in mass:
	count +=row.count(True)

print(count)