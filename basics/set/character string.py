n = input()
lst = [i for i in n if i.isdigit()]
my_set = set()
for i in lst:
	if lst.count(i)>1:
		my_set.add(i)

print(
	*sorted(my_set) if len(my_set)>0 else ["NO"]
)



