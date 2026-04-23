def find_words_ending_with_eya(filename):
    with open(filename, encoding="utf-8") as file:
        words = file.read().strip().split()
        eya_words = [word.upper() for word in words if "ЕЯ" in word.upper()]
        eya_list = list(set(eya_words))
        new = sorted(eya_list, key=lambda x: (len(x), x))

        print("\n".join(new))


print(find_words_ending_with_eya("eya.txt"))