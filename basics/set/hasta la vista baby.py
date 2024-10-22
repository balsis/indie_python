my_set = set()
phrase = input().lower().split(',')
print(phrase)
for i in phrase:
	if i not in my_set:
		my_set.add(i)
		print("НЕТ")
	else:
		print('ДА')