import json

with open("group_people.json") as f:
	data = json.load(f)
	result = {}
	for group in data:
		female_sum = 0
		# print(group['id_group'])
		for person in group["people"]:
			if person['gender'] == 'Female' and person['year'] > 1977:
				female_sum += 1
		result[group['id_group']] = female_sum

value = max(result.values())
key = [key for key, v in result.items() if v == value]
print(*key, value)
