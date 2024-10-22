with open('words.txt', encoding= 'utf-8') as f:
	lst = [i for i in f.read().upper().split() if i[-2:] == "ЕЯ"]
	my_set = set(lst)
	sorted_lst = sorted(my_set, key=lambda x: (len(x), x))
	for i in sorted_lst:
		print(i)