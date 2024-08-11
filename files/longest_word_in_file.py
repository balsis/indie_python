from string import punctuation


def longest_word_in_file(file_name: str) -> str:
	file = open(file_name, encoding='utf-8')
	a = file.read()
	for symbol in punctuation:
		a = a.replace(symbol, '')
	max_len, max_word = 0, None
	for word in a.split():
		if len(word) >= max_len:
			max_len = len(word)
			max_word = word
	return max_word


longest_word_in_file('branches.txt')
