n, m = map(int, input().split())
mas = []
mas.append('.' * (m + 2))
for i in range(n):
	row = '.' + input() + '.'
	mas.append(row)
mas.append('.' * (m + 2))

count = 0

for i in range(1, n+1):
	for j in range(1, m+1):
		if mas[i-1][j] =='.' and mas[i][j+1]=='.' and mas[i+1][j]=='.' and mas[i][j-1]=='.' and mas[i][j] =='.':
			count+=1

print(count)