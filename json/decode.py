import json

with open("Abracadabra__1_.txt") as txt, open("Alphabet.json") as j:
	data = json.load(j)
	lst = []
	for i in txt.read():
		if i.isalpha():
			lst.append(data[i])
		else:
			lst.append(i)
	result = "".join(lst)
	print(result)
