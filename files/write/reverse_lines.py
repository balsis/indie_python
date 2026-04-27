def reverse_lines(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        text1 = file.readlines()

    with open("reversed.txt", mode="w", encoding="utf-8") as file:
        text2 = file.writelines(text1[::-1])


reverse_lines("shopping.txt")
