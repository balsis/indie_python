def lorem(file_name:str) -> int:
	with open(file_name, "r") as f:
		lst = [i for i in f.read().lower().replace('\n', ' ').split(' ')]
		return len(set(lst))

print(lorem("lorem.txt"))

