with open("lorem.txt", "r") as f:
	lst = [i for i in f.read().upper().replace('\n', ' ').split(' ')]
	dct = {}
	for i in lst:
		if i in dct:
			dct[i] += 1
		else:
			dct[i] = 1
	print(f"words = {dct}")
