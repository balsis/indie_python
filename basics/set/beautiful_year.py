a = input()
for i in range(int(a)+1, 9999):
	if len(set(list(str(i))))==4:
		print(i)
		break