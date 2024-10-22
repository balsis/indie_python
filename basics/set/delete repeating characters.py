n = input()
my_set = set(n)
for i in n:
	if i in my_set:
		print(i, end = '')
		my_set.remove(i)

