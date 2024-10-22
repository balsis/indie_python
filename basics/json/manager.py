import json

with open("manager_sales.json") as f:
	obj = json.load(f)
	max_value = 0
	for i in obj:
		manager = f"{i['manager']['first_name']} {i['manager']['last_name']}"
		summa = 0
		for j in i['cars']:
			summa += j['price']
		if summa >= max_value:
			max_value = summa
		print(f"{manager} - {summa}")
	print(max_value)
